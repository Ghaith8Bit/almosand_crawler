import scrapy


class InvoiceSpiderSpider(scrapy.Spider):
    name = "invoice_spider"
    allowed_domains = ["dashboard.almosand.com"]
    start_urls = ["https://dashboard.almosand.com/invoices/create"]

    def parse(self, response):
        print('Spider is working!')
        # Add your scraping logic here
