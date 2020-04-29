#那年今日
import requests
import lxml.html
import datetime

from Ann_date_sql import *

# today_str=str(datetime.now().date())
def get_url(html_url,encode):
    """
    爬取整个网页内容
    :param html_url:
    :return:
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    response = requests.get(html_url, headers=headers)
    response.encoding = encode
    html_content = response.text
    return html_content

def get_data(html_content,today_str):
    
    metree = lxml.html.etree

    parser = metree.HTML(html_content)

    thing_list= parser.xpath("//ul[@class='oh']/li/div[@class='pic']/div[@class='t']")

    for i in thing_list:
        year_date=i.xpath("./span/text()")[0]
        info=i.xpath("./a/text()")[0]
        url=i.xpath("./a/@href")[0]
        #插入数据库
        thing_insertData(today_str,year_date,info,url)
    print('ok')
    
def year_today_main(today_str):
    today=today_str.split('-')
    html_url='http://www.todayonhistory.com/%s/%s/'%(today[0],today[1])
    get_data(get_url(html_url,'utf-8'),today_str)