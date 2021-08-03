#!/bin/sh
#go to the spider directory
cd /Users/long/Downloads/burger_project/burgerbot/burgerbot/spiders

PATH=$PATH:/usr/local/bin
export PATH
#https://click.palletsprojects.com/en/7.x/python3/
#export LC_ALL=en_US.utf-8

$PIPENV run scrapy crawl bot_proof -o new_proof.json

end_datetime=$(date '+%m_%d_%Y_%H_%M_%S')
echo "${end_datetime} - spider finished successfully"


 #41 15 * * * /opt/anaconda3/bin/python /Users/long/Downloads/burgerbot/burgerbot#/spiders/bot_long.py >> /Users/long/Downloads/b    ot.log 2>&1

 #54 * * * * /opt/anaconda3/bin/python && sh /Users/long/Downloads/burger_project/crawl.sh >> /Users/long/Downloads/cron.log 2 >&     1

 #38 15 * * * /usr/bin/python3 /Users/long/Downloads/test.py >> /Users/long/Downl#oads/bot.log 2>&1
# */5 * * * * export
# PIPENV=/usr/local/bin/pipenv && /Users/long/Downloads/burger_project/crawl.sh >> /Users/long/Downloads/cron.log 2 >& 1

# PATH=/usr/local/bin
# PIPENV=/usr/local/bin/pipenv
# */5 * * * *  cd /Users/long/Downloads/burger_project/burgerbot/burgerbot/spiders/ && $PIPENV run scrapy crawl bot_proof >> /Users/long/Downloads/cron.log 2 >& 1
