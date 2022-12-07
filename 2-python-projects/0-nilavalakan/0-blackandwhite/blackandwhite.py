from PIL import Image

k=Image.open('flower.jpg')
b=k.convert('L')
b.save('bandw.jpg')
k.show()
b.show()