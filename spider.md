### urlib和requests简单获取

* 用urllib2
''' python
from urllib import request

with request.urlopen("http://coding.net") as url:
    s = url.read()
'''

* 更新所有库
pip list --outdated | grep '^[a-z]* (' | cut -d " " -f 1 | xargs pip install -U 

* requests库的使用
** get
‘‘‘ python
url = "http://blog.csdn.net/stonecao"
params = {'viewmode': 'contents'}
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__gads=ID=a1aff84dfd7ff4af:T=1447863203:S=ALNI_MbSjb94oUxpPlcmPrL8Y2-JReWOJg; __qca=P0-1717168395-1447863203653; uuid_tt_dd=861692581579214174_20151119; bdshare_firstime=1447935989549; __utma=17226283.1021534213.1447863201.1448720019.1448720019.1; _ga=GA1.2.1021534213.1447863201; lzstat_uv=16826650832307193950|3602465@3411160@3311294@3497199@2737459@3429585@3550616@3517495@2955225@3607338@3573258@3584961@3590372; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1486257923; UN=bainian18; UE="fnz2010@163.com"; BT=1486999858888; __message_district_code=000000; uuid=33724675-b74e-448c-9913-35df8fdcfae5; ViewMode=contents; dc_tos=ommrsw; dc_session_id=1489202240856; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0',
    'Host': 'blog.csdn.net',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
}
req = requests.get(url, params=params, headers=header)
print(type(req))
print('header:', req.headers)
print(req.status_code)
print(req.encoding)
print('cookies:', req.cookies)
print('content:', req.text)

’’’

** post
''' python
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

#有时候我们需要传送的信息不是表单形式的，需要我们传JSON格式的数据过去，所以我们可以用 json.dumps() 方法把表单数据序列化。

import json
import requests
 
url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text

#如果想要上传文件，那么直接用 file 参数即可
url = 'http://httpbin.org/post'
files = {'file': open('test.txt', 'rb')}
r = requests.post(url, files=files)
print(r.text)

#requests 是支持流式上传的，这允许你发送大的数据流或文件而无需先把它们读入内存。要使用流式上传，仅需为你的请求体提供一个类文件对象即可

with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)
'''

** cookies
''' python
#添加 cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
'''

** 会话

‘‘‘ python
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

import requests

s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)

#通过 s.headers.update 方法设置了 headers 的变量。然后我们又在请求中设置了一个 headers，那么会出现什么结果？很简单，两个变量都传送过去了。

{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.9.1", 
    "X-Test": "true", 
    "X-Test2": "true"
  }
}

’’’

** 证书

‘‘‘ python
 #查验证书是否有效
r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
print(r.text)
#想跳过刚才 12306 的证书验证，把 verify 设置为 False 即可
’’’

** 代理

‘‘‘ python
import requests

proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text

#也可以通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理

export HTTP_PROXY="http://10.10.1.10:3128"
export HTTPS_PROXY="http://10.10.1.10:1080"
’’’

### phantomjs用法

### Xpath用法 

