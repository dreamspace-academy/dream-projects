import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,20,10])
datas=["Mobile","TV","Dress","Doll"]


plt.pie(y, labels=datas,shadow=True)
plt.show()