import requests
from lxml import html, etree
response = requests.get('http://pycoders.com/archive/')
tree = html.fromstring(response.text)
# etree.HTML(response.text)

print(tree.xpath('//div[@class="campaign"]/a/@href'))

