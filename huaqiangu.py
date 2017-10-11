from urllib import request
from bs4 import BeautifulSoup
import json

if __name__=="__main__":

    url ="http://www.136book.com/piaoyangguohailaikanni/"

    head = {
        "User - Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"
    }
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, "lxml")
    soup.texts = soup.find('div', id = 'book_detail', class_ = 'box1').find_next('div')
    #a = soup.select('a')[0]['href']
    #print(a)

    for link in soup.texts.ol.children:
        if link != '':
            download_url = link.a.get('href')
            download_req = request.Request(download_url, headers=head)
            download_response = request.urlopen(download_req)
            download_html = download_response.read()
            download_soup = BeautifulSoup(download_html,'lxml')
            download_soup.texts = download_soup.find('div', id= 'content')
            #抓取其中的文本
            download_soup_texts = download_soup_texts.text
            with open('/home/feier/python3/python爬虫', 'w') as f:
                f.write(link.text+'')#写入章节标题
                f.write(download_soup_texts)#写入章节内容
                f.write('')
        f.close()


#爬取每个连接对用的文本
# if __name__=="__main__":
#     url ="http://www.136book.com/yemanwangfeiduwangnansihou/edqltv/"
#     head = {
#         "User - Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"
#     }
#     req = request.Request(url,headers=head)
#     response = request.urlopen(req)
#     html = response.read()
#
#     soup = BeautifulSoup(html,'html.parser')
#
#     soup_text = soup.find('div', id='content')
#
#     print(soup_text.text)



