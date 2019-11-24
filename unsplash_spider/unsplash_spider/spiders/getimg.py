# -*- coding: utf-8 -*-
import scrapy
import re
import copy


class GetimgSpider(scrapy.Spider):
    name = 'getimg'
    allowed_domains = ['unsplash.com']
    start_urls = []
    word='dog' #搜索单词
    page_num=100 #页码深度
    for i in range(page_num):
        start_urls.append('https://unsplash.com/napi/search/photos?query='+word+'&page='+str(i+1))

    def parse(self, response):
        photo_id=re.findall('download":"https://unsplash.com/photos/(.*?)/download"',response.text)
        for i in range(len(photo_id)):
            yield scrapy.Request('https://unsplash.com/photos/'+photo_id[i]+'/download',meta={'id':copy.deepcopy(photo_id[i])},callback=self.parse_download)

    def parse_download(self, response):

        filename=response.meta['id']
        with open('image/'+filename+'.jpg','wb') as f:
            f.write(response.body)
