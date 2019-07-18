import re
from urllib.parse import urlparse

import scrapy
from scrapy import signals


class LinkCheckerSpider(scrapy.Spider):
    name = 'link_checker'
    handle_httpstatus_list = [404]
    valid_url = []
    invalid_url = []
    maxdepth = 2
    domain = ''

    def __init__(self, url='https://www.elle.com/fashion/', *args, **kwargs):
        super(LinkCheckerSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(LinkCheckerSpider, cls).from_crawler(crawler, *args, **kwargs)
        # Register the spider_closed handler on spider_closed signal
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_closed(self):
        """ Handler for spider_closed signal."""
        print('----------')
        print('There are', len(self.valid_url), 'working links and',
              len(self.invalid_url), 'broken links.', sep=' ')
        if len(self.invalid_url) > 0:
            print('Broken links are:')
            for invalid in self.invalid_url:
                print(invalid)
        print('----------')

    def parse(self, response):
        """ Main method that parse downloaded pages. """
        from_url = ''
        from_text = ''
        depth = 0;
        # Extract the meta information from the response, if any
        if 'from' in response.meta: from_url = response.meta['from']
        if 'text' in response.meta: from_text = response.meta['text']
        if 'depth' in response.meta: depth = response.meta['depth']

        if len(self.domain) == 0:
            parsed_uri = urlparse(response.url)
            self.domain = parsed_uri.netloc


        if response.status == 404:
            self.invalid_url.append({'url': response.url,
                                     'from': from_url,
                                     'text': from_text})
        else:
            self.valid_url.append({'url': response.url,
                                   'from': from_url,
                                   'text': from_text})
            parsed_uri = urlparse(response.url)
            if parsed_uri.netloc == self.domain and depth < self.maxdepth:
                a_selectors = response.xpath("//a")
                for selector in a_selectors:
                    text = selector.xpath('text()').extract_first()
                    link = selector.xpath('@href').extract_first()
                    request = response.follow(link, callback=self.parse)
                    request.meta['from'] = response.url
                    request.meta['text'] = text
                    yield request