import requests, string
from lxml import etree
import multiprocessing

headers = {'Host': 'www.kekenet.com',
           'Origin': 'http://www.kekenet.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
           'Referer': 'http://www.kekenet.com/read/news/List_1298.shtml',
           'Upgrade-Insecure-Requests': 1,
           'Cookie': 'keke_read_news_pagetotal=1295; pgv_pvid=7636489960; Hm_lvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237358; Hm_lpvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237845; CNZZDATA1037071=cnzz_eid%3D2135797081-1471233399-%26ntime%3D1471233399'
           }


def make_url_list(i):
    com_single_url = 'http://www.kekenet.com/read/news/List_%s.shtml' % i
    return com_single_url


def get_link_page(base_url):
    wb_data = requests.get(base_url, headers=headers)
    html = str(wb_data.content, 'utf-8', errors='ignore')
    new_html = etree.HTML(html)
    xpath = new_html.xpath('//*[@id="menu-list"]/li/h2/a[2]/@href')
    return xpath


def get_content(single_url):
    wb_data = requests.get(single_url, headers=headers)
    html = str(wb_data.content, 'utf-8', errors='ignore')
    new_html = etree.HTML(html)
    header = new_html.xpath('//*[@id="nrtitle"]')
    result = new_html.xpath('//*[@id="article_eng"]/div/div/p')
    if header:
        print(header[0].text)
        exclude = set(string.punctuation)
        file_name = ''.join(ch for ch in header[0].text if ch not in exclude)
        print(file_name)
        with open(file_name, 'w', encoding='utf-8', errors='ignore') as f:
            for every_graph in result:
                if every_graph.text:
                    graph = every_graph.text
                    f.write(graph)
                    f.write('\n')


if __name__ == "__main__":
    url_list = list(map(make_url_list, [i for i in range(1000, 1204)]))
    print('url_list = ',url_list)
    every_url_list = list(map(get_link_page, url_list))
    new_url_list = []
    for i in every_url_list:
        new_url_list.extend(i)
    pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=pool_size)
    pool.map_async(get_content, new_url_list)
    pool.close()
    pool.join()
