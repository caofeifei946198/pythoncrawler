import requests
import time
from bs4 import BeautifulSoup
from http import cookiejar
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename=
                'cookies.txt')
try:
    session.cookies.load(ignore_discard = True)
except:
    print('load cookies failed')
headers = {
'Host':'www.zhihu.com',
'Referer':'https://www.zhihu.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
}
def get_xsrf():
    response = session.get('https://www.zhihu.com', headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    xsrf = soup.find('input', attrs={'name':'_xsrf'}).get
    ('value')
    return xsrf
def get_captcha():
    '''
    把验证码图片保存到当强目录，手动识别验证码
    :return:
    '''
    t = str(int(time.time()*100))
    captcha_url = "https://www.zhihu.com/captcha.gif?r='+t+'&type=login"
    #验证码的连接
    r = session.get(captcha_url, headers = headers)
    with open('captcha.jpg','wb') as f:
        f.write(r.content)
    captcha = input('验证码: ')
    return captcha

def login(email, password):
    login_url = 'https://www.zhihu.com/login/email'
    data = {
        'email':email,
        'password':password,
        '_xsrf':get_xsrf(),
        'captcha':get_captcha(),
        'remember_me':'true'

    }
    response = session.post(login_url, data=data, headers=headers)
    login_code = response.json()
    print(login_code['msg'])
    for i in session.cookies:
        print(i)
    session.cookies.save()
