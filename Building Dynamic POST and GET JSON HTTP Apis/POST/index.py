'''
Building a json POST endpoint that writes to a text file on the backend
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

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt","a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully"}))  #run in postman like http://localhost:8882/list?fruit=Mango and also run again in chrome to check updated one

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/list",listRequestHandler)
    ])
    port = 8882
    app.listen(port)
    print(f"Application has started and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
