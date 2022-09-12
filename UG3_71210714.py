teks_user = input("Masukkan sebuah teks: ")
cari_kata = input("Masukkan kata yang ingin anda hitung: ")

pisah_kata = teks_user.lower().split(" ")

jml_huruf = 0

for kata in pisah_kata:
    if kata == cari_kata:
        jml_huruf += 1
    
print(jml_huruf)

