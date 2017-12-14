import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('hDEXigBx3q22MD9N4c4k9h/7ql08sBMCUTAuhBAevphGCcbIJb65W0nik3BePY6w68ZBPb9dkjc/s+2znFz26qZrSiOSKCghglNRZJCnQe7NUHi+RGMIExGa0r+A3HGYMAVFZwctBTmuqyTyp2aDAAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bc1445fa31789d24b3cebe96a69b5010')


@app.route("/callback", methods=['POST'])
def callback():
    #get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    #print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'


def pattern_mega(text):
    patterns = [
        'mega','mg', 'mu'
    ]
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True



def digiroin():
    target_url = 'https://www.digiroin.com/forum/login'
    print('launching Digiroin in a second')
    rs = reqests.session()
    res = rs.get(traget_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for titleURL in soup.select('.bm_c tbody .xst'):
        if pattern_mega(titleURL.text):
            title = titleURL.text
            if '11379780-1-1' in titleURL['href']:
                continue
            link = 'http://www.digiroin.com/' + titleURL['href']
            data = '{}\n{}\n\n'.format(title, link)
            content += data
    return content


def apple_news():
    target_url = 'http://www.appledaily.com.tw/realtimenews/section/new'
    head = 'http://www.appledaily.com.tw'
    print('Start opening appleNews....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('.rtddt a'), o):
        if index == 15:
            return content
        if head in data['href']:
            link = data['href']
        else:
            link = head + data['href']
        content += '{}\n\n'.format(link)
    return content

def technews():
    target_url = 'https://technews.tw/'
    print('Start opening Technews...')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.txt, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('article div h1. entry-title a')):
        if index == 12:
            return content
        title = data.text
        link - data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content


def gironews():
    target_url = 'https://www.giro.com/'
    print('Start opening gironews...')
    rs = requests.session()
    res = rs.get(traget_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.txt, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('article div h1. entry-title a')):
        if index == 12:
            return content
        title = data.text
        link - data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text", event.message.text)
    if event.message.text == "Hello":
        confirm_template_message = TemplateSendMessage(
            alt_text='Welcome!',
            template=ConfirmTemplate(
                text='Hey there, Choose what you want to see...',
                actions=[
                    MessageTemplateAction(
                        label='Merchant',
                        text='I want to see available merchant'
                    ),
                    MessageTemplateAction(
                        label='Info',
                        text='Help'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
        return 0
    if event.message.text == "apple_news":
        content = apple_news()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "technews":
        content = technews()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Help":
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://image.freepik.com/free-icon/setting_318-32132.jpg',
                        title='Help',
                        text='Here are the list',
                        actions=[
                            MessageTemplateAction(
                                label='Listed Problem',
                                text='i wanna see the listed problem'
                            ),
                            MessageTemplateAction(
                                label='Apps Crash',
                                text='my apps keep crashing'
                            ),
                            URITemplateAction(
                                label='Others',
                                uri='https://digiro.in/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://t4.ftcdn.net/jpg/01/82/58/55/240_F_182585589_bZubTDLlgFKpv07XyXtW00HFTqH8SCnu.jpg',
                        title='Merchant',
                        text='Here are the listed merchant',
                        actions=[
                            MessageTemplateAction(
                                label='Fast food',
                                text='i want fastfood'
                            ),
                            MessageTemplateAction(
                                label='Dinner Menu',
                                text='i want dinner'
                            ),
                            URITemplateAction(
                                label='See more',
                                uri='https://digiro.in'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://thumbs.dreamstime.com/b/boy-girl-icon-6447384.jpg',
                        title='Biro Jodoh',
                        text='Hayoloo Jomblo Looo',
                        actions=[
                            MessageTemplateAction(
                                label='Cari Pacar Laki',
                                text='Saya Mencari Pasangan Lelaki'
                            ),
                            MessageTemplateAction(
                                label='Cari Pacar Perempuan',
                                text='Saya Mencari Pasangan Perempuan'
                            ),
                            URITemplateAction(
                                label='Saya Mencari Boneng',
                                uri='https://digiro.in/'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
        return 0
    if event.message.text == "Giro":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.ytimg.com/vi/opKg3fyqWt4/hqdefault.jpg',
                title='Menu',
                text='Please select'
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='message text'
                    ),
                    URITemplateAction(
                        label='uri',
                        uri='http://google.com/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        return 0
    if event.message.text == "I want to see available merchant":
        carousel_template_message = TemplateSendMessage(
            alt_text='Merchant List',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://image.freepik.com/free-icon/setting_318-32132.jpg',
                        title='Merchant Danang',
                        text='Bayar jika membeli',
                        actions=[
                            MessageTemplateAction(
                                label='Promo',
                                text='mana promonya?'
                            ),
                            MessageTemplateAction(
                                label='Meet Danang',
                                text='my apps keep crashing'
                            ),
                            URITemplateAction(
                                label='Others',
                                uri='https://digiro.in/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://t4.ftcdn.net/jpg/01/82/58/55/240_F_182585589_bZubTDLlgFKpv07XyXtW00HFTqH8SCnu.jpg',
                        title='Merchant',
                        text='Here are the listed merchant',
                        actions=[
                            MessageTemplateAction(
                                label='Fast food',
                                text='i want fastfood'
                            ),
                            MessageTemplateAction(
                                label='Restaurant',
                                text='i want dinner'
                            ),
                            URITemplateAction(
                                label='See more',
                                uri='https://digiro.in'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://thumbs.dreamstime.com/b/boy-girl-icon-6447384.jpg',
                        title='Biro Jodoh',
                        text='Hayoloo Jomblo Looo',
                        actions=[
                            MessageTemplateAction(
                                label='Cari Pacar Laki',
                                text='Saya Mencari Pasangan Lelaki'
                            ),
                            MessageTemplateAction(
                                label='Cari Pacar Perempuan',
                                text='Saya Mencari Pasangan Perempuan'
                            ),
                            URITemplateAction(
                                label='Saya Mencari Boneng',
                                uri='https://digiro.in/'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
        return 0


if __name__ == '__main__':
    app.run(debug = True, port = 80)