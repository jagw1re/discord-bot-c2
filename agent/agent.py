from http.server import HTTPServer

from networking.networking import TaskingServer

PORT = 8000
HOST = "localhost"


def main():
    server = HTTPServer((HOST, PORT), TaskingServer)
    server.serve_forever()


if __name__ == "__main__":
    main()
