from PIL import Image

k=Image.open('flo.jpg')
b=k.convert('L')
b.save('Bandw.jpg')
k.show()
b.show()