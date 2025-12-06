# GitHub Eğitim - GitHubTest

Bu depo, GitHub üzerinde eğitim ve alıştırma (classroom-style) amaçlı kullanılmak üzere hazırlanmıştır.

İçerik
- `exercises/` - Ders alıştırmaları ve başlangıç dosyaları
- `tests/` - Alıştırmaları doğrulayan basit pytest testleri
- `SYLLABUS.md` - Ders akışı ve hedefler

Hızlı başlangıç (yerel)
- Python 3.8+ yüklü olduğundan emin olun.
- Sanal ortam oluşturun ve bağımlılıkları yükleyin:

PowerShell:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
pytest -q
```

Linux / macOS (bash):

```bash
python -m venv .venv; source .venv/bin/activate; pip install -r requirements.txt
pytest -q
```

Nasıl kullanılır (öğrenciler)
- `exercises/01-intro/README.md` içindeki talimatları takip edin ve belirtilen dosyaları oluşturun.
- Değişikliklerinizi test etmek için `pytest` çalıştırın.

Nasıl kullanılır (öğretmenler)
- Bu depoyu bir ödev şablonu olarak kopyalayın veya GitHub Classroom/Assignments ile kullanın.
- `.github/workflows/ci.yml` dosyası testleri otomatik çalıştırır.

İleriye dönük
- Yeni alıştırmalar eklenecek. Repo basit ve öğretici kalacak şekilde tasarlandı.

---

Bu README kısa bir başlangıçtır; daha fazla yönerge için `CONTRIBUTING.md` ve `SYLLABUS.md` dosyalarına bakın.

## Kullanım — Hızlı Komutlar

Aşağıdaki komutlar Windows PowerShell'de (önerilen) çalışır. Bu adımlar, yerelde testleri çalıştırmak ve alıştırmaları doğrulamak içindir.

PowerShell:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
python -m pytest -q
```

Alternatif (bash):

```bash
python -m venv .venv; source .venv/bin/activate; pip install -r requirements.txt
pytest -q
```

Notlar:
- Her alıştırma `exercises/NN-name/` içinde yer alır. Öğrenciler genellikle `answer.txt` gibi istenen dosyayı oluşturup içerisine isteneni yazarlar.
- Testler `tests/` klasöründe toplanmıştır; hata mesajları test çıkışında açıklayıcı olacak şekilde tasarlanmıştır.
