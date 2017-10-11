import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re
# res = requests.get("http://news.sina.com.cn/china/")
# res.encoding = "utf-8"
# #print(res.text)
# soup = BeautifulSoup(res.text, "html.parser")

# for news in soup.select(".news-item"):#news-item时个类，前面加上.
#     if len(news.select("h2")) > 0:#进行遍历
#         h2 = news.select("h2")[0].text#抓取新闻标题
#         time = news.select(".time")[0].text#炸取新闻时间
#         a = news.select("a")[0]["href"]#抓取新闻连接
#         print(time,h2, a)#取得文字内容
# comments = requests.get("http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fymesii5759330&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&")
# comments.encoding = "utf-8"
# #print(comments.text)
# jd = json.loads(comments.text.strip("var data="))
# print(jd['result']['count']['total'])新闻屏临数存放在result下的count下的total中
# newsurl = "http://news.sina.com.cn/c/gat/2017-09-26/doc-ifymesii5759330.shtml"
# newsid = newsurl.split("/")[-1].lstrip("doc-i").rstrip(".shtml")#使用split隔开
# # print(newsid)

#soup = BeautifulSoup(res.text, "html.parser")
# title = soup.select("#artibodyTitle")[0].text#artibodyTitle为id,前面加#
# timesource = soup.select(".time-source")[0].contents[0].strip()
# dt = datetime.strptime(timesource, "%Y年%m月%d日%H:%M")#将字串转换为时间
# mediansource = soup.select(".time-source span a")[0].text
#
# #dt = datetime.strptime(timesource,"%Y年%m月%d日%H:%M")
# print(title,timesource,mediansource)
# article = []
# for p in soup.select("#artibody p")[:-1]:
#     article.append(p.text.strip())#用strip去掉空格部分
# print(article)
#"＆".join(article)#将每段文字连接起来
# editor = soup.select(".article-editor")[0].text
# print(editor)
# commentCounts = soup.select("#commentCount1")[0].text
# print(ommentCounts)
# commentURL = "http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fymesii5759330&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&"
# commentURL.format(newsid)
#res = requests.get("http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=2&callback=newsloadercallback&_=1506560557667")
#如果时非同布的载入一般存放在XHR中，但页可能存放在JS中，评论数存放在JS中
# jd = json.loads(res.text.lstrip(' newsloadercallback(').rstrip(');'))#转换为json格式
# for ent in jd['result']['data']:#产生每页新闻连接
#
#     print(ent['url'])#内容存放在result下的data中
#使用for循环产生多页连接
news_total = []#存放抓取的连接
url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}"
for i in range(1,30):
    print(url.format(i))
