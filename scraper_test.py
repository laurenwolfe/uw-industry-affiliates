import parser
from Company import *

#  current_affils, prev_affils = parser.scrape("https://www.cs.washington.edu/industrial_affiliates/current")
#  parser.scrape("https://www.cs.washington.edu/industrial_affiliates/current")

#  returns (company, year, website, current)
aff_companies = parser.scrape("data/affiliate.html")
company_json = ""

for aff_company in aff_companies:
    res = Company(aff_company[0], aff_company[1], aff_company[2], aff_company[3])
    json = res.get_json()
    if company_json:
        company_json = company_json + ', ' + json
    else:
        company_json = json



