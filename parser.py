from bs4 import BeautifulSoup, Comment
import urllib.request
import re


def get_html(page):
    with urllib.request.urlopen(page) as response:
        return response.read()


def parse(html):
    previous_companies = list()
    current_companies = list()

    soup = BeautifulSoup(html, 'html.parser')
    # select the section of html we want to strip
    content = soup.find('div', attrs={'class', 'field-item even'})

    # get all current affiliates
    html_li = content.ul.text
    res = html_li.split('\n')
    res = list(filter(is_blank, res))  # remove any empty elements in list

    for el in res:
        current_companies.append(el.strip())

    # get previous affiliates, remove comments and tags
    comments = content.findAll(text=lambda text: isinstance(text, Comment))

    for comment in comments:
        stripped_comment = re.sub("<.*?>", "", comment)
        previous_companies.append(stripped_comment.strip())  #remove anything within carets

    # finish parsing elements, return a tuple with company
    # name and the year they became affiliates
    current_companies = parse_member_year(current_companies)
    previous_companies = parse_member_year(previous_companies)
    return current_companies, previous_companies


# return the parsed year and name from a company list
def parse_member_year(companies):
    company_tuples = list()
    for company in companies:
        c = company.split("(")
        c1 = c[0].rstrip()
        c2 = re.sub(r'\D', "", c[1])
        company_tuples.append((c1, c2))
    return company_tuples


def is_blank(x):
    if x.isspace() or not x:
        return False
    return True


def scrape(page):
    return parse(get_html(page))
