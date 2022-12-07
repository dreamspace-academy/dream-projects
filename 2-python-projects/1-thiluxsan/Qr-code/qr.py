import pyqrcode
url='https://www.youtube.com/watch?v=hQdqL6RD42Q&list=PLagL21mvvlErbzAQkkIKneqHVWqx1opBp&index=3'
r=pyqrcode.create(url)
r.svg('Qr.svg',scale=10)