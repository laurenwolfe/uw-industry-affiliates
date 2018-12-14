#  from bs4 import BeautifulSoup, Comment
#  import urllib.request

def get_html(page):
    #  with urllib.request.urlopen(page) as file:

    file = open(page, "r")
    return file.read()


def parse(html):
    companies = list()
    curr = True

    #  soup = BeautifulSoup(html, 'html.parser')
    #  content = soup.find('div', attrs={'class', 'field-item even'}).li
    #  content = str(content).split("\n")

    content = str(html).split("^^^")
    for c in content:
        c = c.strip("\', \'").strip()

        if c[0:2] == "<!":
            curr = False

        c = c.split("\"")

        if len(c) < 5:
            print("error parsing data, index < 5")

        website = c[1]
        name_year = c[4].lstrip(">").rstrip(")")
        name_year = name_year.split("</a> (Member since ")
        companies.append((name_year[0], name_year[1], website, curr))
    return companies


def scrape(page):
    return parse(get_html(page))
