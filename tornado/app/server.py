import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
Handlers=[
    (r"/", MainHandler),
]
application = tornado.web.Application(Handlers)
if __name__ == "__main__":
    application.listen(8000)
    print("Server Listening on 8000...")
    tornado.ioloop.IOLoop.instance().start()
