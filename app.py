from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from mongodb_house import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import  os
import json
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token #render環境變數
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret #render環境變數
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    write_one_data(eval(body.replace('false','False')))
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if msg =='法律諮詢':
        message = buttons_message_law()
        line_bot_api.reply_message(event.reply_token, message)

    elif msg =='修繕服務':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '修繕服務',
                contents = json.load(open('fix.json', 'r', encoding='utf-8'))  
            )) 

    elif msg =='收款':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '收款',
                contents = json.load(open('check.json', 'r', encoding='utf-8'))  
            )) 
    elif msg =='繳費查詢':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '繳費查詢',
                contents = json.load(open('unpaid_notice.json', 'r', encoding='utf-8'))  
            )) 
    elif msg =='繳費':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '繳費',
                contents = json.load(open('fee.json', 'r', encoding='utf-8'))  
            )) 

    elif msg =='查詢繳納狀況':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '查詢繳納狀況',
                contents = json.load(open('paid_read.json', 'r', encoding='utf-8'))  
            ))
    elif msg =='合約專區':#(房客)
        message = buttons_message_contract1()
        line_bot_api.reply_message(event.reply_token, message)
        
    elif msg =='合約':#(房東)
        message = buttons_message_contract2()
        line_bot_api.reply_message(event.reply_token, message)

    elif msg =='確認合約':#(房客)
        message = Confirm_Template_contract()
        line_bot_api.reply_message(event.reply_token, message)

    elif msg =='@ok':
    #==========資料庫(查詢對話紀錄功能)=============
        datas = read_chat_records()
        print(type(datas))
        n = 0
        text_list = []
        for data in datas:
            if '@' in data:
                continue
            else:
                text_list.append(data)
            n+=1
        data_text = '\n'.join(text_list)
        message = TextSendMessage(text=data_text[:5000])
        line_bot_api.reply_message(event.reply_token, message) 
    #==========資料庫(查詢對話紀錄功能)=============
    #============確認功能==============
        message2 = Confirm_Template()
        line_bot_api.push_message('U07a91bc93fb0c609e7df95ec39bc630a', message2)  
    #============確認功能============== 
    
    elif msg =='簽約流程一覽':
        message = Carousel_Template1()
        line_bot_api.reply_message(event.reply_token, message)
    elif msg =='常見租屋陷阱':
        message = Carousel_Template2()
        line_bot_api.reply_message(event.reply_token, message)
    elif msg =='退租注意事項':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '退租注意事項',
                contents = json.load(open('go.json', 'r', encoding='utf-8'))  
            )) 
    elif msg =='看房注意事項':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '看房注意事項',
                contents = json.load(open('look_house.json', 'r', encoding='utf-8'))  
            )) 
    elif msg =='簽約注意事項':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '簽約注意事項',
                contents = json.load(open('sign.json', 'r', encoding='utf-8'))  
            )) 
    elif msg =='租屋須知':
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
        
    elif msg =='@我要找房':
    #=======資料庫(刪除功能)===========
        text = delete_all_data()
        message = TextSendMessage(text=text)
        line_bot_api.reply_message(event.reply_token, message)   
    #=======資料庫(刪除功能)===========
    #==========房屋篩選===============
        line_bot_api.push_message('U07a91bc93fb0c609e7df95ec39bc630a',
            FlexSendMessage(
                alt_text = '房屋條件篩選',
                contents = json.load(open('select.json', 'r', encoding='utf-8'))  
            )) 
    #==========房屋篩選===============
    
    elif msg =='是':
        line_bot_api.reply_message(event.reply_token,
            FlexSendMessage(
                alt_text = '房屋',
                contents = json.load(open('house.json', 'r', encoding='utf-8'))  
            )) 
        
    #======MongoDB操作範例======
    elif msg =='@讀取':
        datas = read_many_datas()
        datas_len = len(datas)
        message = TextSendMessage(text=f'資料數量，一共{datas_len}條')
        line_bot_api.reply_message(event.reply_token, message)

    elif msg =='分租套房':
        datas = col_find('events')
        message = TextSendMessage(text=str(datas))
        line_bot_api.reply_message(event.reply_token, message)
    #======MongoDB操作範例======
    else:
        pass

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
