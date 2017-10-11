import os
import requests
import re
import time#获取日期
import pandas as pd
from bs4 import BeautifulSoup

url = "http://www.p2peye.com/shuju/ptsj/"
start = time.clock()
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Host':'www.p2peye.com',
'Upgrade-Insecure-Requests':'1'
}
r = requests.get(url, headers=headers)



html = r.content
html = str(html, encoding="GBK")#对抓取的页面进行编码


title = re.findall(r'"return false".*?title="(.*?)"',html)
total = re.findall(r'"total">(.*?)万<',html)
rate = re.findall(r'"rate">(.*?)<',html)
pnum = re.findall(r'"pnum">(.*?)人<',html)
cycle = re.findall(r'"cycle">(.*?)月<',html)
p1num = re.findall(r'"p1num">(.*?)人<',html)
fuload = re.findall(r'"fuload">(.*?)分钟<',html)
alltotal = re.findall(r'"alltotal">(.*?)万<',html)
capital = re.findall(r'"capital">(.*?)万<',html)
    #strftime表示将时间转换成字符串，获取当天的时间
date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    #创建贷款及理财数据表
    #设置数据表各字段顺序
columns = ['采集日期','平台名称','成交额(万)','综合利率',
       '投资人(人)','借款周期(月)','借款人(人)',
       '满标速度(分钟)','累计贷款金额(万)','净资金流入(万)']
#创建数据表
table = pd.DataFrame({'采集日期':date,
                  '平台名称':title,
                  '成交额(万)':total,
                   '综合利率' :rate,
                  '投资人(人)':pnum,

                  '借款周期(月)':cycle,
                  '借款人(人)':p1num,
                  '满标速度(分钟)':fuload,
                  '累计贷款金额(万)':alltotal,
                  '净资金流入(万)':capital},
                 columns=columns
)
    # table.to_csv('/home/feier/python3/python爬虫/贷款数据' + date + 'csv', index=False)
# table.to_csv('贷款数据.csv', index=False, mode='a')
# # print('累计数据追加导出完毕')
        # print(date + '日数据导出完毕')


#查看数据表
print(table)
#导出csv文件
table.to_csv('/home/feier/python3/python爬虫/贷款数据'+date+'csv',index=False)
        # print(date+'日数据导出完毕')
    #在历史csv文件中追加新信息
table.to_csv('贷款数据.csv', index=False,mode='a')
        # print('累计数据追加导出完毕')
