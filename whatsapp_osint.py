# whatsapp_osint.py
import phonenumbers
from phonenumbers import geocoder, carrier

def wa_check(number):
    nomor = phonenumbers.parse(number)
    print("Lokasi:", geocoder.description_for_number(nomor, "id"))
    print("Provider:", carrier.name_for_number(nomor, "id"))

# Contoh panggil
# wa_check("+6281234567890")