'''
Building a simple GET HTTP method end point in Python
'''
import tornado.web  #The Tornado web server and tools. #tornado.web provides a simple web framework with asynchronous features that allow it to scale to large numbers of open connections, making it ideal for long polling 
import tornado.ioloop #In Tornado 6.0, .IOLoop is a wrapper around the asyncio event loop, with a slightly different interface. The .IOLoop interface is now provided primarily for backwards compatibility; new code should generally use the asyncio event loop interface directly. The IOLoop.current class method provides the IOLoop instance corresponding to the running asyncio event loop.

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world, this is a python command executed from the backend")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/animal",listRequestHandler)
    ])
    port = 8882
    app.listen(port)
    print(f"Application has started and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()

# class Application(
#     handlers: _RuleList | None = None,
#     default_host: str | None = None,
#     transforms: List[type[OutputTransform]] | None = None,
#     **settings: Any
# )

"""
A collection of request handlers that make up a web application.

Instances of this class are callable and can be passed directly to HTTPServer to serve the application:

    application = web.Application([
        (r"/", MainPageHandler),
    ])
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
The constructor for this class takes in a list of ~.routing.Rule objects or tuples of values corresponding to the arguments of ~.routing.Rule constructor: (matcher, target, [target_kwargs], [name]), the values in square brackets being optional. The default matcher is ~.routing.PathMatches, so (regexp, target) tuples can also be used instead of (PathMatches(regexp), target)

A common routing target is a RequestHandler subclass, but you can also use lists of rules as a target, which create a nested routing configuration:

    application = web.Application([
        (HostMatches("example.com"), [
            (r"/", MainPageHandler),
            (r"/feed", FeedHandler),
        ]),
    ])
In addition to this you can use nested ~.routing.Router instances, ~.httputil.HTTPMessageDelegate subclasses and callables as routing targets (see ~.routing module docs for more information).

When we receive requests, we iterate over the list in order and instantiate an instance of the first request class whose regexp matches the request path. The request class can be specified as either a class object or a (fully-qualified) name.

A dictionary may be passed as the third element (target_kwargs) of the tuple, which will be used as keyword arguments to the handler's constructor and ~RequestHandler.initialize method. This pattern is used for the StaticFileHandler in this example (note that a StaticFileHandler can be installed automatically with the static_path setting described below):

    application = web.Application([
        (r"/static/(.*)", web.StaticFileHandler, {"path": "/var/www"}),
    ])
    We support virtual hosts with the add_handlers method, which takes in a host regular expression as the first argument:

    application.add_handlers(r"www\.myhost\.com", [
        (r"/article/([0-9]+)", ArticleHandler),
    ])
If there's no match for the current request's host, then default_host parameter value is matched against host regular expressions.

warning

Applications that do not use TLS may be vulnerable to DNS rebinding <dnsrebinding> attacks. This attack is especially relevant to applications that only listen on 127.0.0.1 or other private networks. Appropriate host patterns must be used (instead of the default of r'.*') to prevent this risk. The default_host argument must not be used in applications that may be vulnerable to DNS rebinding.

You can serve static files by sending the static_path setting as a keyword argument. We will serve those files from the /static/ URI (this is configurable with the static_url_prefix setting), and we will serve /favicon.ico and /robots.txt from the same directory. A custom subclass of StaticFileHandler can be specified with the static_handler_class setting.
"""
