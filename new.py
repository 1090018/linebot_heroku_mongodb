#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot.models import *

def test():
    message = TemplateSendMessage(
        alt_text='常見問題一覽',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://storage.cloud.google.com/pig_house/%E5%B8%B8%E8%A6%8B%E5%95%8F%E9%A1%8C%E5%9C%96%E7%89%87/1.png",
                    action=MessageTemplateAction(
                        label="簽約流程一覽",
                        text="簽約流程一覽"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://storage.cloud.google.com/pig_house/%E5%B8%B8%E8%A6%8B%E5%95%8F%E9%A1%8C%E5%9C%96%E7%89%87/2.png",
                    action=MessageTemplateAction(
                        label="常見租屋陷阱",
                        text="常見租屋陷阱"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://storage.cloud.google.com/pig_house/%E5%B8%B8%E8%A6%8B%E5%95%8F%E9%A1%8C%E5%9C%96%E7%89%87/4.png",
                    action=MessageTemplateAction(
                        label="看房注意事項",
                        text="看房注意事項"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://storage.cloud.google.com/pig_house/%E5%B8%B8%E8%A6%8B%E5%95%8F%E9%A1%8C%E5%9C%96%E7%89%87/3.png",
                    action=MessageTemplateAction(
                        label="簽約注意事項",
                        text="簽約注意事項"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://storage.cloud.google.com/pig_house/%E5%B8%B8%E8%A6%8B%E5%95%8F%E9%A1%8C%E5%9C%96%E7%89%87/5.png",
                    action=MessageTemplateAction(
                        label="退租注意事項",
                        text="退租注意事項"      
                    )
                )
            ]
        )
    )
    return message
