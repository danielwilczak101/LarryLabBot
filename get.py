
import requests
import json
import numpy as np

resp = requests.get('http://192.168.1.140:4000/camera')
data = resp.json()

decodedArrays = json.loads(data)

finalNumpyArray = np.asarray(decodedArrays["array"])

print(finalNumpyArray.shape)
