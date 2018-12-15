from Company import *
from MData import *

db_conn = MData()  # MongoDB db connection instance


def ingest_affiliate_list():
    import uw_parser

    affiliate_list = list()

    # returns (company, year, website, current)
    affiliates = uw_parser.scrape("data/affiliate.html")

    for affiliate in affiliates:
        industry_affiliate = Company(affiliate[0], affiliate[1], affiliate[2], affiliate[3])
        affiliate_list.append(industry_affiliate)

    return affiliate_list


def ingest_wikipedia(affiliate_list):
    import wiki_parser
    # TODO
    # Make server calls to wikipedia for each company name, add data to objects


def add_affiliates_to_mongo(affiliates):
    for affiliate in affiliates:
        json_dict = affiliate.json_make_dict()

        if json_dict:
            mongo_id = db_conn.put_json(json_dict)
            if mongo_id:
                affiliate.set_id(mongo_id)


def process_data():
    affiliate_list = ingest_affiliate_list()

    if len(affiliate_list) == 0:
        sys.exit("No affiliate companies found during initial ingestion. Please check configuration.")

    # ingest wikipedia, update the Company objects.
    ingest_wikipedia(affiliate_list)

    # do whatever other ingestion desired

    # when data is complete, push to database?
    # or, create a dictionary that stores the company names and document ids,
    # so that the records can be easily updated en mass.

    add_affiliates_to_mongo(affiliate_list)


