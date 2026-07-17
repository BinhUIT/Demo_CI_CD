#!/content/bash
# Di chuyển vào đúng thư mục dự án trên Azure
cd /home/azureuser/app

# Kích hoạt môi trường và cập nhật thư viện
source venv/bin/activate
pip install -r requirements.txt

# Tắt server Python cũ nếu có
pkill -9 -f "python src/main.py" || true

# Khởi chạy server Python thuần chạy ngầm hoàn toàn
nohup python src/main.py > server.log 2>&1 &