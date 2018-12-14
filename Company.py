class Company():
    """Object representing an affiliate company."""

    def __init__(self, co_name, joined_year, website, current):
        self.co_name = co_name
        self.joined_year = joined_year
        self.website = website
        self.current = current

    def get_json(self):
        json_str = "{{ \"name\": \"{}\", \"joined_year\": {}, \"website\": \"{}\", \"current_affiliate\": {} }}"
        return json_str.format(self.co_name, self.joined_year, self.website, self.current)
