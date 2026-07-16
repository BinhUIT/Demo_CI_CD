from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello từ Server Azure! CD đã hoạt động thành công 🎉"