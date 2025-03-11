from socketserver import BaseRequestHandler, TCPServer
import json

class MyTCPHandler(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        self.request.sendall(data[::-1])
        return super().handle()

with open('conf.json', 'r') as f:
    conf = json.load(f)

    host = conf['server']['address']
    port = conf['server']['port']
    server_name = conf['server']['server_name']

with TCPServer((host, port), MyTCPHandler) as srv:
    srv.serve_forever()