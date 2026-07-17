from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Trả về HTTP Status 200 (Thành công)
        self.send_response(200)
        # Định nghĩa kiểu nội dung trả về là text thuần
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        
        # Nội dung string muốn trả về
        message = "Hello từ Server Azure! Python thuần không cần FastAPI"
        self.wfile.write(message.encode("utf-8"))

def run_server():
    server_address = ("0.0.0.0", 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server đang chạy ở port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()