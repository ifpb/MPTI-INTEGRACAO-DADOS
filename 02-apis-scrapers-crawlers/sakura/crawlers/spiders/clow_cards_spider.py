import scrapy

from spiders.selectors import clow_cards_selectors as ccs
from loaders import ClowCardLoader
from items import ClowCardItem


class ClowCardsSpider(scrapy.Spider):
    name = 'clow-cards'
    start_urls = ['https://ccsakura.fandom.com/wiki/Clow_Cards']
    no_clow_version = ['/wiki/The_Hope', '/wiki/The_Nameless_Card']

    def parse(self, response):
        metadata = {'card_type': 'Clow Card'}
        card_urls = response.xpath(ccs.CARD_PAGE).getall()

        for url in card_urls:
            if url not in self.no_clow_version:
                yield response.follow(url=url, callback=self.parse_card, meta=metadata)

    def parse_card(self, response):
        loader = ClowCardLoader(item=ClowCardItem(), response=response)

        loader.add_xpath('card', ccs.NAME)
        loader.add_value('card_type', response.meta.get('card_type'))
        loader.add_xpath('img_url', ccs.IMAGE_URL)
        loader.add_xpath('sign', ccs.SIGN)
        loader.add_xpath('magic_type', ccs.MAGIC_TYPE)

        return loader.load_item()
