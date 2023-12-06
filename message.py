#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message_law():
    message = TemplateSendMessage(
        alt_text='法律',
        template=ButtonsTemplate(
            title="您有法律相關疑問嗎?",
            text="以下是我們提供的法律服務：",
            actions=[
                MessageTemplateAction(
                    label="法律懶人包",
                    text="查看懶人包"
                ),
                MessageTemplateAction(
                    label="法律諮詢管道",
                    text="查看有什麼管道"
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

#TemplateSendMessa否，重新篩選",
                    text="@我要找房"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template1():
    message = TemplateSendMessage(
        alt_text='簽約流程旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='步驟1《確認房東身分》',
                    text = '請房東出示『身分證明文件』、『房屋所有權狀』，確保房屋為房東所屬。若對方為二房東，查看是否取得『轉租同意證明』',  #不得超過60字
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

def Carousel_Template2():
    message = TemplateSendMessage(
        alt_text='租屋陷阱旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='陷阱1《租屋網刊登『照騙』》',
                    text = '房東或業者刻意利用修圖軟體製造屋內空間明亮、寬敞的錯覺。',  #不得超過60字
                    actions=[
                        MessageTemplateAction(
                            label="👉破解陷阱1",
                            text="破解陷阱1"
                        ),
                    ]
                ),
                CarouselColumn(
                    title='陷阱2《假房東》',
                    text='在租屋網刊登假房源，誘騙租客上門，後謊稱不便看房，並以物件搶手為由，要求先行支付定金後便「人間蒸發」。',
                    actions=[
                        MessageTemplateAction(
                            label="👉破解陷阱2",
                            text="破解陷阱2"
                        ),
                    ]
                ),
                 CarouselColumn(
                    title='陷阱3《非法二房東》',
                    text='二房東在未經屋主同意下擅自修改格局並出租，若東窗事發，租客有可能被真正的房東要求搬離租屋處。',
                    actions=[
                        MessageTemplateAction(
                            label="👉破解陷阱3",
                            text="破解陷阱3"
                        ),
                    ]
                ),
                 CarouselColumn(
                    title='陷阱4《要求高額訂金或押金》',
                    text='租屋押金明定不得超過二個月的租金總額。若房東巧立名目收取較高的金額，即為違法，應予以拒絕。',
                    actions=[
                        MessageTemplateAction(
                            label="👉破解陷阱4",
                            text="破解陷阱4"
                        ),
                    ]
                ),
                 CarouselColumn(
                    title='陷阱5《帶看A屋，出租B屋》',
                    text='部分不肖房東會在網路以條件較好的A物件招攬租客，卻在帶看甚至是簽約後，藉故要求改租條件較差的B物件。',
                    actions=[
                        MessageTemplateAction(
                            label="👉破解陷阱5",
                            text="破解陷阱5"
                        ),
                    ]
                ),
                CarouselColumn(
                    title='陷阱6《有問題一概不負責》',
                    text='某些房東遇到房屋漏水、設備損壞時，會百般推託不願修繕，甚至在簽約時要求房客自負修繕責任。',
                    actions=[
                        MessageTemplateAction(
                            label="👉破解陷阱6",
                            text="破解陷阱6"
                        )
                    ]
                )
            ]
        )
    )
    return message
