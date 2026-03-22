import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv
import random

try:
    import anthropic
except ImportError:
    print("Error: anthropic package is missing. Please run: pip3 install anthropic python-dotenv")
    sys.exit(1)

# .env を読み込む
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465)) if os.getenv("SMTP_PORT") else 465
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
MAIL_FROM = os.getenv("MAIL_FROM")
TARGET_EMAILS = [e.strip() for e in os.getenv("REPORT_TARGET_EMAILS", "").split(",") if e.strip()]

def get_dummy_data():
    """GA4からの取得をシミュレーションしたダミーデータ"""
    sessions = random.randint(1500, 3000)
    events = [
        f"click_cta_web: {random.randint(20, 50)}回",
        f"click_cta_line: {random.randint(10, 30)}回",
        f"click_cta_hotpepper: {random.randint(5, 15)}回",
        f"click_cta_rakuten: {random.randint(1, 10)}回"
    ]
    return sessions, events

def generate_ai_analysis(sessions, events_list):
    """ダミーデータをもとにAnthropic APIへ分析をリクエスト"""
    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY.startswith("sk-ant-api03-..."):
        return "【注意】Anthropic APIキーが未設定のため、AI分析はスキップされました。\nAPIキーを設定すると、ここに具体的な改善提案文章が自動生成されます。"
        
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    events_str = "\n".join(events_list)
    prompt = f"""
あなたはSTRETCH+（ストレッチ専門店）の専属Webマーケターです。
以下はテスト用のダミーデータですが、過去30日間のGoogle Analytics 4のデータを分析し、サイト改善のための提案を3つ出力してください。
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
    print("Anthropic (Claude) に分析を依頼中...（数秒かかります）")
    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1500,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        print(f"Anthropic API制限または認証エラーを検知しました: {e}")
        return f"【AI分析エラー】\nAnthropicのAPI呼び出しに失敗しました（利用枠不足、またはエラー）。\nAnthropicの管理画面（Billing）にてクレジットカード設定や残高のチャージが行われているかご確認ください。\n\n詳細なエラー文:\n{e}"

def send_test_email(sessions, events_list, ai_report):
    subject = f"【テスト配信】STRETCH+ 月次AI分析＆改善提案レポート ({datetime.now().strftime('%Y/%m')})"
    
    events_str = "\n".join(events_list)
    body = f"""STRETCH+ 運用チームの皆様

※本メールは配信テスト用のダミーレポートです※
過去30日間の運用データに基づく、今月のAI分析・改善提案レポートをお届けします。

■ 今月のトラフィック（ダミーデータ）
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

    print("メールを送信中...")
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

if __name__ == "__main__":
    if not SMTP_SERVER or not SMTP_USER or not SMTP_PASS:
        print("エラー: .env にSMTP（メール）の設定が不足しています。")
        sys.exit(1)
        
    try:
        sessions, ev_list = get_dummy_data()
        ai_report = generate_ai_analysis(sessions, ev_list)
        send_test_email(sessions, ev_list, ai_report)
        print("✅ テストAIレポートのメール送信が完了しました！受信トレイをご確認ください。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
