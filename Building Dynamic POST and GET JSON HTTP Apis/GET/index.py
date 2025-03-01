'''
Building a json GET endpoint that reads from a text file on the backend
'''
import tornado.web
import tornado.ioloop
import json

class listRequestHandler(tornado.web.RequestHandler):      
    def get(self):
        fh = open("list.txt","r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/list",listRequestHandler)
    ])
    port = 8882
    app.listen(port)
    print(f"Application has started and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
