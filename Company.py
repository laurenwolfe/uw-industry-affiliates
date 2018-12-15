import wiki_parser


class Company:
    """Object representing an affiliate company."""

    def __init__(self, co_name, joined_year, website, current):
        self.co_name = co_name
        self.joined_year = joined_year
        self.website = website
        self.current = current
        self.mongo_id = None
        self.industry_keywords = ""
        self.num_employees = None
        self.headquarters = ""

    def make_json_str(self):
        json_str = "{{ \"name\": \"{}\", \"joined_year\": {}, \"website\": \"{}\", \"current_affiliate\": {} }}"
        return json_str.format(self.co_name, self.joined_year, self.website, self.current)

    def json_make_dict(self):
        if not self.mongo_id:
            json_dict = {
                "name": self.co_name,
                "joined_year": self.joined_year,
                "website": self.website,
                "current_affiliate": self.current
                }
            return json_dict
        else:
            return None

    def set_id(self, mongo_id):
        self.mongo_id = mongo_id

    def ingest_wiki_data(self):
        page = "https://en.wikipedia.org/wiki/" + self.co_name
        status_code, wiki_dict = wiki_parser.ingest_url(page)

        if status_code != 200:
            "No Wikipedia entry found for {}. Status code {}.".format(self.co_name, status_code)
        else:
            added = 0
            if 'Industry' in wiki_dict:
                self.industry_keywords = self.industry_keywords + wiki_dict['Industry']
                print(self.industry_keywords)
                added = added + 1
            if 'Products' in wiki_dict:
                self.industry_keywords = self.industry_keywords + wiki_dict['Products']
                print(self.industry_keywords)
                added = added + 1
            if 'Services' in wiki_dict:
                self.industry_keywords = self.industry_keywords + wiki_dict['Services']
                print(self.industry_keywords)
                added = added + 1
            if 'Type of Site' in wiki_dict:
                self.industry_keywords = self.industry_keywords + wiki_dict['Type of Site']
                print(self.industry_keywords)
                added = added + 1
            if 'Num Employees' in wiki_dict:
                self.industry_keywords = self.num_employees + wiki_dict['Num Employees']
                print(self.num_employees)
                added = added + 1
            if 'Headquarters' in wiki_dict:
                self.industry_keywords = self.headquarters + wiki_dict['Headquarters']
                print(self.headquarters)
                added = added + 1
            print()
            "{} columns added from Wikipedia for {}.".format(added, self.co_name)
