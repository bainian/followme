pyspider useage:

use phantomJS:
pyspider phantomjs
Web server running on port 25555
add parameter fetch_type='js' to self.crawl
proxy: username:password@hostname:port, Handler.crawl_config can be used with proxy to set a proxy for whole project.

use pyquery:
在pyspider的doc对象中包装了pyquery对象
selector的使用参见http://www.w3school.com.cn/cssref/css_selectors.asp
attr规则：有则取，有则改，没有则添加 ，重复就替换（三种 写法）
''' python
txt = '<p id="hello" class="hello">text haja</p>'

p = pq(txt)('p')
print(p.attr('id'))
print(p.attr('id', 'pop'))
print(p.attr('id', 'hello2'))
p.attr.id = 'ppp'
print(p.attr('id'))
print(p)
p.attr['class'] = 'change'
print(p)
p.attr(id_='hhh', class_='cccc')
print(p)
p.attr['id'] = None
p.attr(id_ = "None")
print(p)
'''




















