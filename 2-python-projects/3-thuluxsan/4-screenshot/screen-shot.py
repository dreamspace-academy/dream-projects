import pyscreenshot as sc
import time
time.sleep(5)

k=sc.grab()

k.save('sample-screenshot.png')

k.show()