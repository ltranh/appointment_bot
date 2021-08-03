# Appointment-BOT
## Overview
This is a Bot that notifies the user when a new bookable appointment appears on the https://service.berlin.de/terminvereinbarung website. Can be adapted for different appointment websites.
### Libraries used
This project utilizes the Scrapy library as well as the Twilio Whatsapp API.
### Objective
A crawler is implmented to scrape a website for appointments that appear rarely and without notice. Most of the time the appointments are booked (red colored box).
The bot looks at the current two months and then also checks the following third month for open bookings.
Once an open booking is found, it uses the Twilio Whatsapp Sandbox API to send a message to any given Whatsapp number. 
### Implement it!
If you would like to implmement this project, signup for a Twilio trial and follow the guide on the following page:\ 
https://www.twilio.com/docs/whatsapp/sandbox
As you can see the bot uses a pre approved Sandbox Template, hence it is a bit cumbersome (this is done so that the bot can send a message in a 72 hour window withour restrictions by Whatsapp)
#### Setup
It is highly recommended to use a python virtual environment as that will make it easier for the bot to be run from an sh file. 
I used the cronjob below (write 'crontab -e' into your terminal and paste the following):/
```
PIPENV=/usr/local/bin/pipenv
*/3 * * * * sh /Users/USER/Downloads/burgerbot/crawl.sh >> /Users/USER/Downloads/cron.log 2 >& 1
```
The paths will depend on your implementation. PIPENV is the virtual environment of my choice. A cronjob allows to schedule sh script runs. My implementation runs every three minutes as you can 
see from the '*/3'. If you wanted to run the script every day at 15:03, you would write '3 15 * * *' (More info on crontabs in the sources)

Lastly an sh script is utilized to run the virtual environment as well as the bot command:
```
$PIPENV run scrapy crawl bot_proof -o new_proof.json
```
The -o new_proof.json will allow the bot to run to a json file. This is used for monitoring the exact states of the website at the respective time points.

To summarize the cronjob runs every three minutes to trigger the sh script which then runs the bot in a virtual environment. \
Sources:\
https://www.twilio.com/docs/whatsapp/quickstart/python \
https://docs.scrapy.org/en/latest/
https://ostechnix.com/a-beginners-guide-to-cron-jobs/
