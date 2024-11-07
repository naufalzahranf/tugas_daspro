def hitung_total_dan_rata_rata(*angka):
    if len(angka) == 0:
        return "Tidak ada angka yang dimasukkan."

    total = 0
    for indeks in range(len(angka)):
        nilai = angka[indeks]
        total += nilai
        if indeks == 0:
            print(f"{nilai}", end="")
        else:
            print(f" + {nilai}", end="")
    print(f" = {total}")

    # Perhitungan rata-rata
    rata_rata = total / len(angka)
    print(f"Rata-rata = {total} / {len(angka)} = {rata_rata}")
    
    return total, rata_rata

jumlah_angka = int(input("Berapa jumlah angka yang akan Anda masukkan? "))

# Membuat list untuk menyimpan angka-angka yang diinputkan
daftar_angka = []
for i in range(jumlah_angka):   
    angka = int(input(f"Masukkan angka ke-{i + 1}: "))
    daftar_angka.append(angka)

# Memanggil fungsi dengan angka yang diinputkan
total, rata_rata = hitung_total_dan_rata_rata(*daftar_angka)

