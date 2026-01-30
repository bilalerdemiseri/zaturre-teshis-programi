import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import tensorflow as tf
import numpy as np
import os
import sys

# Görünüm Ayarları
ctk.set_appearance_mode("Dark")  # Karanlık Mod
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🫁 Zatürre Teşhis Destek Sistemi")
        self.geometry("500x600")
        self.resizable(False, False)  # Pencereyi büyütülemez yap

        # Model dosyasının yolunu belirle (exe içinde ve normal çalıştırmada çalışması için)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        model_path = os.path.join(base_path, 'best_model.keras')
        
        # Model Yükleme (DenseNet121 projenizden gelen model)
        self.model = tf.keras.models.load_model(model_path)

        # Arayüz Elemanları
        self.label = ctk.CTkLabel(self, text="Zatürre Teşhis Paneli", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        self.image_label = ctk.CTkLabel(self, text="Henüz bir görüntü seçilmedi", width=300, height=300, fg_color="gray20", corner_radius=10)
        self.image_label.pack(pady=10)

        self.upload_btn = ctk.CTkButton(self, text="Röntgen Fotoğrafı Seç", command=self.upload_image)
        self.upload_btn.pack(pady=20)

        self.result_text = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16))
        self.result_text.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                # 1. Önizleme göster
                my_image = ctk.CTkImage(light_image=Image.open(file_path), size=(300, 300))
                self.image_label.configure(image=my_image, text="")
                
                # 2. "Analiz ediliyor..." mesajı ver (Arayüz donmuş gibi görünmesin)
                self.result_text.configure(text="⏳ Analiz ediliyor, lütfen bekleyin...", text_color="white")
                self.update() # Arayüzü hemen güncelle

                # 3. Görüntü Ön İşleme
                img = Image.open(file_path).convert('RGB').resize((224, 224))
                img_array = np.array(img) / 255.0
                img_array = np.expand_dims(img_array, axis=0)
                
                # 4. Tahmin Süreci (Burası biraz vakit alabilir)
                preds = self.model.predict(img_array, verbose=0)
                prediction = float(preds[0][0]) 
                
                # 5. Sonucu Yazdır
                if prediction > 0.5:
                    self.result_text.configure(text=f"⚠️ Zatürre Belirtisi: %{prediction*100:.2f}", text_color="#FF5555")
                else:
                    self.result_text.configure(text=f"✅ Normal: %{(1-prediction)*100:.2f}", text_color="#55FF55")
            
            except Exception as e:
                # Bir hata olursa konsol yerine ekranda göster ki sorunu anlayalım
                self.result_text.configure(text=f"❌ Hata oluştu: {str(e)}", text_color="orange")

if __name__ == "__main__":
    app = App()
    app.mainloop()