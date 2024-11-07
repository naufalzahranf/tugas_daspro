"""" Nama : Naufal Zahran Fadhlurrohman
    NIM : 2409107
    Kelas : RPL 1B """

def volume_tabung(r,t):
    phi = 3.14
    return phi*r*r*t

r = float(input("Masukan Jari-Jari tabung:"))
t = float(input("Masukan tinggi tabung:"))

volume = volume_tabung(r,t)
print(f"volume tabung adalah {volume} cm")