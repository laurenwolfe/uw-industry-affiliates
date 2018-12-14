class Company:
    """Object representing an affiliate company."""

    def __init__(self, name, joined_year, current):
        self.name = name
        self.joined_year = joined_year
        self.current = current

    def print_self(self):
        print(self.name)
        print(self.joined_year)
        print(self.current)

    def get_json(self):
        json_str = '{ "name": "{0}", "joined_year": {1}, "current_affiliate": {2} }'
        return json_str.format(self.name, self.joined_year, self.current)
