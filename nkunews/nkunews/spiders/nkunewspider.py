import scrapy
from nkunews.items import NkunewsItem


class NkunewspiderSpider(scrapy.Spider):
    name = "nkunewspider"
    allowed_domains = ["news.nankai.edu.cn"]
    start_urls = ["http://news.nankai.edu.cn/ywsd/index.shtml"]
    baseUrl = "http://news.nankai.edu.cn/ywsd/system/count//0003000/000000000000/000/000/c0003000000000000000_000000"
    offset = 570
    behind = ".shtml"

    def parse(self, response):
        
        node_list=response.xpath("//table[@width='98%']")
        
        for node in node_list:
            item = NkunewsItem()
            if len(node.xpath(".//tr/td[1]/div/a/text()")):
                item['NewsTitle'] = node.xpath(".//tr/td[1]/div/a/text()").extract()[0].encode("utf-8")
            else :
                item['NewsTitle'] =""
            
            if len(node.xpath(".//tr/td[1]/div/a/@href")):
                
                item['NewsUrl'] = node.xpath(".//tr/td[1]/div/a/@href").extract()[0].encode("utf-8")
                
            else:
                item['NewsUrl'] =""
            if len(node.xpath(".//tr/td[2]/div/text()")):
                
                item['NewsTime'] = node.xpath(".//tr/td[2]/div/text()").extract()[0].encode("utf-8")
            else:
                item['NewsTime'] =""
            yield item
            
        if self.offset > 0:
            url = self.baseUrl +str(self.offset) + self.behind
            yield scrapy.Request(url, callback = self.parse)
            self.offset -=1
            
         
