
import urllib.request
import json
import numpy as np

with urllib.request.urlopen("http://192.168.1.140:4000/camera") as url:
    data = json.loads(url.read().decode())

new = np.array(data)

print(new.shape)
