import http.server
import time
from prometheus_client  import start_http_server, Summary

REQUEST_LATENCY_TIME = Summary('request_latency_time','latency in processing request')


class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        start_time= time.time()
        self.send_response(200)
        time.sleep(3)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First python Application</title></head></html>",'utf-8'))
        self.wfile.close
        end_time= time.time()-start_time
        REQUEST_LATENCY_TIME.observe(end_time)

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('172.31.19.25',5000), HandleRequests)
    server.serve_forever()