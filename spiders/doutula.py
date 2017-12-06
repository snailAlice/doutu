#-*- coding : utf-8 -*-
import os
import scrapy
import requests
from ..items import DoutuItem

class Doutu(scrapy.Spider):
    name = 'doutu'
    #allowed_domains = ["doutula.com","*.sinaimg.cn"]
    start_urls = ['https://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1,10)]


    def parse(self, response):
        i = 0
        for content in response.xpath('//*[@id="pic-detail"]/div/div[1]/div[2]/ul/li/div/div/a'):

            i += 1
            item = DoutuItem()
            print (content)
            item['img_url'] = 'http:'+ content.xpath('//img/@data-original').extract()[i]
            item['name'] = content.xpath('//p/text()').extract()[i].encode("utf-8")
            try:
                if not os.path.exists('/Users/wangxiangyang/PycharmProjects/pywork/doutu/doutu'):
                    os.makedirs('/Users/wangxiangyang/PycharmProjects/pywork/doutu/doutu')

                r = requests.get(item['img_url'])
                filename = '{}'.format(item['name']) + item['img_url'][-4:].encode("utf-8")
                print (filename)
                with open('/Users/wangxiangyang/Documents/picture/'+filename, 'wb') as fo:
                    fo.write(r.content)
            except:
                print('Error!')
            yield item



