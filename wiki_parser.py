import requests
from xml.etree import ElementTree


def clean_data(p_url):
    response = requests.get(p_url)
    root = ElementTree.fromstring(response.content)
    query = root.find('query')
    query = query.find('pages')
    query = query.find('page')

    if query:
        query = query.find('revisions')
        query = query.find('rev')
        text = ''.join(query.itertext())
        text = text.replace('{', "")
        text = text.replace('}', "")
        lines = text.splitlines()
        return lines



