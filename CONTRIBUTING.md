# Contributing

Teşekkürler! Bu depo eğitim amaçlıdır; katkılar, öğretim materyali ve hata düzeltmeleri memnuniyetle karşılanır.

Yerel geliştirme ve test çalıştırma:

PowerShell (Windows):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
python -m pytest -q
```

Linux / macOS (bash):

```bash
python -m venv .venv; source .venv/bin/activate; pip install -r requirements.txt
pytest -q
```

Alıştırma ekleme yönergeleri (öğretmenler):
- Yeni bir klasör `exercises/NN-name/` oluşturun.
- İçine `README.md` (talimatlar) ve `starter.txt` veya gerekli başlangıç dosyalarını koyun.
- `tests/` içine test ekleyin veya mevcut testleri genişletin.

Öğrenciler için kısa not:
- Her alıştırma kendi klasöründe `answer.txt` veya istenen çözümü oluşturmalıdır.
- Değişiklik yapınca `pytest` ile testleri çalıştırın.

Lisans ve kod davranışı için `LICENSE` ve `CODE_OF_CONDUCT.md` dosyalarına bakın.
Katkıda bulunma
================

Teşekkürler! Bu repo eğitim amaçlıdır. Aşağıda hem öğrenciler hem de katkıda bulunanlar için kısa yönergeler var.

Öğrenciler
- Depoyu klonlayın ve bir dal (branch) oluşturun: `git checkout -b ogrenci/<ad>`
- `exercises/` içindeki alıştırmaları takip edin.
- Değişiklikleri yerelde test edin: `pip install -r requirements.txt` ve `pytest`.
- Değişikliklerinizi push edin ve bir Pull Request oluşturun.

Öğretmenler / Eğitmenler
- Bu repoyu ders materyali olarak kopyalayabilir veya GitHub Classroom ile bağlantılandırabilirsiniz.
- Yeni alıştırma eklerken `tests/` içine uygun pytest testleri ekleyin.

Stil
- Türkçe açıklamalar kullanın.
- Basit ve öğretici olsun: çözümler açıkça test edilebilir olmalı.

Geri bildirim
- Lütfen issue açarak geri bildirim verin veya ders içeriğini geliştirme teklifinde bulunun.
