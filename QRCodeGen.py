import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=15,
    border=1
)

qr.add_data('https://9e-docteur.github.io/qrcodelandingpage/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')