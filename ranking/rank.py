from importlib import import_module as mload
from pkgutil import walk_packages
from functools import partial

from multiprocessing import Pool

def get_metric(url, func):
    return func(url)

class Ranker(object):
    """
    Goes through the metrics module and returns scores based on the
    functions within that module

    Basically, any function called `score` will
    be assumed to be a part of our metrics
    """

    def __init__(self, metrics_module='metrics', function_name="score"):
        root = mload(metrics_module)
        all_packages = walk_packages(root.__path__, root.__name__ + ".")
        
        apis = [mload(package[1]) for package in all_packages]
        active_methods = [getattr(api, function_name, None) for api in apis]
        self.metrics = filter(None, active_methods)
        self.names = [metric.__module__.rpartition('.')[-1] for metric in self.metrics]
        self.pool = Pool(len(self.metrics))

    def all_scores(self, url):
        rank_op = partial(get_metric, url)
        scores = self.pool.map(rank_op, self.metrics)
        return dict(zip(self.names, scores))

test = Ranker() 
print test.all_scores('indico.io')
