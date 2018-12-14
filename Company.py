class Company:
    """Object representing an affiliate company."""

    def __init__(self, co_name, joined_year, website, current):
        self.co_name = co_name
        self.joined_year = joined_year
        self.website = website
        self.current = current

#    def make_json(self):
#        json_str = "{{ \"name\": \"{}\", \"joined_year\": {}, \"website\": \"{}\", \"current_affiliate\": {} }}"
#        return json_str.format(self.co_name, self.joined_year, self.website, self.current)

    def make_dict(self):
        json_dict = {
            "name": self.co_name,
            "joined_year": self.joined_year,
            "website": self.website,
            "current_affiliate": self.current
            }

        return json_dict
