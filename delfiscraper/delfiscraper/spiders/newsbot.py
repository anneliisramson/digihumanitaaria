import scrapy


class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    allowed_domains = ['www.delfi.ee']
    #start_urls = ['https://www.delfi.ee/archive/?tod=03.12.2020&fromd=01.01.2020&channel=1&category=13&query=']
    #start_urls = ['https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=14&category=19350036&query=teadus']
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=21&category=0&query=majandus',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=1&category=13&query=uudised',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=47&category=67583634&query=poliitika',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=47&category=67583610&query=',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=1&category=0&query=koroona']
                
                
                
                
    start_urls = [
        
#hõberemmelga otsing - võib tulla korduvaid linke

#'https://old.delfi.ee/archive/?tod=31.12.2021&fromd=01.01.2017&channel=0&category=0&query=Haabersti+h%C3%B5beremmelga',
#'https://old.delfi.ee/archive/?tod=31.12.2021&fromd=01.01.2017&channel=0&category=0&query=Haabersti+h%C3%B5beremmelgas',
#'https://www.delfi.ee/otsing?search=Haabersti%20remmelga&domain=all&categoriesExternalId&order=LATEST&publishTimeFrom=2017-01-01T00%3A00%3A00Z&publishTimeTo=2021-12-31T21%3A59%3A59Z',
#'https://www.delfi.ee/otsing?search=Haabersti%20remmelgas&domain=all&categoriesExternalId&order=LATEST&publishTimeFrom=2017-01-01T00%3A00%3A00Z&publishTimeTo=2021-12-31T21%3A59%3A59Z'

#tselluloositehase otsing
'https://old.delfi.ee/archive/?tod=18.03.2022&fromd=01.01.2016&channel=1&category=0&query=tselluloositehas'

        
    ]

    def parse(self, response):
        HL_SELECTOR = '.headline'
        for news in response.css(HL_SELECTOR): 
            LINK_SELECTOR = 'h1 a ::attr(href)'
            yield {
                'link': news.css(LINK_SELECTOR).extract_first(),
            }
        next_page = response.xpath('.//a[@class="item item-next"]/@href').extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = 'http://www.delfi.ee' + next_href.strip()
            request = scrapy.Request(url=next_page_url)
            yield request