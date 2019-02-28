#! -*- coding: utf-8 -*-
import scrapy
import re
from urllib import quote, unquote

majorTitles = []

class GkpSplicer(scrapy.Spider):
    name = 'gkp'
    allowed_domains = ['gaokaopai.com']
    mids = ["080601", "081004", "082303", "080602T", "080503T", "550306", "580204", "550309", "7000080", "7000085", "7000093", "7000096", "7000094", "560403", "7000162", "580202", "7000179", "7000257", "7000279", "7000299", "7000277", "080801", "080203", "080206", "081806T", "580303", "7000168", "7000170", "7000169", "7000259", "7000278"]
    prosses = ["42", "3", "1", "1", "4", "13", "7", "3", "3", "1", "3", "6", "1", "11", "2", "69", "2", "5", "1", "2", "2", "39", "19", "11", "1", "3", "11", "1", "12", "4", "3"]
    majorsurl = []
    for idx in range(len(mids)):
        for num in range(int(prosses[idx])):
            majorsurl.append('http://www.gaokaopai.com/zhuanye-yuanxiao-%s-p-%s.html' % (mids[idx], num+1))
    start_urls = majorsurl
    # print(start_urls)
    # start_urls = start_urls[-1:]

    def parse(self, response):
        global majorTitles
        majorTitle = response.xpath('//div[@class="majorTitle"]/h1/text()').extract()[0].encode('utf-8')
        with open('result.txt', 'a+') as f:
            if majorTitle not in majorTitles:
                f.write('\n\n*********%s*********\n' % majorTitle)
                majorTitles.append(majorTitle)
            for t in response.xpath('//div[@class="tit"]/h3/a/text()').extract():
                f.write('\n')
                f.write(t.encode('utf-8'))
        # filename = response.url.split('/')[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # for t in response.xpath('//span[@class="pageInfo"]/text()').extract():
        #     with open('gross.txt', 'a+') as f:
        #         f.write('\n')
        #         f.write(re.split('[^\/]*\/(\d+).*', t)[1].encode('utf-8'))

class GkpMajoridSpider(scrapy.Spider):
    name = 'gkpi'
    majors = ["电气工程及其自动化", "建筑电气与智能化", "农业电气化", "智能电网信息工程", "新能源科学与工程", "供用电技术", "电力系统自动化技术", "高压输配电线路施工运行与维护", "电力系统继电保护与自动化技术", "分布式发电与微电网技术", "风力发电工程技术", "光伏发电技术与应用", "风电系统运行与维护", "建筑电气工程技术", "电机与电器技术", "电气自动化技术", "船舶电气工程技术", "铁道供电技术", "港口电气技术", "城市轨道交通供配电技术", "船舶电子电气技术", "自动化", "材料成型及控制工程", "过程装备与控制工程", "交通设备与控制工程", "自动化生产设备应用", "工业过程自动化技术", "工业自动化仪表", "智能控制技术", "铁道信号自动控制", "港口机械与自动控制"]
    majorsurl = []
    for majorname in majors:
        majorsurl.append('http://www.gaokaopai.com/zhuanye-search.html?keyword=%s&t=3' % majorname)
    allowed_domains = ['gaokaopai.com']
    start_urls = majorsurl

    def parse(self, response):
        with open('number.txt', 'a+') as f:
            for t in response.xpath('//div[@class="majorList"]/ul[@class="list"]/li/h3/a').extract():
                tsplits = re.split('.*-jianjie-([^\.]+)\.html[^>]*>([^<]*)<[^<]*', t.encode('utf-8'))
                # f.write('\n')
                # f.write(tsplits[1])
                # f.write('\n')
                # f.write(tsplits[2])
                if unquote(re.split('.*?keyword=([^&]+)&t=.*', response.url)[1]) == tsplits[2]:
                    f.write('\n')
                    f.write(tsplits[1])
                #     
                # f.write('\n')
                # f.write(t.encode('utf-8'))
                # f.write('\n')
                # f.write(unquote(re.split('.*?keyword=([^&]+)&t=.*', response.url)[1]))
                # f.write('\n')
                # f.write(re.split('[^>]*>([^<]*)<.*', t.encode('utf-8'))[1])
                # f.write('\n')
                # f.write(t.encode('utf-8'))

class GkpMajorgrossSpider(scrapy.Spider):
    name = 'gkpg'
    mids = ["080601", "081004", "082303", "080602T", "080503T", "550306", "580204", "550309", "7000080", "7000085", "7000093", "7000096", "7000094", "560403", "7000162", "580202", "7000179", "7000257", "7000279", "7000299", "7000277", "080801", "080203", "080206", "081806T", "580303", "7000168", "7000170", "7000169", "7000259", "7000278"]
    majorsurl = []
    for mid in mids:
        majorsurl.append('http://www.gaokaopai.com/zhuanye-yuanxiao-%s-p-1.html' % mid)
    allowed_domains = ['gaokaopai.com']
    start_urls = majorsurl

    def parse(self, response):
        for t in response.xpath('//span[@class="pageInfo"]/text()').extract():
            with open('gross.txt', 'a+') as f:
                f.write('\n')
                f.write(re.split('[^\/]*\/(\d+).*', t)[1].encode('utf-8'))