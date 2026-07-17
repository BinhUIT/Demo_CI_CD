import pytest
from io import BytesIO
from unittest.mock import Mock
from src.main import SimpleHTTPRequestHandler

def test_server_response():
    # 1. Chuẩn bị luồng nhận request giả lập và luồng ghi đầu ra
    mock_rfile = BytesIO(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
    mock_wfile = BytesIO()
    
    # 2. Tạo một class con kế thừa để triệt tiêu các hàm kết nối mạng thật của BaseHTTPRequestHandler
    class TestHandler(SimpleHTTPRequestHandler):
        def setup(self):
            pass  # Không chạy thiết lập socket thật
        def finish(self):
            pass  # Không chạy đóng socket thật

    # 3. Khởi tạo handler với các giá trị giả lập
    mock_request = Mock()
    client_address = ('127.0.0.1', 8000)
    mock_server = Mock()
    
    # Ép thuộc tính rfile và wfile vào trước khi hàm khởi tạo chạy
    TestHandler.rfile = mock_rfile
    TestHandler.wfile = mock_wfile
    
    handler = TestHandler(mock_request, client_address, mock_server)
    
    # 4. Lấy kết quả mà server đã ghi ra luồng dữ liệu
    mock_wfile.seek(0)
    result = mock_wfile.read().decode('utf-8')
    
    # 5. Kiểm tra nội dung trả về
    assert "Hello từ Server Azure!" in result