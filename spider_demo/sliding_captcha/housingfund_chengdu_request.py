# https://www.cdzfgjj.gov.cn:9802/cdnt/login.jsp#per
import execjs  # 依赖 nodejs
import requests
import random
import re
from lxml import etree
import time
import urllib3
urllib3.disable_warnings()

ctx = execjs.compile(''.join(open('./source/chengdu610000_md5.js').readlines()))  # 这个文件

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': '*/*',
    'Host': 'www.cdzfgjj.gov.cn:9802',
    'Origin': 'https://www.cdzfgjj.gov.cn:9802',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest'
}
session = requests.session()
session.headers.update(headers)
session.verify = False
index_page = session.get('https://www.cdzfgjj.gov.cn:9802/cdnt/login.jsp#corp').text
# print(index_page)
html = etree.HTML(index_page)
web_case = re.search('web_case="(.*?)"', index_page).groups()[0]
print(web_case)

# pass_params = [
#     {
#         'x': '991,999,1016,1036,1059,1076,1098,1117,1137,1146,1159,1177,1178,1179,1184,1191,1195,1201,1206,1213,1219,1227,1233,1239,1247,1253,1258,1266,1270,1275,1279,1283,1286,1287,1291,1292,1292,',
#         'y': '404,404,406,406,406,407,407,407,407,407,407,407,407,407,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,406,',
#         't': '1533017836939,1533017836957,1533017836974,1533017836990,1533017837007,1533017837024,1533017837041,1533017837059,1533017837075,1533017837092,1533017837109,1533017837126,1533017837143,1533017837160,1533017837178,1533017837195,1533017837212,1533017837230,1533017837247,1533017837264,1533017837281,1533017837298,1533017837315,1533017837332,1533017837350,1533017837367,1533017837384,1533017837401,1533017837418,1533017837435,1533017837452,1533017837469,1533017837486,1533017837504,1533017837539,1533017837555,1533017837574,'
#     }
# ]

enc_lgyz = ctx.call('strEnc', web_case, "lgyz",str(random.random()))

def get_time_str():
    timestamp = int(str(time.time()).replace('.', '')[:13])
    l = [str(timestamp)]
    for i in range(37):
        timestamp -= random.randint(100, 1000)
        l.append(str(timestamp))
    return ','.join(reversed(l)) + ','

def get_x_str():
    end = 1292
    l = [str(end)]
    for i in range(36):
        end -= random.randint(1, 8)
        l.append(str(end))
    return '991,' + ','.join(reversed(l)) + ','

def get_y_str():
    l = []
    for i in range(37):
        l.append(random.choice(['404', '406', '407']))
    return ','.join(l) + ','

data = {
    "dto['captcha']": 'captcha',
    "dto['referrer']": 'https://www.cdzfgjj.gov.cn:9802/cdnt/login.jsp',
    "dto['move_x']": get_x_str(),
    "dto['move_y']": get_y_str(),
    "dto['time']": get_time_str(),
    "dto['lgyz']": enc_lgyz,
}

print(data)
url_captcha = 'https://www.cdzfgjj.gov.cn:9802/cdnt/infor/queryAction!getToken.do?r='+str(random.random())
response_captcha = session.post(url_captcha, data=data).json()
print(response_captcha)

token = response_captcha['fieldData']['token']

param_login = {
    'j_username': '{"j_username":"6222024402064365293","j_password":"08362200","loginType":5}',
    'j_password': '08362200',
    'token': token,
    'bsr': 'safari/8.0.8'
}
print(param_login)
url_login = 'https://www.cdzfgjj.gov.cn:9802/cdnt/login?r=' + str(random.random())
login_res = session.post(url_login, data=param_login)
print(login_res.text)
print(session.get('https://www.cdzfgjj.gov.cn:9802/cdnt/indexAction.do?_r=0.25783734507843414').text)

