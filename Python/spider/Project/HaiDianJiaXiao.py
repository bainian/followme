import random

import requests
from lxml import etree

yyrq_date = '20170316'
yctime = ['2002', '2003']  # 字符串 早 2001, 中 2002, 晚 2003

login_url = 'http://haijia.bjxueche.net/'
view_state = '__VIEWSTATE'
my_data = {
    'txtUserName': '51382219930508482X',
    'txtPassword': '5103041075',
    'BtnLogin': '登  录'
}
my_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'haijia.bjxueche.net',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

s = requests.Session()
res = s.get(url=login_url)
# print(type(res.text))
# print(type(res.content))
content = etree.HTML(res.content)
var1 = content.xpath('//input[@name="__VIEWSTATE"]/@value')
var2 = content.xpath('//input[@name="__VIEWSTATEGENERATOR"]/@value')
var3 = content.xpath('//input[@name="__EVENTVALIDATION"]/@value')
# print('var1 = ', var1)
# print('var2 = ', var2)
# print('var3 = ', var3)
my_data['__EVENTVALIDATION'] = var3
my_data['__VIEWSTATE'] = var1
my_data['__VIEWSTATEGENERATOR'] = var2
# print(res.text)
code_url = login_url + 'tools/CreateCode.ashx?key=ImgCode&random=' + str(random.random())
code_res = s.get(code_url)
with open('code.jpg', 'wb') as f:
    f.write(code_res.content)
    f.close()
# print('code_url:', code_url)
yanzheng_code = input('查看当前目录下图片code.jpg，并输入四位验证码：')
my_data['txtIMGCode'] = yanzheng_code

# ycdate = input('输入约车日期（20170317）:')
# yctime = input('输入约车时间段：早=1，中=2, 晚=3')
# if yctime == '1':
#     yctime = '2001'
# elif yctime == '2':
#     yctime = '2002'
# elif yctime == '3':
#     yctime = '2003'
# else:
#     print('input error')
#
#


response = s.post(login_url, data=my_data, headers=my_header)
print('登陆结果：', response.status_code)

re_url = 'http://haijia.bjxueche.net/ych2.aspx'
# 这里需要用到phantomjs与selenium配合js抓取
data1 = s.get(re_url)
print('主页结果：', data1.status_code)
# print(data1.text)
# ych = etree.HTML(data1.content)

getcars_js_req_url = 'http://haijia.bjxueche.net/Han/ServiceBooking.asmx/GetCars'
getcars_data = {
    'pageNum': 1,
    'pageSize': 35,
    'xllxID': '2'
}

# 查询某天某时段内的车有没有可约的，大于0
def makeRequest(data):
    print('查询 %s - %s ' % (data['yyrq'], data['yysd']))
    res = s.post(getcars_js_req_url, data=data)

    pass


for date in yyrq_date:
    for time in yctime:
        getcars_data['yyrq'] = date
        getcars_data['yysd'] = time
        makeRequest(getcars_data)
        pass
