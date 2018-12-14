import parser
from Company import *
from MData import *

#  current_affils, prev_affils = parser.scrape("https://www.cs.washington.edu/industrial_affiliates/current")
#  parser.scrape("https://www.cs.washington.edu/industrial_affiliates/current")

#  returns (company, year, website, current)
affiliates = parser.scrape("data/affiliate.html")
company_json = ""
db_conn = MData()

for affiliate in affiliates:
    affiliate_obj = Company(affiliate[0], affiliate[1], affiliate[2], affiliate[3])
    j_dict = affiliate_obj.make_dict()
    print(type(j_dict))
    idx_id = db_conn.put_json(j_dict)
    print(idx_id)
