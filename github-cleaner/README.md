# GitHub Non-Follower Cleaner

Bu araç, seni takip etmeyen kişileri tespit eder ve otomatik olarak takipten çıkarır.

## Kullanım

1. Gerekli kütüphaneleri kur:
   ```bash
   pip install -r requirements.txt
   ```

2. `main.py` dosyasını aç ve:
   - `USERNAME` kısmına kendi kullanıcı adını yaz (hazır: bahattinyunus)
   - `TOKEN` kısmına GitHub Personal Access Token'ını ekle.

3. Ardından programı çalıştır:
   ```bash
   python main.py
   ```

## Token Oluşturma
- GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
- Yeni token oluştur ve **sadece şu izni** ver:
  - `user:follow`
- Token'ı kopyalayıp `main.py` içindeki `TOKEN` değişkenine yapıştır.

Program seni takip etmeyenleri bulur ve otomatik olarak takipten çıkarır.
