from transitions.extensions import GraphMachine
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction, MessageAction, VideoSendMessage
import random
from utils import send_text_message, send_temp_message
from bug import bug2, bug1, bug3, bug4, bug5, bug6
# a
url_list_for_all = []
# b
text_list = []
# a
title_list = []
# b
url_list = []

video = []

set_url = "https://www.dcard.tw"


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
       
        return text.lower() == "熱門"
        

    def is_going_to_state2(self, event):
        text = event.message.text
        if "甚麼" in text:
            return True
        elif "什麼" in text:
            return True
        else:
            return False
        # return text.lower() == "Dcard有甚麼版"

    def is_going_to_state3(self, event):
        text = event.message.text

        if "版" in text:
            return True
        else:
            return False

    def is_going_to_state4(self, event):
        text = event.message.text
        
        return text.lower() == "功能"
    
    def is_going_to_state5(self, event):
        text = event.message.text
       
        return text.lower() == "最新"
    
    def is_going_to_state6(self, event):
        text = event.message.text
        
        return text.lower() == "搜尋關鍵字"

    def is_going_to_state7(self, event):
        text = event.message.text

        if "搜尋:" in text:
            return True
        else:
            return False
    def is_going_to_state8(self, event):
        text = event.message.text
       
        return text.lower() == "dcard影片"
    def is_going_to_state9(self, event):
        text = event.message.text
       
        return text.lower() == "yes"
    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        title_list = []
        url_list = []
        bug1(title_list, url_list)
        message_t = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png',
                title='熱門文章',
                text='Top 4 articles',
                actions=[
                    URITemplateAction(
                        label=title_list[0],
                        uri=set_url+url_list[0]
                    ),
                    URITemplateAction(
                        label=title_list[1],
                        uri=set_url+url_list[1]
                    ),
                    URITemplateAction(
                        label=title_list[2],
                        uri=set_url+url_list[2]
                    ),
                    URITemplateAction(
                        label=title_list[3],
                        uri=set_url+url_list[3]
                    )
                    
                ]
            )
        )
        send_temp_message(reply_token, message_t)

        self.go_back()
        
    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        temp = ""
        text_list = []
        url_list_for_all = []
        bug2(text_list, url_list_for_all)
        for i in range(len(text_list)):
            if(len(temp) <= 1980):
                temp = temp + text_list[i] + ":" + url_list_for_all[i] + "\n"
        
        reply_token = event.reply_token
        send_text_message(reply_token, temp)
        self.go_back()
        

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")
        title_list = []
        url_list = []
        reply_token = event.reply_token
        text = event.message.text
        find = text.split("版", 1)
        bug3(title_list, url_list, find[0])
        if(len(title_list) != 0):
            message_t = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png',
                    title=find[0] + "版",
                    text='Top 4 articles',
                    actions=[
                        URITemplateAction(
                            label=title_list[0],
                            uri=set_url+url_list[0]
                        ),
                        URITemplateAction(
                            label=title_list[1],
                            uri=set_url+url_list[1]
                        ),
                        URITemplateAction(
                            label=title_list[2],
                            uri=set_url+url_list[2]
                        ),
                        URITemplateAction(
                            label=title_list[3],
                            uri=set_url+url_list[3]
                        )
                        
                    ]
                )
            )
            send_temp_message(reply_token, message_t)   
        else:
            send_text_message(reply_token, "沒有"+find[0]+"這個版(大小寫有差)")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")
        reply_token = event.reply_token
        title_list = []
        url_list = []
        bug1(title_list, url_list)
        message_t = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png',
                title='功能',
                text='choose one',
                actions=[
                    MessageAction(
                    label='熱門文章',
                    text='熱門'
                    ),
                    MessageAction(
                    label='最新文章',
                    text='最新'
                    ),
                    MessageAction(
                    label='搜尋我要的關鍵字',
                    text='搜尋關鍵字'
                    ),
                    MessageAction(
                    label='有什麼',
                    text='有什麼'
                    )
                    
                ]
            )
        )
        send_temp_message(reply_token, message_t)

        self.advance(event)
        
    def on_exit_state4(self, t):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")
        reply_token = event.reply_token
        title_list = []
        url_list = []
        bug4(title_list, url_list)
        message_t = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png',
                title='最新文章',
                text='Top 4 articles',
                actions=[
                    URITemplateAction(
                        label=title_list[0],
                        uri=set_url+url_list[0]
                    ),
                    URITemplateAction(
                        label=title_list[1],
                        uri=set_url+url_list[1]
                    ),
                    URITemplateAction(
                        label=title_list[2],
                        uri=set_url+url_list[2]
                    ),
                    URITemplateAction(
                        label=title_list[3],
                        uri=set_url+url_list[3]
                    )
                    
                ]
            )
        )
        send_temp_message(reply_token, message_t)

        self.go_back()
        
    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state6")

        self.advance(event)
        
    def on_exit_state6(self, t):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state7")
        title_list = []
        url_list = []
        reply_token = event.reply_token
        text = event.message.text
        find = text.split(":", 2)
        print(find)
        bug5(title_list, url_list, find[1])
        if(len(title_list) != 0):
            message_t = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png',
                    title=find[1],
                    text='Top 4 articles',
                    actions=[
                        URITemplateAction(
                            label=title_list[0],
                            uri=set_url+url_list[0]
                        ),
                        URITemplateAction(
                            label=title_list[1],
                            uri=set_url+url_list[1]
                        ),
                        URITemplateAction(
                            label=title_list[2],
                            uri=set_url+url_list[2]
                        ),
                        URITemplateAction(
                            label=title_list[3],
                            uri=set_url+url_list[3]
                        )
                        
                    ]
                )
            )
            send_temp_message(reply_token, message_t)   
        else:
            send_text_message(reply_token, "搜尋不到 " + find[1])
        self.go_back()
        
    def on_exit_state7(self):
        print("Leaving state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")
        reply_token = event.reply_token
        video = []
        final = []
        temp = ""
        bug6(video)
        final = random.sample(video, 5)
        # print(len(final))
        for i in range(len(final)):
            temp = temp + final[i] + "\n"
        
        reply_token = event.reply_token
        send_text_message(reply_token, temp)
        self.go_back()

        
    def on_exit_state8(self):
        print("Leaving state8")

    def on_enter_state9(self, event):
        print("I'm entering state9")
        reply_token = event.reply_token
        message = VideoSendMessage(
            original_content_url='https://i.imgur.com/esj1spp.mp4',
            preview_image_url='https://upload.wikimedia.org/wikipedia/commons/f/f8/Dcard_Favicon_x520.png'
        )
      
        
        reply_token = event.reply_token
        send_temp_message(reply_token, message)
        self.go_back()

        
    def on_exit_state9(self):
        print("Leaving state9")
