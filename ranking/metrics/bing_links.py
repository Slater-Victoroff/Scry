import json

import requests

from lxml import etree
from lxml.cssselect import CSSSelector

def score(url):
    query_url = 'http://www.bing.com/search?q="%s"+-site:%s&FORM=MSNH' % (url, url)
    html = etree.HTML(requests.get(query_url).content)
    return get_results(html)

def get_results(document):
    results_selector = CSSSelector('div#b_tween span.sb_count')
    results = results_selector(document)
    try:
        return int(results[0].text.replace(',', '').split()[0])
    except IndexError:
        return 0

if __name__ == "__main__":
    import sys
    print score(sys.argv[1])
