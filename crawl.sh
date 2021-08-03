#!/bin/sh
#go to the spider directory
cd /Users/USER/Downloads/burger_project/burgerbot/burgerbot/spiders

PATH=$PATH:/usr/local/bin
export PATH


$PIPENV run scrapy crawl bot_proof -o new_proof.json

end_datetime=$(date '+%m_%d_%Y_%H_%M_%S')
echo "${end_datetime} - spider finished successfully"
