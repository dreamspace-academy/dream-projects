from PIL import Image

x=Image.open('krish.jpg')
n=x.convert('L')
n.save('bnd.jpg')
x.show()
n.show()