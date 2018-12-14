class Company:
    """Object representing an affiliate company."""

    def __init__(self, co_name, joined_year, website, current):
        self.co_name = co_name
        self.joined_year = joined_year
        self.website = website
        self.current = current
        self.mongo_id = None


    def make_json_str(self):
        json_str = "{{ \"name\": \"{}\", \"joined_year\": {}, \"website\": \"{}\", \"current_affiliate\": {} }}"
        return json_str.format(self.co_name, self.joined_year, self.website, self.current)

    def make_dict(self):
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

