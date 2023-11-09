import http.server
from prometheus_client  import start_http_server, Counter

Request_count = Counter("app_request_count","Number of requessts received")

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        Request_count.inc()
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First python Application</title></head></html>"))
        self.wfile.close

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('51.20.117.254',5000), HandleRequests)
    server.serve_forever()