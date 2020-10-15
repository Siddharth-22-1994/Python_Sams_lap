from PIL import Image
from pyzbar.pyzbar import decode
import pyqrcode

# To create QR Code
qr = pyqrcode.create('http://127.0.0.1:8000/')
qr.png('greet.png', scale=10)


# To read QR Code
d = decode(Image.open('greet.png'))
print(d[0].data.decode('ascii'))
