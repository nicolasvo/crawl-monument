# -*- coding: utf-8 -*-
import scrapy
from ..items import MonumentItem


class BoiSpider(scrapy.Spider):
    name = 'boi'
    allowed_domains = ['http://www.culture.gouv.fr/']
    start_urls = ["http://www.culture.gouv.fr/public/mistral/dapamer_fr?ACTION=RETROUVER&NUMBER={0}&GRP={1}&REQ=%28%28paris%29%20%3aLOCA%2cPLOC%20%29&USRNAME=nobody&USRPWD=4%24%2534P&SPEC=&SYN=1&IMLY=&MAX1=1&MAX2=1&MAX3=200&DOM=MH".format(x+1,y) for y in range(10) for x in range(200)]

    def parse(self, response):
        monument_item = MonumentItem()
        x = response.xpath('//table[@width="566"]/./tr')[0]
        monument_item['appelation'] = x.xpath('.//b/text()').extract()[0].strip()
        monument_item['url'] = response.url
        
        for x in response.xpath('//table[@width="566"]/./tr'):
            var_td = x.xpath('./td[1]/font/n/text()').extract()[0].lower()
            if "adresse" in var_td:
                monument_item['adresses'] = x.xpath('td[2]/font/n/text()').extract()[0].strip()
            elif "date protection" in var_td:
                monument_item['date_protection'] = x.xpath('td[2]/font/n/text()').extract()[0].strip()
                if "mh" in x.xpath('td[2]/font/n/text()').extract()[0].strip().lower():
                    monument_item['inscrit_mh'] = True
                else: monument_item['inscrit_mh'] = False
            elif "pr" and "protection" in var_td:
                monument_item['prec_protection'] = x.xpath('td[2]/font/n/text()').extract()[0].strip()
            elif "dénomination" in var_td:
                monument_item['denomination'] = [x.strip() for x in x.xpath('td[2]/font/n/text()').extract()[0].strip().split(";")]
            elif "eléments mh" in var_td:
                monument_item['elements_mh'] = [x.strip() for x in x.xpath('td[2]/font/n/text()').extract()[0].strip().split(";")]
            elif "date(s)" in var_td:
                monument_item['date'] = x.xpath('td[2]/font/n/text()').extract()[0].strip()
            elif "historique" in var_td:
                monument_item['historique'] = x.xpath('td[2]/font/n/text()').extract()[0].strip()            
            elif "statut" in var_td:
                monument_item['statut'] = x.xpath('td[2]/font/n/text()').extract()[0].strip()
        yield monument_item           
