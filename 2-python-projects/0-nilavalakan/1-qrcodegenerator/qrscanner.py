import pyqrcode
url='https://thedreamshub.com/'
n=pyqrcode.create(url)
n.svg('Qr.svg',scale=10)