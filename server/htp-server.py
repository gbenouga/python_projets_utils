import http.server
#import socketserver

port = 80
address = ("", port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

#httpd = socketserver.TCPServer(address, handler)
httpd = server(address, handler)

print(f"Serveur démaré sur le port {port}")

httpd.serve_forever()