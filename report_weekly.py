import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from dotenv import load_dotenv

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
except ImportError:
    print("Error: Missing google-analytics-data package. Please pip install -r requirements.txt")
    sys.exit(1)

# Load config
load_dotenv()

GA4_PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
MAIL_FROM = os.getenv("MAIL_FROM")
TARGET_EMAILS = [e.strip() for e in os.getenv("REPORT_TARGET_EMAILS", "").split(",") if e.strip()]

def get_ga4_data():
    """Fetch GA4 traffic and event data for the past 7 days."""
    client = BetaAnalyticsDataClient()
    
    # Query 1: Overall Sessions
    session_req = RunReportRequest(
        property=f"properties/{GA4_PROPERTY_ID}",
        metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
    )
    session_res = client.run_report(session_req)
    total_sessions = int(session_res.rows[0].metric_values[0].value) if session_res.rows else 0
    total_users = int(session_res.rows[0].metric_values[1].value) if session_res.rows else 0

    # Query 2: CTA Click Events
    event_req = RunReportRequest(
        property=f"properties/{GA4_PROPERTY_ID}",
        dimensions=[Dimension(name="eventName")],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
    )
    event_res = client.run_report(event_req)
    
    events = {}
    total_conversions = 0
    for row in event_res.rows:
        event_name = row.dimension_values[0].value
        count = int(row.metric_values[0].value)
        events[event_name] = count
        if event_name.startswith("click_cta_"):
            total_conversions += count

    cvr = (total_conversions / total_sessions * 100) if total_sessions > 0 else 0.0

    return total_sessions, total_users, total_conversions, cvr, events

def send_email(sessions, users, conversions, cvr, events):
    """Send formatted email via SMTP."""
    subject = f"【STRETCH+】週次GA4運用レポート ({datetime.now().strftime('%Y/%m/%d')})"
    
    body = f"""
STRETCH+ 運用ご担当者様

直近7日間のWEBサイトの運用レポートをお届けします。

■ 全体トラフィック
- 総セッション数: {sessions} 回
- 訪問ユーザー数: {users} 人

■ コンバージョン (CTAクリック総数)
- コンバージョン数: {conversions} 回
- CVR（着地率）: {cvr:.2f} %

■ 各ボタン別のクリック内訳
"""
    for ev, count in events.items():
        if ev.startswith("click_cta_"):
            body += f" - {ev.replace('click_cta_', '')}: {count}回\n"
            
    body += """
--------------------------------------------------
※このメールはサーバー（Bot）より自動送信されています。
"""

    msg = MIMEMultipart()
    msg['From'] = MAIL_FROM
    msg['To'] = ", ".join(TARGET_EMAILS)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
    print("Email sent successfully.")

if __name__ == "__main__":
    if not GA4_PROPERTY_ID or not SMTP_SERVER:
        print("Setup Incomplete: Please configure .env parameters first.")
        sys.exit(1)
        
    try:
        sessions, users, conversions, cvr, events = get_ga4_data()
        send_email(sessions, users, conversions, cvr, events)
    except Exception as e:
        print(f"Error fetching data or sending email: {e}")
