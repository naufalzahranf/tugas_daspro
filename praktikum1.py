"""" Nama : Naufal Zahran Fadhlurrohman
    NIM : 2409107
    Kelas : RPL 1B """

def volume_tabung(r, t):
    phi = 3.14
    if r <= 0 or t <= 0:
        return "Error: Jari-jari dan tinggi tabung harus bernilai positif."
    return phi * r * r * t

r = float(input("Masukkan Jari-Jari tabung (cm): "))
t = float(input("Masukkan Tinggi tabung (cm): "))

if r > 0 and t > 0:
    volume = volume_tabung(r, t)
    print(f"Volume tabung adalah {volume:.2f} cm³")
else:
    print("Error: Jari-jari dan tinggi tabung harus bernilai positif.")