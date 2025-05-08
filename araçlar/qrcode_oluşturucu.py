import qrcode

# Kullanıcıdan link al
url = input("Lütfen QR kod oluşturmak istediğiniz linki girin: ")

# QR kod oluşturma
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Görseli kaydet
img = qrcode.make(url)
img.save("dynamic_qr.png")

print(f"QR kod oluşturuldu: dynamic_qr.png")