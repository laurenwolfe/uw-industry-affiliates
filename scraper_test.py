import parser
from Company import *

current_affils, prev_affils = parser.scrape("https://www.cs.washington.edu/industrial_affiliates/current")
json_str = ""

for affil in current_affils:
    company = Company(affil[0], affil[1], True)
    company.print_self()
