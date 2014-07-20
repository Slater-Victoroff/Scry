import json

import tornado.ioloop
import tornado.web

from ranking.rank import get_rank


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        url = self.get_argument('url', '')
        self.write(json.dumps(get_rank(url )))

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
