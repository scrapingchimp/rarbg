from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, TorrentItem


class RarbgTo(BasePortiaSpider):
    name = "rarbg.to"
    allowed_domains = ['rarbg.to']
    start_urls = [
        'https://rarbg.to/torrents.php?search=1080p&category%5B%5D=4']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*\\/torrent\\/.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                TorrentItem,
                None,
                '.lista-rounded',
                [
                    Field(
                        'title',
                        'tr:nth-child(1) > .block > b > .black *::text, tbody > tr:nth-child(1) > .block > b > .black *::text',
                        []),
                    Field(
                        'magnet',
                        'tr:nth-child(2) > td > div > .lista > tr:nth-child(1) > .lista > a:nth-child(3)::attr(href), tbody > tr:nth-child(2) > td > div > .lista > tr:nth-child(1) > .lista > a:nth-child(3)::attr(href), tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(1) > .lista > a:nth-child(3)::attr(href), tbody > tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(1) > .lista > a:nth-child(3)::attr(href)',
                        []),
                    Field(
                        'poster',
                        'tr:nth-child(2) > td > div > .lista > tr:nth-child(4) > .lista > img::attr(src), tbody > tr:nth-child(2) > td > div > .lista > tr:nth-child(4) > .lista > img::attr(src), tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(4) > .lista > img::attr(src), tbody > tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(4) > .lista > img::attr(src)',
                        []),
                    Field(
                        'description',
                        'tr:nth-child(2) > td > div > .lista > tr:nth-child(7) > .lista *::text, tbody > tr:nth-child(2) > td > div > .lista > tr:nth-child(7) > .lista *::text, tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(7) > .lista *::text, tbody > tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(7) > .lista *::text',
                        []),
                    Field(
                        'size',
                        'tr:nth-child(2) > td > div > .lista > tr:nth-child(15) > .lista *::text, tbody > tr:nth-child(2) > td > div > .lista > tr:nth-child(15) > .lista *::text, tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(15) > .lista *::text, tbody > tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(15) > .lista *::text',
                        []),
                    Field(
                        'peers',
                        'tr:nth-child(2) > td > div > .lista > tr:nth-child(21) > .lista *::text, tbody > tr:nth-child(2) > td > div > .lista > tr:nth-child(21) > .lista *::text, tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(21) > .lista *::text, tbody > tr:nth-child(2) > td > div > .lista > tbody > tr:nth-child(21) > .lista *::text',
                        [])])]]
