from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from datetime import datetime
import random

PORT = 8000
BOXNAME = os.uname()[1]
MESSAGES = [
    "The technology you use impresses no one. The experience you create with it is everything.",
    "It has become appallingly obvious that our technology has exceeded our humanity.",
    "The real problem is not whether machines think but whether men do.",
    "Technology is best when it brings people together.",
    "Any sufficiently advanced technology is indistinguishable from magic.",
    "The advance of technology is based on making it fit in so that you don't really even notice it, so it's part of everyday life.",
    "The human spirit must prevail over technology.",
    "Innovation distinguishes between a leader and a follower.",
    "Technology is nothing. What's important is that you have a faith in people, that they're basically good and smart, and if you give them tools, they'll do wonderful things with them.",
    "The great myth of our times is the idea that technology can cure all of our social and political problems.",
    "Digital design is like painting, except the paint never dries.",
    "For a successful technology, reality must take precedence over public relations, for nature cannot be fooled.",
    "Technology, like art, is a soaring exercise of the human imagination.",
    "We are changing the world with technology.",
    "The Internet is becoming the town square for the global village of tomorrow.",
    "Once a new technology rolls over you, if you're not part of the steamroller, you're part of the road.",
    "Technology made large populations possible; large populations now make technology indispensable.",
    "Just because something doesn't do what you planned it to do doesn't mean it's useless.",
    "You cannot endow even the best machine with initiative; the jolliest steamroller will not plant flowers.",
    "Technology is a useful servant but a dangerous master.",
    ]

HEAD = "<HTML><HEAD><TITLE>Summit server!</TITLE></HEAD>\n"
BODY = f"<p><br>Welcome!<br> My hostname is {BOXNAME}</p>"
THANKS = "🆃🅷🅰🅽🅺 🆈🅾🆄 🅵🅾🆁 🅲🅾🅼🅸🅽🅶"

CONTENT = HEAD + BODY + "</HTML>"

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/index.html' or self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(CONTENT, "utf8"))
        elif self.path == '/app':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = random.choice(MESSAGES)
            self.wfile.write(bytes(HEAD + message, "utf8"))
            when = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            self.wfile.write(bytes(f"<br><br>The time is now: {when}", "utf8"))
        elif self.path == '/thanks': 
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-16')
            self.end_headers()
            self.wfile.write(bytes(HEAD + THANKS, "utf-16"))
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(CONTENT, "utf8"))
            self.wfile.write(bytes(f"<p>You requested {self.path} but I don't have that, try /index.html or /app", "utf8"))
        print(f"GET for {self.path} from {self.client_address[0]}")

server = HTTPServer(('', PORT), MyHandler)
print("Server started at http://localhost:8000")
server.serve_forever()

