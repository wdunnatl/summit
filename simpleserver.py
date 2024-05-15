from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
PORT = 8000

os.chdir('.')
boxname = os.uname()[1]

index = open("./index.html", "w")
header = "<HTML><HEAD><TITLE>Summit server!</TITLE></HEAD>\n"
body = f"<br>Welcome!<br> This is {boxname}"

index.write(header + body)
index.close()

server = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
print("Server started at http://localhost:8000")
server.serve_forever()

