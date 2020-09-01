from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re

class Servidor(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        pattern = pattern = re.compile(r"/produto/(?P<produto>\d*[0-9]+)")
        m = pattern.search(self.path)
        if m is None:
            self.send_response(400)
            self._set_headers()
            self.wfile.write('{"erro": "produto invalido"}'.encode())
            return

        produto =  m.group('produto')
        x = json.dumps({
            "path": produto
        })
        self._set_headers()
        self.wfile.write(x.encode())
        
httpd = HTTPServer(('localhost', 9001), Servidor)
httpd.serve_forever()