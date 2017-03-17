import scrapy


# Spider是用户编写用于从单个网站(或者一些网站)爬取数据的类。其包含了一个用于下载的初始URL，
# 如何跟进网页中的链接以及如何分析页面中的内容， 提取生成 item 的方法
class DmozSpider(scrapy.Spider):
    name = 'dmoz'  # 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字
    allowed_domains = ['dmoz.org']
    start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
                  "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]  # 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取

    # 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 该方法负责解析返回的数据(response data)，
    # 提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self, response):  # Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.url.encode('utf-8'))
            f.write(response.body)

        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            item = DmozItem()
            item['title'] = title
            item['link'] = link
            item['desc'] = desc
            yield item
