import scrapy
import csv

class PatanjaliSpider(scrapy.Spider):
    name = "patanjali"

    def start_requests(self):
        urls = [
           "https://www.patanjaliayurved.net/category/digestives/138",
#            "https://www.patanjaliayurved.net/category/health-and-wellness/139",
#            "https://www.patanjaliayurved.net/category/chyawanprash/150",
#            "https://www.patanjaliayurved.net/category/badam-pak/151",
#            "https://www.patanjaliayurved.net/category/ghee/152",
#            "https://www.patanjaliayurved.net/category/honey/153",
#            "https://www.patanjaliayurved.net/category/health-drinks/177"
#            "https://www.patanjaliayurved.net/category/fruit-beverage/184",
#   "https://www.patanjaliayurved.net/category/diet-food/218",
#   "https://www.patanjaliayurved.net/category/biscuits-and-cookies/3",
#   "https://www.patanjaliayurved.net/category/spices/11"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/candy/12"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/herbal-tea/13"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/jam/14"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/murabba/15"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/dalia-poha-and-vermicelli/130"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/flours/131"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/sauces-and-pickles/132"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/corn-flakes/183"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/dal-pulses/185"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/rice/186"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/noodles/190"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/oats/191"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/papad/192"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/namkeen/193"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/edible-oil/217"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/sweets/222"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/salt/230"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/sugar/231"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/dried-fruits-nuts/234"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/breakfast-cereals/243"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/kwath/5"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/vati/16"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/bhasma/17"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/churna/18"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/guggul/19"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/parpati-ras/134"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/pishti/135"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/arishta/178"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/asava/179"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/syrup/181"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/godhan-ark/199"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/oil/208"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/lep/210"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/balm-inhaler/211"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/eye-ear-oral-care/248"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/agarbatti-and-dhoops/7"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/hawan-samagri/200"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/pooja-essentials/220"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/dishwash-bar-and-gel/221"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/body-care/25"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/eye-care/137"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/shishu-care/207"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/swadeshi-samridhi-card/224"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/nutrition/233"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/nutrition-bar/235"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/spiritual/237"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/home/239"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/accessories/240"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/sports-wear/241"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/women-ethnic/242"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/copperware/245"
#   },
#   {
#     "url": "https://www.patanjaliayurved.net/category/dairy-frozen-items/247"
#   }
# ]
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_parent)

    def parse_parent(self, response):
        child_urls = response.css('div.categorytree>ul>li>ul>li>a::attr(href)').getall()        
        self.logger.info(' '.join(child_urls))
        for child_url in child_urls:
            yield scrapy.Request(url=response.urljoin(child_url), callback=self.parse_child)

    def parse_child(self, response):
        data = {
            'url': response.url,
            #'breadcrumb1': response.css('div.block-breadcrumb>ul.breadcrumb>li:nth-child(2)>a::text').get(),
            #'breadcrumb2': response.css('div.block-breadcrumb>ul.breadcrumb>li:nth-child(3)>a::text').get(),
            'lastbreadcrumb': response.css('div.block-breadcrumb>ul.breadcrumb>li.active::text').get(),
            'heading': response.css('div.product-detail-section>h3::text').get(),            
            # 'product-information': '<b>Product Information</b>' + response.css('div.product-information>div>p>font::text').get() + '\n<b>Benefits</b>' + response.css('#collapse1>div::text').get() 
            #     + '\n<b>Ingredients</b>' + response.css('#collapse2>div::text').get() + '\n<b>How to use</b>' + response.css('#collapse3>div>div:nth-child(1)>font::text').get()
            #     + '\n<b>Other Product Info</b>' + response.css('#collapse4>div.panel-body>font::text').get(),
            'weight': response.css('div.col-md-5.col-sm-4.details-custom>div>select>option::text').get(),
            'product-image': response.css('#product-main::attr(src)').get(),
        }
        
        # Save data to a CSV file
        with open('output.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            writer.writerow(data)
