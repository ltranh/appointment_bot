from ..items import BurgerbotItem
from ..constants import constant
import os
import scrapy
import time
from scrapy.crawler import CrawlerProcess
from twilio.rest import Client
from scrapy.linkextractors import LinkExtractor


class BotSpidere(scrapy.Spider):
    #initialization
    name = constant.BOT_NAME
    allowed_domains = ['berlin.de']
    start_urls = [constant.URL]


    def parse(self, response):
        #twillio setup & credentials
        account_sid = constant.PLACEHOLDER
        auth_token = constant.PLACEHOLDER
        client = Client(account_sid, auth_token)

        #initialization
        items = BurgerbotItem()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        #finding the link for the table of the next month
        links = LinkExtractor(restrict_css='.next a').extract_links(response)[0]

        #using css clasifiers to find desired data
        for mt in response.css('div.calendar-month-table'):
            month = mt.css(' th.month::text').get()
            for td in mt.css(' td'):

                #refers to the type of slot buchbar - bookable, nichbuchbar - unbookable
                clas =  td.xpath("@class").get()
                #assigning information to item object
                items[constant.DATE] = clas
                items[constant.TIME] = current_time
                items[constant.MONTH] = month
                #extracting the dates of the bookable slots - may not be entirely accurate
                date = td.css('.buchbar.heutemarkierung a::text').get()
                date1 = td.css('.buchbar a::text').get()
                #for bookable slots that open TODAY
                if clas == constant.BOOKABLE_TODAY :
                    #extracts the link for an appointment slot if one exists
                    link_reg = LinkExtractor(restrict_css='.buchbar.heutemarkierung a').extract_links(response)[0]
                    items[constant.DATE] = date
                    #for easy recoggnition in json file
                    items[constant.MONTH] = month + constant.TAG
                    #Twilio api call using a pre approved template
                    message = client.messages.create(
                                                  from_=constant.TRIAL_NUMBER,
                                                  body=constant.TEMPLATE.format(month,date),
                                                  to=constant.RECIPIENT_1
                    )
                    #API information for debugging
                    print(message.sid)
                    #notifies developer
                    os.system('say "Beer time."')
                    message1 = client.messages.create(
                                                  from_=constant.TRIAL_NUMBER,
                                                  body=constant.TEMPLATE.format(month,date),
                                                  to=constant.RECIPIENT_2
                    )

                elif clas == constant.BOOKABLE:
                    #extracts the link for an appointment slot if one exists
                    link_reg = LinkExtractor(restrict_css='.buchbar a').extract_links(response)[0]
                    items[constant.DATE] = date1
                    #additional tag used for easy recoggnition in json file
                    items[constant.MONTH] = month + constant.TAG
                    message = client.messages.create(
                                                  from_=constant.TRIAL_NUMBER,
                                                  body=constant.TEMPLATE.format(month,link_reg.url),
                                                  to=constant.RECIPIENT_1
                    )
                    #notifies developer
                    os.system('say "Vine time."')
                    print(message.sid)
                    message1 = client.messages.create(
                                                  from_=constant.TRIAL_NUMBER,
                                                  body=constant.TEMPLATE.format(month,link_reg.url),
                                                  to=constant.RECIPIENT_2
                    )
                    message2 = client.messages.create(
                                                  from_=constant.TRIAL_NUMBER,
                                                  body=constant.TEMPLATE.format(month,link_reg.url),
                                                  to=constant.RECIPIENT_3
                    )
                #printing item object to JSON file that can be produced by the bot
                yield items
        #follows the link of the next month table so that more months can be scraped
        yield response.follow(links, callback=self.parse)

#running the bot
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(BotSpidere)
    process.start()
