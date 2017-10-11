from time import ctime#用来获取本地时间
from bs4 import BeautifulSoup#HTML解析器
#import itchat#威信API接口
import requests#抓取URL内容
from pandas import Series#一组数组对象，用来处理抓取到的内同
import json
#itchat.login()
Help = '''
友情提示:
请输入景点拼音获取景点信息
注意：
陕西－－请输入shaanxi
吉林市－－请输入jilinshi
抚州－－请输入jiangxifuzhou
'''
#itchat.send(Help, toUserName="filehelper")
#注册消息响应事件

def getTOUR(pinyin):

    try:
        url = "https://lvyou.baidu.com/xiamen"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        name = soup.select('.title')[0].text
        grade = soup.select('.main-score')[0].text
        describe = soup.select('.main-desc-p')[0].text
        season = soup.select('.main-besttime')[0].text
        advice = soup.select('.main-dcnt')[0].text
        #main_out = soup.select('.main-out')[0].text
        output=name+'\n'+grade+'\n'+describe+'\n'+advice+'*'*25+u'\n推荐: '
    except NameError:
        output = '''未知景点信息，请检查是否正确输入景点拼音"
        注意：
        陕西－－请输入shaanxi
        吉林市－－请输入jilinshi
        抚州－－请输入jiangxifuzhou
        '''
    return output
    try:
        season = soup.find('span', {'class': 'main-besttime'}).text
    except ArithmeticError:
        senson = ' '
    try:
        advice = soup.find('span', {'class': 'main-dcnt'}).text
    except ArithmeticError:
        advice = ' '
    arr = []
    try:
        sites = soup.find_all('div', {'class': 'scene-info'})
        if sites == []:
            sites = soup.find_all('li', {'class': 'hot-scene'})
        for site in sites:
            try:
                a = site.find('a', {'class': 'sname'}).text
                arr.append(a)
            except ArithmeticError:
                a = site.find('a', {'class': 'sname'}).text
                arr.append(a)

    except SyntaxError:
        output2 = "无推荐"

    for i in range(0, j):
        output2 = output2 + '\n' + arr[i]
    output = output + '*' * 25 + u'\n推荐: ' + '\n' + output2

itchat.msg_register(itchat.content.TEXT)
def getcity(msg):#创建函数用来存储pinyin并通过pinyin获得景点信息

    pinyin = msg['Text']
    results = getTOUR(pinyin)

    itchat.send(results, msg['FromUserName'])






if __name__=="__main__":

    getTOUR('xiamen')
    getcity('msg')
    itchat.run()