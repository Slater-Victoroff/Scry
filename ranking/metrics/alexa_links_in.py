import requests

from lxml import etree

def score(url):
    alexa_url = 'http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' % url
    document = etree.XML(requests.get(alexa_url).content)
    return get_links_in(document)

def get_links_in(document):
    links_in = document.xpath('//LINKSIN')
    return links_in[0].get('NUM')

if __name__ == "__main__":
    import sys
    print score(sys.argv[1])
