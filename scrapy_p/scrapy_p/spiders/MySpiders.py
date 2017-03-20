import scrapy
from scrapy.crawler import CrawlerProcess

from scrapy_p.items import BlogItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'  # 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字
    allowed_domains = ['dmoz.org']
    start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
                  "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]  # 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取

    # 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 该方法负责解析返回的数据(response data)，
    # 提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self, response):  # Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法
        filename = response.url.split('/')[-2]
        self.log(filename)
        yield filename

        for url in response.xpath('*//a/@href').extract():
            self.log(url)
            yield scrapy.Request(url, callback=self.parse)

            # with open(filename, 'wb') as f:
            #     f.write(response.url.encode('utf-8'))
            #     f.write(response.body)

            # for sel in response.xpath('//ul/li'):
            #     title = sel.xpath('a/text()').extract()
            #     link = sel.xpath('a/@href').extract()
            #     desc = sel.xpath('text()').extract()
            #     item = DmozItem()
            #     item['title'] = title
            #     item['link'] = link
            #     item['desc'] = desc
            #     yield item


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/luoshengyang']

    def parse(self, response):
        file_name = response.xpath('//div[@id="blog_title"]/h2/a/text()').extract()[0]
        print(file_name)
        titles = response.xpath('//div[@id="article_list"]//span[@class="link_title"]//a/text()').extract()
        descs = response.xpath('//div[@id="article_list"]//div[@class="article_description"]/text()').extract()
        links = response.xpath('//div[@id="article_list"]//span[@class="link_title"]//a/@href').extract()
        # title2 = []
        # desc2 = []
        # link2 = []
        # for tt in titles:
        #     title2.append(tt.strip())
        # for dd in descs:
        #     desc2.append(dd.strip())
        # for ll in links:
        #     link2.append(ll.strip())
        # with open(file_name.strip(), 'wb') as f:
        #     f.write(file_name.encode('utf-8'))
        #     f.write('\t\n'.encode('utf-8'))
        #     f.write(str(title2).encode('utf-8'))
        #     f.write('\t\n'.encode('utf-8'))
        #     f.write(str(desc2).encode('utf-8'))
        #     f.write('\t\n'.encode('utf-8'))
        #     f.write(str(link2).encode('utf-8'))

        for title, desc, link in zip(titles, descs, links):
            item = BlogItem()
            item['title'] = title.strip()
            item['link'] = response.urljoin(link.strip())
            item['desc'] = desc.strip()
            # self.log('item', item)
            self.logger.info('item', item)
            yield item
        next_page = response.urljoin(response.xpath('//*[@id="papelist"]/a[text()="下一页"]/@href').extract()[0])
        print(next_page)
        yield scrapy.Request(next_page, callback=self.parse)


process = CrawlerProcess()
process.crawl(DmozSpider)
process.crawl(BlogSpider)
process.start()