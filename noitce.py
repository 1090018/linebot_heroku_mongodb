from linebot.models import *
# LINE Bot 的訊息處理

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
