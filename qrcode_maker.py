import qrcode

img = qrcode.make('https://github.com')
img.save('QRcode.png')