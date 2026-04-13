# Khai báo thư viện AI Hugging Face.
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class TranslatorModel:
    def __init__(self):
        # Khởi tạo bộ đọc và não AI.
        model_name = "Helsinki-NLP/opus-mt-en-vi"
        print(f"Đang tải mô hình {model_name}...")
        print("(Quá trình này có thể mất vài phút cho lần chạy đầu tiên để tải data về máy)")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        print("Đã tải mô hình thành công và sẵn sàng dịch!")

    def translate(self, text: str) -> str:
        # Mã hóa, dịch và giải mã văn bản.
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        outputs = self.model.generate(**inputs, max_length=512)
        
        translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated_text

# Chạy thử nghiệm mô hình cục bộ.
if __name__ == "__main__":
    translator = TranslatorModel()
    cau_tieng_anh = "Hello, it is Lab 1 on API,  I am learning how to build an AI API."
    
    cau_tieng_viet = translator.translate(cau_tieng_anh)
    print("\n--- TEST MÔ HÌNH ---")
    print(f"EN: {cau_tieng_anh}")
    print(f"VI: {cau_tieng_viet}")