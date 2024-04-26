import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class GoogleSearchSpider(scrapy.Spider):
    name = 'google'
    
    def __init__(self, query):
        self.query = query
        self.start_urls = ['https://www.google.com/search?q=' + query]
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
    
    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)  # Give time for the page to load
        
        links = self.driver.find_elements_by_css_selector('a[href^="http"]')
        for link in links[:3]:  # Only consider the first 3 links
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse_link)
        
    def parse_link(self, response):
        sel = Selector(text=self.driver.page_source)
        # Scraping data from the current page
        text_data = sel.xpath('//text()').extract()
        # Scraping other links in the site
        other_links = sel.xpath('//a/@href').extract()

        for link in other_links:
            # Check if the link has a scheme, if not, add "http://" as the default scheme
            if not link.startswith(('http://', 'https://')):
                link = 'http://' + link
            yield scrapy.Request(link, callback=self.parse_link)

        yield {
            'url': response.url,
            'text_data': text_data,
            'other_links': other_links
        }

        
    def closed(self, reason):
        self.driver.quit()

query = input("Enter your search query: ")
process = CrawlerProcess()
process.crawl(GoogleSearchSpider, query=query)
process.start()