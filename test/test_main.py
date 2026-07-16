import pytest
from fastapi.testclient import TestClient

from src.main import app 


client = TestClient(app)

def test_read_root():
    
    response = client.get("/")
    
    
    assert response.status_code == 200
    
    
    assert response.json() == "Hello từ Server Azure! CD đã hoạt động thành công 🎉"