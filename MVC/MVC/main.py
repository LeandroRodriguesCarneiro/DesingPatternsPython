from tornado import ioloop
from tornado import httpserver
from tornado.web import Application

from controllers.produto_controller import Index, Novo, Atualizar, Deletar

class RunApp(Application):
    def __init__(self):
        handlers = [
            ('/', Index),
            ('/produto/novo', Novo),
            (r'/produto/update/(\d+)/status/(\d+)', Atualizar),
            (r'/produto/delete/(\d+)', Deletar),
        ]

        settings = dict(
            debug = True,
            template_path = 'views',
            static_path = 'static'
        )

        Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    httpserver = httpserver.HTTPServer(RunApp())
    httpserver.listen(8080)
    ioloop.IOLoop.instance().start()