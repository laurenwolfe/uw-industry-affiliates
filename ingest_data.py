from Company import *
from MData import *

db_conn = MData()  # MongoDB db connection instance


def ingest_affiliates():
    import uw_parser

    # returns (company, year, website, current)
    # affiliates = parser.scrape("https://www.cs.washington.edu/industrial_affiliates/current")
    affiliates = uw_parser.scrape("data/affiliate.html")

    for affiliate in affiliates:
        affiliate_obj = Company(affiliate[0], affiliate[1], affiliate[2], affiliate[3])
        json_dict = affiliate_obj.make_dict()

        if json_dict:  # Prevents insert of duplicates into database
            mongo_id = db_conn.put_json(json_dict)
            if mongo_id:
                affiliate_obj.set_id(mongo_id)
