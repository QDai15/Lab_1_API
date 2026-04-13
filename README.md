# AI Translator Pro: English to Vietnamese API

## 1. Thông tin sinh viên
* **Họ và tên:** Đỗ Quốc Đại
* **MSSV:** 24120030
* **Lớp:** 24CTT3

## 2. Thông tin mô hình (Hugging Face)
* **Tên mô hình:** `Helsinki-NLP/opus-mt-en-vi`
* **Loại mô hình:** Dịch máy (Machine Translation)
* **Liên kết gốc:** [https://huggingface.co/Helsinki-NLP/opus-mt-en-vi](https://huggingface.co/Helsinki-NLP/opus-mt-en-vi)

## 3. Mô tả chức năng hệ thống
Dự án này là một hệ thống Web API được xây dựng bằng **FastAPI**, nhằm mục đích khai thác mô hình dịch thuật từ Hugging Face để dịch các đoạn văn bản từ Tiếng Anh sang Tiếng Việt. Hệ thống cung cấp các endpoint để kiểm tra trạng thái máy chủ và thực hiện dịch văn bản với cơ chế kiểm tra lỗi dữ liệu đầu vào.

## 4. Hướng dẫn cài đặt thư viện
**Bước 1:** Clone repository này về máy.
```bash
git clone https://github.com/QDai15/Lab_1_API.git
cd [Tên_thư_mục]
```
**Bước 2:** Tạo môi trường ảo và cài đặt các thư viện cần thiết từ file **requirements.txt**.
```bash
python -m venv venv
venv/Scripts/activate      # Dành cho Windows
# source venv/bin/activate # Dành cho macOS/Linux
pip install -r requirements.txt
```

## 5. Hướng dẫn chạy chương trình
Khởi động server FastAPI bằng lệnh
```bash
uvicorn main:app --reload
```
(**Lưu ý:** Trong lần chạy đầu tiên, hệ thống sẽ mất một chút thời gian để tải weights của mô hình từ Hugging Face về máy).

## 6. Hướng dẫn gọi API và ví dụ (Request/Response)
API được phục vụ tại địa chỉ mặc định: http://127.0.0.1:8000
* **Endpoint 1:** Kiểm tra trạng thái
Method: GET /health
Response thành công:
```json
{
  "status": "ok",
  "message": "API dang hoat dong binh thuong!"
}
```
* **Endpoint2:** Xử lý dịch thuật
Method: POST /generate
Body
```json
{
  "text": "Artificial Intelligence is shaping the future of technology."
}
```
Response thành công:
```json
{
  "english": "Artificial Intelligence is shaping the future of technology.",
  "vietnamese": "Trí tuệ nhân tạo đang định hình tương lai của công nghệ."
}
```

## 7. Liên kết video demo
https://drive.google.com/file/d/1g1Ebr_jJ0PDvijIRPuadKM-EWOWTR-39/view?usp=sharing
