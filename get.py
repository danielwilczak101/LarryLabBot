import urllib.request
import json
import numpy as np
import matplotlib.pyplot as plt

with urllib.request.urlopen("http://192.168.1.140:4000//camera") as url:
    data = json.loads(url.read().decode())

photo = np.array(data)


plt.imshow(photo)
plt.show()
