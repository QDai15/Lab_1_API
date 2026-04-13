# Khai báo thư viện và tạo ứng dụng API.
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Tải mô hình AI từ file model.py.
from model import TranslatorModel

app = FastAPI(title="English to Vietnamese Translator API")

# Cho phép các trang web khác gọi API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Tải mô hình AI khi khởi động máy chủ.
print("Đang khởi động AI, vui lòng đợi...")
translator = TranslatorModel()

# Quy định khuôn mẫu dữ liệu đầu vào.
class TranslateRequest(BaseModel):
    text: str

# Các đường dẫn kiểm tra trạng thái máy chủ.
@app.get("/")
def read_root():
    return {
        "name": "English to Vietnamese Translator API",
        "description": "API su dung mo hinh Helsinki-NLP/opus-mt-en-vi",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API dang hoat dong binh thuong!"
    }

# Hàm xử lý dịch và kiểm duyệt dữ liệu.
@app.post("/generate")
def generate_translation(request: TranslateRequest):
    text_to_translate = request.text.strip()

    # Báo lỗi nếu văn bản bị bỏ trống.
    if not text_to_translate:
        raise HTTPException(
            status_code=400, 
            detail="Văn bản cần dịch không được để trống!"
        )

    # Báo lỗi nếu văn bản quá 500 ký tự.
    if len(text_to_translate) > 500:
        raise HTTPException(
            status_code=400, 
            detail="Văn bản quá dài! Vui lòng nhập dưới 500 ký tự."
        )

    # Gọi AI dịch và trả về kết quả.
    translated_text = translator.translate(text_to_translate)

    return {
        "english": text_to_translate,
        "vietnamese": translated_text
    }