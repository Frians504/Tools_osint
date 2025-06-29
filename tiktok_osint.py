# tiktok_osint.py
import requests

def tiktok_lookup(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    if "tiktok" in res.url:
        print(f"[✓] Username ditemukan: {username}")
        print(f"URL: {res.url}")
    else:
        print("[x] Akun tidak ditemukan atau private.")

# Contoh panggil
# tiktok_lookup("username")