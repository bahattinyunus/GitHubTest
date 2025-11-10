import requests
import time

# ===============================
#  AYARLAR
# ===============================
USERNAME = "bahattinyunus"   # GitHub kullanıcı adın
TOKEN = ""                   # Buraya GitHub Personal Access Token'ını yaz

# ===============================
#  YARDIMCI FONKSİYONLAR
# ===============================
def get_all(url):
    users = []
    page = 1
    while True:
        res = requests.get(
            f"{url}?per_page=100&page={page}",
            headers={"Authorization": f"token {TOKEN}"}
        )
        if res.status_code != 200:
            print(f"Hata: {res.status_code} {res.text}")
            break
        data = res.json()
        if not data:
            break
        users.extend(data)
        page += 1
    return [u["login"] for u in users]

def unfollow(user):
    res = requests.delete(
        f"https://api.github.com/user/following/{user}",
        headers={"Authorization": f"token {TOKEN}"}
    )
    if res.status_code == 204:
        print(f"🚫 Takipten çıkıldı: {user}")
    elif res.status_code == 404:
        print(f"⚠️ {user} bulunamadı (zaten takip etmiyor olabilirsin).")
    else:
        print(f"❌ Hata: {user} ({res.status_code})")

# ===============================
#  ANA AKIŞ
# ===============================
print("Takip edilenler çekiliyor...")
following = get_all(f"https://api.github.com/users/{USERNAME}/following")

print("Takipçiler çekiliyor...")
followers = get_all(f"https://api.github.com/users/{USERNAME}/followers")

nonfollowers = [u for u in following if u not in followers]
print(f"\nSeni takip etmeyen {len(nonfollowers)} kişi bulundu.\n")

for user in nonfollowers:
    unfollow(user)
    time.sleep(1)  # GitHub API rate limitini aşmamak için bekle

print("\n✅ İşlem tamamlandı.")
