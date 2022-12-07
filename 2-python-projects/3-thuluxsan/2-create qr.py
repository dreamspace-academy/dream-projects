import pyqrcode
url='https://www.youtube.com/watch?v=hQdqL6RD42Q&list=PLagL21mvvlErbzAQkkIKneqHVWqx1opBp&index=3'
k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)
