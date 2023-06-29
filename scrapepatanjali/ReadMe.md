Ubuntu: 
- sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
- cd ~/scrapepatanjali/scrapepatanjali/ && scrapy crawl patanjali --loglevel=INFO --logfile=log.txt

class: "."
id: "#"

cd ~/scrapepatanjali/scrapepatanjali/ && python3 spiders/create_shopbase_import_file.py