import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import sys


class ScrapeParser(HTMLParser):
    last_tag = None
    left_col = False
    left_cols = list()
    right_cols = list()
    right_els = list()

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        self.is_left_col(tag)

    def handle_endtag(self, tag):
        self.last_tag = tag
        self.is_left_col(tag)

    def handle_data(self, data):
        if self.left_col:
            self.left_cols.append(data)  # append left val
            if len(self.right_els) > 0:
                self.right_cols.append(self.right_els)  # append right val list and reset it to empty
                self.right_els = list()
        else:
            if data and not data.isspace() and len(self.left_cols) > 0:
                self.right_els.append(data)

    def is_left_col(self, tag):
        if tag == 'th':
            self.left_col = True
        if tag == 'td':
            self.left_col = False

    def error(self, message):
        sys.exit(message)


def ingest_url(p_url):
    wiki_dict = {}
    page = requests.get(p_url)

    if page.status_code != 200:
        return page.status_code, wiki_dict

    soup = BeautifulSoup(page.content, 'html.parser')
    infobox = soup.table.find("tbody")
    parser = ScrapeParser()

    rows = str(infobox).split("<tr>")

    for row in rows:
        parser.feed(row)

    keys = parser.left_cols
    val_lists = parser.right_cols

    # pushes last right column elements list onto the outer list
    if len(parser.right_els) > 0:
        parser.right_cols.append(parser.right_els)
        parser.right_els = list()

    for i in range(len(keys)):
        wiki_dict[keys[i]] = val_lists[i]

    return page.status_code, wiki_dict
