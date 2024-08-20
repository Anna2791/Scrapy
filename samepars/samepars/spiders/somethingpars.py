# import scrapy
#
#
# class SomethingparsSpider(scrapy.Spider):
#     name = "somethingpars"
#     allowed_domains = ["hoff.ru"]
#     start_urls = ["https://hoff.ru/catalog/tovary_dlya_doma/osveschenie/lustry_i_potolochnye_svetilniki/podvesnye_svetilniki/"]
#
#     def parse(self, response):
#         lights = response.css('div.product-name')
#         for light in lights:
#             yield {
#                 'name': light.css('div.product-name a::text').get(),
#                 'price': light.css('div.product-price a::text').get(),
#                 'url': light.css('div.product-name a').attrib['href']
#
#             }

import scrapy

class SomethingparsSpider(scrapy.Spider):
    name = "somethingpars"
    allowed_domains = ["svetonik.ru"]
    start_urls = ["https://svetonik.ru/site/50300/"]

    def parse(self, response):
        lights = response.css('div.bx_catalog_item')
        for light in lights:
            yield {
                'name': light.css('div.bx_catalog_item_title span::text').get(),
                'price': light.css('div.bx_price::text').get(),
                'url': light.css('a').attrib['href']
            }