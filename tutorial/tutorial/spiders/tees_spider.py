import time
from datetime import date

import scrapy 
from tutorial.items import TeesItem

class TeesSpider(scrapy.Spider):
  name = "tees"
  allowed_domains = ["qwertee.com"]
  start_urls = [
    "http://www.qwertee.com/rss"
  ]

  def parse(self,response):
    today = date.today()
    today = today.replace(day=today.day - 1)
    for i in response.xpath('//item[pubDate="'+today.strftime("%a, %d %b %Y")+' 23:00:00 +0000"]'):
      item = TeesItem()
      item['title'] = i.xpath('description/text()').extract()
      item['link'] = i.xpath('guid/text()').extract()
      item['desc'] = i.xpath('pubDate/text()').extract()
      yield item
    """
    filename = response.url.split("/")[-2] + ".html"
    with open(filename,'wb') as f:
    f.write(response.body)
    """
