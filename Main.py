import http.server
import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import parse_qs
import time

monto = 100
listaOferta = ['Oferta1', 'Oferta2', 'Oferta3']

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/server.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


def main():
    PUERTO =8200

    httpd = HTTPServer(('localhost', PUERTO), Serv)
    print('Servidor de subastas en el puerto %s' %PUERTO)
    httpd.serve_forever()

#subasta()
if __name__ == '__main__':
    main()