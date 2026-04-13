from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1. Nhập khẩu (Import) não bộ AI từ file model.py của bạn
from model import TranslatorModel

app = FastAPI(title="English to Vietnamese Translator API")

# 2. Cấu hình CORS (Để các website khác có thể gọi API này)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# 3. Khởi tạo mô hình AI ngay khi Server vừa bật lên
print("Đang khởi động AI, vui lòng đợi...")
translator = TranslatorModel()

# 4. Định nghĩa khuôn mẫu dữ liệu đầu vào bằng Pydantic
class TranslateRequest(BaseModel):
    text: str

# --- CÁC ENDPOINT CŨ ---

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

# 5. Endpoint Cốt lõi: Xử lý dịch thuật (Đã nâng cấp có bắt lỗi)
@app.post("/generate")
def generate_translation(request: TranslateRequest):
    # Lấy câu tiếng Anh và xóa khoảng trắng thừa ở đầu/cuối bằng hàm .strip()
    text_to_translate = request.text.strip()

    # --- BẮT ĐẦU PHẦN KIỂM TRA LỖI ---

    # Lỗi 1: Gửi lên chuỗi rỗng hoặc toàn dấu cách
    if not text_to_translate:
        raise HTTPException(
            status_code=400, 
            detail="Văn bản cần dịch không được để trống!"
        )

    # Lỗi 2: Giới hạn độ dài để tránh spam làm treo AI (Ví dụ: tối đa 500 ký tự)
    if len(text_to_translate) > 500:
        raise HTTPException(
            status_code=400, 
            detail="Văn bản quá dài! Vui lòng nhập dưới 500 ký tự."
        )

    # --- KẾT THÚC PHẦN KIỂM TRA LỖI ---

    # Nếu qua được các chốt chặn trên thì mới cho AI dịch
    translated_text = translator.translate(text_to_translate)

    return {
        "english": text_to_translate,
        "vietnamese": translated_text
    }