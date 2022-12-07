import pyscreenshot as sc
import time



time.sleep(6)
n = sc.grab()
n.save('sample-shot.png')
n.show()
