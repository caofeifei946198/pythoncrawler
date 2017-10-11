import os
import csv
import requests
from bs4 import BeautifulSoup
'''
fork函数产生一个子进程
fork函数很特殊，普通的函数调用一次，返回一次，但是fork调用一次，返回两次
'''
ret = os.fork()
#子进程返回０
if ret == 0:
    print('ret =', ret)
    #getpid()得到当前进程的pid
    print('subprocess pid is', os.getpid())
    #getpid()得到父进程的pid
    print('subprocess know parent pid is', os.getppid())
    #父进程返回子进程的pid,返回的不时０，所以父进程执行else语句
else:
    print('ret =', ret)
    print('parent pid is', os.getpid())
url1 = 'http://zhouww.com/'
url2 = 'http://zhouww.com/page/2/'
result = []
def get_info_from(url):
    #result = []#保存结果
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
    }
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'
    content = web_data.text
    soup = BeautifulSoup(content, 'lxml')
    include_title_url_tags = soup.select('a.post-title-link')
    for tag in include_title_url_tags:
        #组成一个结构化的数据
        data = {
            'url':'http://zhouww.com/' + tag.get('href'),
            'title':'tag.text'
        }
        result.append(data)
        return result

def export_to_csv(result):
    with open('./duohappy.csv','a', newline='', encoding='utf-8') as f:
        field_names = ['url', 'title']
        writer = csv.DictWriter(f, field_names)
        #开始写数据
        for data in result:
            writer.writerow(data)
            ret = os.fork()
            if ret == 0:#子进程执行
                export_to_csv(get_info_from(url1))
            else:
                #父进程执行
                export_to_csv(get_info_from(url2))

def main():
    url1 = 'http://zhouww.com/'
    url2 = 'http://zhouww.com/page/2/'
    get_info_from(url1)
    export_to_csv(result)

if __name__ == '__main__':
     main()





# import csv
# from multiprocessing import Pool
# import requests
# from bs4 import BeautifulSoup
# def