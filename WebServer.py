
from http.server import HTTPServer, BaseHTTPRequestHandler

httpd = HTTPServer(('[2602:61:7460:ed00:4fe:d88e:328d:fa3f]', 80), BaseHTTPRequestHandler)

httpd.serve_forever()