import requests

# Địa chỉ API đang chạy trên máy bạn
BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("\n[1] TEST KIỂM TRA SỨC KHỎE (/health)")
    response = requests.get(f"{BASE_URL}/health")
    print(f" - Mã trạng thái: {response.status_code}")
    print(f" - Dữ liệu trả về: {response.json()}")

def test_translation_success():
    print("\n[2] TEST DỊCH THÀNH CÔNG (/generate)")
    payload = {"text": "Artificial Intelligence and Machine Learning are fascinating fields."}
    response = requests.post(f"{BASE_URL}/generate", json=payload)
    print(f" - Mã trạng thái: {response.status_code}")
    print(f" - Dữ liệu trả về: {response.json()}")

def test_translation_empty_error():
    print("\n[3] TEST LỖI BỎ TRỐNG (/generate)")
    # Cố tình gửi một chuỗi toàn dấu cách
    payload = {"text": "      "}
    response = requests.post(f"{BASE_URL}/generate", json=payload)
    print(f" - Mã trạng thái: {response.status_code}")
    print(f" - Dữ liệu trả về: {response.json()}")

if __name__ == "__main__":
    print("=== BẮT ĐẦU CHẠY KIỂM THỬ TỰ ĐỘNG ===")
    try:
        test_health()
        test_translation_success()
        test_translation_empty_error()
        print("\n=== HOÀN TẤT KIỂM THỬ ===")
    except requests.exceptions.ConnectionError:
        print("\n[LỖI] Không thể kết nối. Server API của bạn đang tắt!")