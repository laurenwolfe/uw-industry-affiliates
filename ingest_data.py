from Company import *
from MData import *
import re
import uw_parser
import wiki_parser


def ingest_affiliate_list():
    #affiliate_list = list()
    affiliates = uw_parser.scrape("data/affiliate.html")

    for affiliate in affiliates:
        url_name = affiliate[0]
        page = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&" \
               "rvprop=content&format=xml&titles={}&rvsection=0".format(url_name)
        found_start = False
        wiki_dict = dict()
        rows = wiki_parser.clean_data(page)
        industry_keywords = ['industry_keywords', 'industry', 'product', 'service', 'company_type',
                             'language', 'research_field', 'platform', 'native_client', 'programming_language', 'operating system', 'website_type']
        headquarters = ['headquarters', 'hq_location_city', 'location_city', 'hq_location', 'location', 'city']
        website = ['url', 'website', 'webpage', 'homepage']
        key_people = ['key people', 'ceo', 'founders']
        num_employee = ['num_employee']
        keywords = industry_keywords + headquarters + key_people + num_employee
        # affiliate_list.append(Company(affiliate[0], affiliate[1], affiliate[2], affiliate[3], None))

        if rows:
            for row in rows:
                if found_start and row:
                    pair = row.partition("=")
                    key = pair[0].replace('|', '').strip()
                    value = pair[2].replace('|', '').strip()
                    print(key)
                    print(value)

                    if not value or not key or key in website:
                        break  # next company
                    else:
                        if word_match(key, keywords):
                            wiki_dict[key] = value
                        else:
                            break

                elif not found_start:
                    re.search(r'\s*Infobox\s*', row)
                    found_start = True
                    continue

        # push obj to database.
        record = Company(affiliate[0], affiliate[1], affiliate[2], affiliate[3], wiki_dict)


def word_match(word, lst):
    if word in lst:
        return True
    return False


def process_data():
    db_conn = MData()  # MongoDB db connection instance
    db_conn.clear_collection()
    ingest_affiliate_list()


if __name__ == "__main__":
    process_data()
