#!/bin/bash 
# Di chuyển vào đúng thư mục dự án trên Azure
cd app

# Kích hoạt môi trường và cập nhật thư viện
source venv/bin/activate
pip install -r requirements.txt

# Tắt server Python cũ nếu có
pkill -9 -f "python3 src/main.py" || true

# Khởi chạy server Python thuần chạy ngầm hoàn toàn
nohup python3 src/main.py > server.log 2>&1 &