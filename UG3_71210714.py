teks_user = input("Masukkan sebuah teks: ")
cari_kata = input("Masukkan kata yang ingin anda hitung: ")

pisah_kata = teks_user.lower().split(" ")
cari_kata = cari_kata.lower()

jml_kata = 0

for kata in pisah_kata:
    if kata == cari_kata:
        jml_kata += 1
    
print(jml_kata)

