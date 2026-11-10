import json

def load_rules():
    with open("Aturan.json", "r", encoding="utf-8") as file:
        return json.load(file) 

def forward_chaining(fakta_awal, aturan):
    fakta = fakta_awal.copy()
    kesimpulan = []

    berubah = True

    ## bagian forward chainingnya
    while berubah:
        berubah = False

        for rule in aturan:
            kondisi = rule["jika"]
            mode = rule["mode"]

            if mode == "dan":
                terpenuhi = all(k in fakta for k in kondisi)
            else:
                terpenuhi = any(k in fakta for k in kondisi)

            if terpenuhi and rule["maka"] not in fakta:
                hasil = rule["maka"]

                fakta.append(hasil)
                kesimpulan.append({
                    "id": rule["id"],
                    "hasil": hasil
                })

                berubah = True

    return kesimpulan


data = load_rules()

print("=" * 50)
print("SISTEM PAKAR UNTUK MENDIAGNOSA GANGGUAN WIFI")
print("=" * 50)

print("\nBatas Keberlakuan:")
print(data["batas"])

print("\nFakta yang tersedia:")
print("1. perangkat tersambung ke WiFi")
print("2. tidak ada akses internet")
print("3. perangkat tidak bisa mengakses internet")
print("4. perangkat lain bisa terhubung ke WiFi")
print("5. indikator WiFi tidak muncul")
print("6. bar sinyal WiFi kosong")
print("7. perangkat jauh dari router")
print("8. router belum direstart")

print("\nMasukkan nomor fakta.")
print("Ketik 0 jika selesai.")

fakta_awal = []

while True:
    pilihan = input("Pilih fakta: ")

    if pilihan == "0":
        break

    fakta_tersedia = {
        "1": "perangkat tersambung ke WiFi",
        "2": "tidak ada akses internet",
        "3": "perangkat tidak bisa mengakses internet",
        "4": "perangkat lain bisa terhubung ke WiFi",
        "5": "indikator WiFi tidak muncul",
        "6": "bar sinyal WiFi kosong",
        "7": "perangkat jauh dari router",
        "8": "router belum direstart"
    }

    if pilihan in fakta_tersedia:
        fakta = fakta_tersedia[pilihan]

        if fakta not in fakta_awal:
            fakta_awal.append(fakta)

        print("Fakta ditambahkan:", fakta)
    else:
        print("Pilihan tidak tersedia.")

hasil = forward_chaining(fakta_awal, data["aturan"])

print("\n" + "=" * 50)
print("HASIL DIAGNOSIS")
print("=" * 50)

if hasil:
    for item in hasil:
        print(f'{item["id"]} -> {item["hasil"]}')
else:
    print("Tidak ditemukan kesimpulan berdasarkan aturan yang tersedia.")