
class Company:
    """Object representing an affiliate company."""
    def __init__(self, co_name, joined_year, website, current, fields):
        self.co_name = co_name
        self.joined_year = joined_year
        self.website = website
        self.current = current
        self.fields = fields
        self.mongo_id = None
        self.industry_keywords = ""
        self.num_employees = None
        self.headquarters = ""

    def add_wiki_data(self, keywords, employees, headquarters):
        self.industry_keywords = keywords
        self.num_employees = employees
        self.headquarters = headquarters

    def json_make_dict(self):
        json_dict = {
            "co_name": self.co_name,
            "joined_year": self.joined_year,
            "website": self.website,
            "current_affiliate": self.current,
            "mongo_id": self.mongo_id,
            "fields": self.fields
            }
        return json_dict


    def set_id(self, mongo_id):
        self.mongo_id = mongo_id
