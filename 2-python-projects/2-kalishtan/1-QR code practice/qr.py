import pyqrcode
url='https://www.facebook.com/lifelongkiller?mibextid=ZbWKwL'
r=pyqrcode.create(url)
r.svg('Qr.svg',scale=10)