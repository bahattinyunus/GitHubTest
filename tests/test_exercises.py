import pathlib


def test_ex1_answer():
    p = pathlib.Path("exercises/01-intro/answer.txt")
    assert p.exists(), "answer.txt bulunamadı. `exercises/01-intro/answer.txt` dosyasını oluşturun."
    content = p.read_text(encoding="utf-8").strip()
    assert content == "Merhaba, GitHub Eğitim!", f"Beklenen içerik 'Merhaba, GitHub Eğitim!' iken bulundu: {content!r}"
