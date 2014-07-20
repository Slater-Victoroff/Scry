import json, urllib
import locale

def score(url):
    query = urllib.urlencode({'q': 'link:%s' % url})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_results = urllib.urlopen(url).read()
    results = json.loads(search_results)
    return int(results['responseData']['cursor']['estimatedResultCount'])
