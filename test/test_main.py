import pytest
from io import BytesIO
from unittest.mock import Mock, patch
from src.main import SimpleHTTPRequestHandler

def test_server_response():
    # 1. Giả lập luồng nhận request (phải trả về chuỗi bytes đại diện cho HTTP GET)
    mock_rfile = BytesIO(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
    mock_wfile = BytesIO()
    
    # 2. Mock socket và request
    mock_request = Mock()
    
    # Kiềm chế không cho hàm khởi tạo gốc chạy tự động để tránh kẹt luồng socket thật
    with patch.object(SimpleHTTPRequestHandler, finish=Mock(), setup=Mock()):
        handler = SimpleHTTPRequestHandler.__new__(SimpleHTTPRequestHandler)
        handler.request = mock_request
        handler.rfile = mock_rfile
        handler.wfile = mock_wfile
        handler.headers = {}
        
        # 3. Chạy hàm xử lý do_GET
        handler.do_GET()
        
        # 4. Kiểm tra kết quả trả về
        mock_wfile.seek(0)
        result = mock_wfile.read().decode('utf-8')
        assert "Hello từ Server Azure!" in result