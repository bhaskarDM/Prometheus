import http.server
import time
from prometheus_client  import start_http_server, Gauge

REQUEST_IN_PROGRESS = Gauge('request_in_progress','Number of live request in progress')
REQUEST_LAST_SERVED = Gauge('request_last_served','Time the application was last served')


class HandleRequests(http.server.BaseHTTPRequestHandler):

    @REQUEST_IN_PROGRESS.track_inprogress()
    def do_GET(self):
        #REQUEST_IN_PROGRESS.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First python Application</title></head></html>"))
        self.wfile.close
        REQUEST_LAST_SERVED.set_to_current_time()
        #REQUEST_LAST_SERVED.set(time.time())
        #REQUEST_IN_PROGRESS.dec()

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('172.31.19.25',5000), HandleRequests)
    server.serve_forever()