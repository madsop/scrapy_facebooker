import scrapy
from facebook_event import FacebookEventSpider
from scrapy.crawler import CrawlerProcess

pages = ["AttacNorge", "UngdomMotEU"]

def getProcess():
    return CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    })
 
def run():
    process = getProcess()
    for page in pages:
        process.crawl(FacebookEventSpider, page=page)
    process.start()

run()