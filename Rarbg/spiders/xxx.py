# -*- coding: utf-8 -*-
import scrapy


class XxxSpider(scrapy.Spider):
    name = 'xxx'
    allowed_domains = ['rarbg.to']
    start_urls = ['https://rarbg.to/torrents.php?search=1080p&category%5B%5D=4']

    def parse(self, response):
        for torrent_url in response.xpath("/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table[2]/tbody/tr[@class=lista2]/td[2]/a/@href").extract():
            yield scrapy.Request(response.urljoin(torrent_url), callback=self.parse_torrent_page)
            
    def parse_torrent_page(self, response):
        item = {}
        torrent = response.xpath("/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div/table")
        item["title"] = torrent.css(".//tbody/td[2]/img/@alt").extract_first()
        yield item
