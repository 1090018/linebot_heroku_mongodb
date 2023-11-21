from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import schedule
import time
import datetime

app = Flask(__name__)

# 設置 LINE Bot 的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# LINE Bot 的訊息處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text.lower()
    if '繳錢' in message_text:  # 當收到包含「繳錢」的訊息時
        reply_text = "別忘了每個月的5日要繳錢喔！"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

# 設置每月5日的提醒
def remind_to_pay():
    today = datetime.date.today()
    if today.day == 5:
        line_bot_api.push_message('YOUR_USER_ID', TextSendMessage(text="別忘了今天要繳錢喔！"))

# 設置每天定時檢查是否要提醒
def schedule_reminder():
    schedule.every().day.at("08:00").do(remind_to_pay)  # 每天早上8點檢查

# 在Flask啟動時開始執行定時任務
@app.before_first_request
def activate_job():
    schedule_reminder()

# LINE Bot 的 Webhook 處理
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

if __name__ == "__main__":
    app.run()
