import requests
from requests.exceptions import RequestException
import json
import re
#from day31.config import *
import pymongo

MONGO_URL=('localhost')
MONGO_DB_PORT = 27017
MONGO_DB='meituan'
MONGO_TABLE='meituan'
# SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
# KEYWORD = 'python'

client=pymongo.MongoClient(MONGO_URL)#与数据库建立连接
db=client['MONGO_DB']#获得数据库MONGO_DB
#print(db)
base_url='http://comment.mobilem.360.cn/comment/getComments?callback=jQuery17209056727722758744_1502991196139&baike=%E7%BE%8E%E5%9B%A2%E5%A4%96%E5%8D%96+Android_com.sankuai.meituan.takeoutnew&start='

def the_url(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None

def the_total():
    html=the_url(base_url)
    pattern1 = re.compile('"total":(.*?),"messages"', re.S)
    Total = re.findall(pattern1, html)
    Total=int(':'.join(Total))
    #print(type(Total))
    show='总计评论%d条'%Total
    print(show)
    write_to_file(show)
    return Total

def parse_one_page(html):
    pattern = '\"content\":\".*?"'
    items=re.findall(pattern,html)
    for item in items:
        item =eval(item.split(':',1)[1])
        write_to_file(item)
        print(item)
        save_to_mongo(item)



def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('储存到MongoDB成功',result)
    except Exception:
        print('储存到MongoDB失败',result)

def write_to_file(content):
    with open('meituan_result.text','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main():
    Total=the_total()
    Total=int(Total/10)+2
    for i in range(Total):
        url = base_url + str(i*10)
        if the_url(url)!=None:
            html=the_url(url)
            parse_one_page(html)
        else:
            print('输完啦')

if __name__ == '__main__':
    main()