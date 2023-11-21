#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message_law():
    message = TemplateSendMessage(
        alt_text='合約',
        template=ButtonsTemplate(
            title="請選擇您需要的合約服務",
            text="以下是我們提供的服務：",
            actions=[
                URITemplateAction(
                    label="合約範本",
                    uri="https://storage.cloud.google.com/pig_house/%E5%90%88%E7%B4%84/%E4%BD%8F%E5%AE%85%E7%A7%9F%E8%B3%83%E5%AE%9A%E5%9E%8B%E5%8C%96%E5%A5%91%E7%B4%84%E7%AF%84%E6%9C%AC%20(1).pdf"
                ),
                MessageTemplateAction(
                    label="上傳合約",
                    text="上傳合約"
                ),
                MessageTemplateAction(
                    label="查看合約",
                    text="查看合約"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message_contract():
    message = TemplateSendMessage(
        alt_text='合約',
        template=ButtonsTemplate(
            title="請選擇您需要的合約服務",
            text="以下是我們提供的服務：",
            actions=[
                URITemplateAction(
                    label="合約範本",
                    uri="https://storage.cloud.google.com/pig_house/%E5%90%88%E7%B4%84/%E4%BD%8F%E5%AE%85%E7%A7%9F%E8%B3%83%E5%AE%9A%E5%9E%8B%E5%8C%96%E5%A5%91%E7%B4%84%E7%AF%84%E6%9C%AC%20(1).pdf"
                ),
                MessageTemplateAction(
                    label="上傳合約",
                    text="上傳合約"
                ),
                MessageTemplateAction(
                    label="查看合約",
                    text="查看合約"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='簽約流程旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='步驟1《確認房東身分》',
                    text = '請房東出示『身分證明文件』、『房屋所有權狀』，確保房屋為房東所屬。若對方為二房東，查看是否取得『轉租同意證明』',
                    actions=[
                        URITemplateAction(
                            label='辨別針假房東',
                            uri='https://www.591.com.tw/help-book20.html'
                        ),
                        URITemplateAction(
                            label='查詢房東風評',
                            uri='https://rent-exp.blogspot.com/?fbclid=IwAR3x4DmyMQNlKTD_pHr5VU-UdRGb3WHga1IyFNrkFSfneuJj4NpJEDLFHZQ'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='步驟2《確認合約資訊》',
                    text='《住宅租賃契約應約定及不得約定事項》規定特定條款不得加註於租約，建議和內政部租約範本比對，較能保障自身權益。',
                    actions=[
                        URITemplateAction(
                            label='租賃契約須知',
                            uri='https://www.591.com.tw/help-book13.html'
                       ),
                        URITemplateAction(
                            label='應約定及不得約定事項',
                            uri='https://storage.cloud.google.com/pig_house/%E5%90%88%E7%B4%84/%E4%BD%8F%E5%AE%85%E7%A7%9F%E8%B3%83%E5%AE%9A%E5%9E%8B%E5%8C%96%E5%A5%91%E7%B4%84%E6%87%89%E8%A8%98%E8%BC%89%E5%8F%8A%E4%B8%8D%E5%BE%97%E8%A8%98%E8%BC%89%E4%BA%8B%E9%A0%85.pdf'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='步驟3《完成簽約流程》',
                    text='通常租客需支付兩個月的押金、首月的租金，因此要先準備好三個月的租金。簽字蓋章完成後，雙方要各自保留一份租約',
                    actions=[
                        URITemplateAction(
                            label='訂金、押金、租金',
                            uri='https://news.591.com.tw/news/2098'
                        ),
                        URITemplateAction(
                            label="安全提醒",
                            uri="https://www.591.com.tw/help-book18.html"
                        )
                    ]
                )
            ]
        )
    )
    return message
