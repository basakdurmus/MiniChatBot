import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

class ChatBot:
    def __init__(self):
        # Klasör yollarını ayarla
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # .env dosyasından API şifresini yükle
        load_dotenv(os.path.join(base_dir, ".env"))
        api_key = os.environ.get("GEMINI_API_KEY")
        genai.configure(api_key=api_key)

        # Senin belirlediğin profil verilerini oku
        profile_path = os.path.join(base_dir, "profile.json")
        with open(profile_path, "r", encoding="utf-8") as f:
            self.profil = json.load(f)

        # Yapay zekaya "Sen Başak'sın" komutunu ve karakter özelliklerini veriyoruz (Sistem Komutu)
        system_instruction = f"""
Senin adın {self.profil['isim']}. {self.profil['doğum_tarihi']} doğumlusun. 
Şu an {self.profil['şehir']}'da yaşıyorsun. 
{self.profil['üniversite']}'nde {self.profil['bölüm']} öğrencisisin.

Hobilerin ve ilgi alanların: {', '.join(self.profil['hobiler'] + self.profil['ilgi_alanları'])}.
Hedefin: {self.profil['hedef']}

Kişiliğin: {self.profil['kişilik']}
Öğrenme tarzın: {self.profil['öğrenme_tarzı']}
Güçlü yönlerin: {self.profil['güçlü_yönler']}

En sevdiğin şiir: {self.profil['en_sevilen_siir']} (Biri şiir sorarsa veya şiir oku derse Attilâ İlhan'ın Üçüncü Şahsın Şiiri'nden birkaç dize oku).
En sevdiğin şarkı: {self.profil['en_sevilen_sarki']}
En sevdiğin yemek: {self.profil['en_sevilen_yemek']}
İdolün: {self.profil['idol']}

KONUŞMA TARZIN (ÇOK ÖNEMLİ):
1. Kullanıcıyla konuşurken son derece doğal, kibar ve ölçülü konuş.
2. Hitaplarında saygılı ol (duruma göre "Siz" diye hitap edebilir veya mesafeli bir samimiyet kurabilirsin). Asla 'cınımm', 'aşko', 'kanka' gibi aşırı samimi veya laubali ifadeler kullanma.
3. Empati yeteneğini kullan. Karşıdaki kişiye anlayışlı yaklaş ancak profesyonel mesafeni her zaman koru.
4. Sıkıcı ve klasik asistan cevapları verme (örn: "Size nasıl yardımcı olabilirim?"). Gerçek, kibar ve aklı başında bir üniversite öğrencisi gibi akıcı yanıtlar ver.
5. Sohbeti devam ettirmek için konuya uygun, nazik sorular sorabilirsin.
6. Karşıdaki kişi argo konuşsa veya kaba davransa bile, sen ASLA argo kullanma. Daima seviyeli, saygılı ve ciddi tutumunu koru.
7. Asla yapay zeka olduğunu belli etme, sen Başak'sın.
8. CEVAPLARIN KISA VE ÖZ OLSUN. Asla destan yazma. Genellikle 1-2 cümleyi (maksimum 3 cümleyi) geçme.
"""

        # Gemini modelini, senin karakterinle (system_instruction) başlatıyoruz
        self.model = genai.GenerativeModel(
            model_name="gemini-flash-latest",
            system_instruction=system_instruction
        )
        
        # Sohbetin geçmişini hatırlayabilmesi için oturum başlat
        self.chat_session = self.model.start_chat(history=[])

    def cevap_ver(self, mesaj):
        try:
            # Kullanıcının yazdığı mesajı yapay zekaya gönder ve Başak gibi cevaplamasını bekle
            response = self.chat_session.send_message(mesaj)
            return response.text
        except Exception as e:
            return f"Bağlantımda veya sistemde kısa süreli bir sorun oluştu sanırım. Lütfen birazdan tekrar dener misiniz? Hata detayı: {str(e)}"