import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
    import anthropic
except ImportError:
    print("Error: Missing packages. Please pip install -r requirements.txt")
    sys.exit(1)

load_dotenv()

GA4_PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
MAIL_FROM = os.getenv("MAIL_FROM")
TARGET_EMAILS = [e.strip() for e in os.getenv("REPORT_TARGET_EMAILS", "").split(",") if e.strip()]

def get_monthly_data():
    """Fetch GA4 traffic for the past 30 days."""
    client = BetaAnalyticsDataClient()
    req = RunReportRequest(
        property=f"properties/{GA4_PROPERTY_ID}",
        metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="yesterday")],
    )
    res = client.run_report(req)
    sessions = int(res.rows[0].metric_values[0].value) if res.rows else 0

    event_req = RunReportRequest(
        property=f"properties/{GA4_PROPERTY_ID}",
        dimensions=[Dimension(name="eventName")],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="yesterday")],
    )
    event_res = client.run_report(event_req)
    events_list = [f"{r.dimension_values[0].value}: {r.metric_values[0].value}回" for r in event_res.rows if "click_cta_" in r.dimension_values[0].value]
    
    return sessions, events_list

def generate_ai_analysis(sessions, events_list):
    """Use Anthropic Claude to analyze data and suggest improvements."""
    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY.startswith("sk-ant-api03-..."):
        return "AI APIキーが未設定のため、改善提案はスキップされました。"
        
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    events_str = "\n".join(events_list)
    prompt = f"""
あなたはSTRETCH+（ストレッチ専門店）の専属Webマーケターです。
過去30日間のGoogle Analytics 4のデータを分析し、サイト改善のための提案を3つ出力してください。
日本のビジネス形式で、丁寧に解説してください。

【直近30日のデータ】
・総セッション数: {sessions}
・各ボタンのクリック数:
{events_str}

【レポートフォーマット】
1. 今月のパフォーマンス概要
2. 注目すべきポイント
3. 次月の改善アクションプラン（3つ）
"""

    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1500,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"【AI分析エラー】\nAnthropicのAPI呼び出しに失敗しました。\nAnthropicの管理画面（Billing）にてAPIの利用枠（残高クレジット）をご確認ください。\n\n詳細エラー:\n{e}"

def send_monthly_email(sessions, events_list, ai_report):
    subject = f"【STRETCH+】月次AI分析＆改善提案レポート ({datetime.now().strftime('%Y/%m')})"
    
    events_str = "\n".join(events_list)
    body = f"""STRETCH+ 運用チームの皆様

過去30日間の運用データに基づく、今月のAI分析・改善提案レポートをお届けします。

■ 今月のトラフィック（過去30日）
- 総セッション数: {sessions}
- コンバージョン内訳:
{events_str}

==================================================
🤖 AIによる分析・改善提案レポート
==================================================
{ai_report}
==================================================

※本レポートはGA4データに基づきAIが自動生成しています。
"""

    msg = MIMEMultipart()
    msg['From'] = MAIL_FROM
    msg['To'] = ", ".join(TARGET_EMAILS)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

if __name__ == "__main__":
    if not GA4_PROPERTY_ID or not SMTP_SERVER:
        print("Setup Incomplete: Please configure .env parameters first.")
        sys.exit(1)
        
    try:
        sessions, ev_list = get_monthly_data()
        ai_report = generate_ai_analysis(sessions, ev_list)
        send_monthly_email(sessions, ev_list, ai_report)
        print("Monthly AI Report sent.")
    except Exception as e:
        print(f"Error: {e}")
