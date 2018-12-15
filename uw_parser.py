
def get_html(page):
    file = open(page, "r")
    return file.read()


def parse(html):
    companies = list()
    curr = True
    content = str(html).split("^^^")

    for c in content:
        c = c.strip("\', \'").strip()

        if c[0:2] == "<!":
            curr = False

        c = c.split("\"")

        if len(c) == 5:
            website = c[1]
            name_year = c[4].lstrip(">").rstrip(")")
            name_year = name_year.split("</a> (Member since ")
            companies.append((name_year[0], name_year[1], website, curr))
    return companies


def scrape(page):
    return parse(get_html(page))
