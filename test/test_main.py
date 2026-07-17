import pytest
from io import BytesIO
from unittest.mock import Mock
from src.main import SimpleHTTPRequestHandler

def test_server_response():
    # Giả lập (Mock) các thành phần luồng vào ra của request
    request = Mock()
    client_address = ('127.0.0.1', 8000)
    server = Mock()
    
    # Tạo đối tượng handler để test
    handler = SimpleHTTPRequestHandler(request, client_address, server)
    
    # Giả lập hàm ghi file đầu ra
    handler.wfile = BytesIO()
    
    # Chạy hàm xử lý request GET
    handler.do_GET()
    
    # Lấy kết quả mà server đã trả về
    handler.wfile.seek(0)
    result = handler.wfile.read().decode('utf-8')
    
    # Kiểm tra xem string trả về có đúng không
    assert "Hello từ Server Azure!" in result