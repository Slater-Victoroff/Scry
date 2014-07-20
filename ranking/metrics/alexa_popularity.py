import requests

from lxml import etree

def score(url):
    alexa_url = 'http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' % url
    document = etree.XML(requests.get(alexa_url).content)
    return get_popularity(document)

def get_popularity(document):
    links_in = document.xpath('//POPULARITY')
    return links_in[0].get('TEXT')

if __name__ == "__main__":
    print score('indico.io')
