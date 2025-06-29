import os
from tiktok_osint import tiktok_lookup
from whatsapp_osint import wa_check

os.system("clear")
print("""
\033[1;32m╔════════════════════════════╗
║  \033[1;36mTOOLS OSINT - MR.FRIANS     \033[1;32m║
╠════════════════════════════╣
║ 1. TikTok Lookup           ║
║ 2. Cek Nomor WhatsApp      ║
║ 0. Exit                    ║
╚════════════════════════════╝
""")
pil = input("Pilih: ")

if pil == "1":
    user = input("Masukkan username TikTok: ")
    tiktok_lookup(user)
elif pil == "2":
    nomor = input("Masukkan Nomor (cth +628xxx): ")
    wa_check(nomor)
else:
    print("Keluar...")