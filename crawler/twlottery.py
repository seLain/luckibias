import requests
import re
from bs4 import BeautifulSoup

res  = requests.get('http://www.taiwanlottery.com.tw/index_new.aspx')
soup = BeautifulSoup(res.text,'html.parser')

'''開獎日期 期數'''
date    = []#Announced date
periods = [] #Number of periods
for span in soup.select('span'):
    match = re.search(r'^<span class="font_black15">(.*?)\s(.*?)</span>',str(span))
    if match:
        date.append(match.group(1))
        periods.append(match.group(2))

'''special_ball 特別號'''
special_ball = []
for div in soup.select('div'):
    match = re.search(r'^<div class="ball_red">(.*?)<',str(div))
    if match:
        special_ball.append(match.group(1))


def big_lottery():
    big_lottery__order  = []
    big_lottery__sorted = []
    counter = 0
    for div in soup.select('div'):
        match = re.search(r'^<div class="ball_tx ball_yellow">(.*?)<',str(div))
        if match:
            counter += 1
            if 21 <= counter <= 26:
                big_lottery__order.append(match.group(1))
            elif 27 <= counter <= 32:
                big_lottery__sorted.append(match.group(1))

    print("******************大樂透******************")
    print("******************49樂合彩****************")
    print(date[3],periods[3])
    print('*******開獎順序*******',''.join(big_lottery__order))
    print('*******大小排序*******',''.join(big_lottery__sorted))
    print('*******特別號碼*******',int(special_ball[2]))
    print("******************************************")

big_lottery()