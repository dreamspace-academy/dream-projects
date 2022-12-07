from PIL import Image

s=Image.open('sai.jpg')
a=s.convert('L')
a.save('bnd.jpg')
s.show()
a.show()