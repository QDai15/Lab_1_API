from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class TranslatorModel:
    def __init__(self):
        # Tên mô hình dịch thuật Anh-Việt trên tảng Hugging Face
        model_name = "Helsinki-NLP/opus-mt-en-vi"
        print(f"Đang tải mô hình {model_name}...")
        print("(Quá trình này có thể mất vài phút cho lần chạy đầu tiên để tải data về máy)")
        
        # 1. Tải Tokenizer (Bộ băm từ)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # 2. Tải Model (Bộ não AI)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        print("Đã tải mô hình thành công và sẵn sàng dịch!")

    def translate(self, text: str) -> str:
        # Bước 1: Mã hóa câu tiếng Anh thành các con số (Tensor) để AI có thể hiểu
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        
        # Bước 2: AI bắt đầu suy nghĩ và tạo ra chuỗi số đại diện cho câu tiếng Việt
        outputs = self.model.generate(**inputs, max_length=512)
        
        # Bước 3: Giải mã chuỗi số đó ngược lại thành ngôn ngữ loài người (Tiếng Việt)
        translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return translated_text

# Đoạn code nhỏ dưới đây chỉ để chúng ta test thử xem mô hình có hoạt động không
if __name__ == "__main__":
    # Khởi tạo mô hình
    translator = TranslatorModel()
    
    # Dịch thử một câu
    cau_tieng_anh = "Hello, it is Lab 1 on API,  I am learning how to build an AI API."
    cau_tieng_viet = translator.translate(cau_tieng_anh)
    
    print("\n--- TEST MÔ HÌNH ---")
    print(f"EN: {cau_tieng_anh}")
    print(f"VI: {cau_tieng_viet}")