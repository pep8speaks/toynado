import tornado.ioloop
import tornado.web


class Main_Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
def make_app():
    return tornado.web.Application([
        (r"/", Main_Handler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()