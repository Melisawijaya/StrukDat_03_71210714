teks_user = input("Masukkan sebuah teks: ")
cari_kata = input("Masukkan kata yang ingin anda hitung: ")

jml_kata = 0
teks_user = teks_user.lower()
pisah_kata = teks_user.split(" ")
cari_kata = cari_kata.lower()

for kata in pisah_kata:
    if kata == cari_kata:
        jml_kata += 1
    
print(jml_kata)

