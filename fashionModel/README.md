# Fashion Model
## Part I - The Web Crawler

- Requires Python 3.6
- MongoDB installed

### Dependencies

- Scrapy(v1.0.3) : Web Crawlimg framework
- Pymongo(v3.0.3) : Tool for working with MongoDB 

Install with pip
- pip install Scrapy==1.0.3 
- pip install pymongo

To run the standalone scrapy program :

- scrapy crawl link_checker 

This will run the spider named link_checker.

- The output for now consists of all the links found in the given domain with a max depth upto two including the link - text
- One can see the output in a python list either when the spider terminates on its own ( could take upto several minutes ) or when its forcefully terminated ( clt + c). 
- A further modification will be extracting only the links correlating directly to the desired ouptput ( i.e topics which are latest and most debated.)








