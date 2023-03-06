username="informatika"
password="12345678"

for i in range (3):
    masuk_username=input (" username anda: ")
    masuk_password=input (" password anda: ")

    if masuk_username == username and masuk_password == password:
        print("Berhasil login!")
        break

    else:
        print("Username atau password salah coba lagi")
print()    

if masuk_username !=username and masuk_password != password:
    print("Akun anda diblokir ")