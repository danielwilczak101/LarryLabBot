# Larry The Lab Bot
Larry got new mecanum wheels and a 8BitDo SN30 controller to control all of his movements. The website looks funny because of all the movements he can now do.  

https://www.youtube.com/embed/S1lelsa4xNU

![](https://raw.githubusercontent.com/danielwilczak101/LarryLabBot/media/images/larryv4_cleaned_up.jpg)


#### Website:
All controls go through the website so that you dont need any fance gui or controllers. If it works on your pc's browser then you can control larry. The best is when two people fight over control. Since it's on the browser this is possible.

<p align="center"> 
  <kbd>
    <img width="460" height="400"
    src="https://github.com/danielwilczak101/LarryLabBot/blob/media/images/websiteV4.png">
  </kbd>
</p>


#### Features:
  - Website for controls
  - 8BitDo SN30
  - Grab images using API call's
    ```Python
    import urllib.request
    import json
    import numpy as np
    import matplotlib.pyplot as plt

    with urllib.request.urlopen("http://192.168.1.140:4000/camera") as url:
        data = json.loads(url.read().decode())

    photo = np.array(data)


    plt.imshow(photo)
    plt.show()
    ```

## Start up commands
Connect to the pi once powered on.
```bash
ssh-keygen -R raspberrypi.local // Remove old pi connection from pc
ssh pi@raspberrypi.local // connect to local raspberry pi because i'm to lazy to look up the I.P
```
Move to the code directory.
```bash
cd Desktop/LarryLabBot/
```

Run one of the two options.
```bash
gunicorn -w 1 -b 0.0.0.0:4000 app:app // Not detached
gunicorn -w 1 -b 0.0.0.0:4000 app:app -D --log-file=gunicorn.log // Detached
```

# Larry's Long History:

## Larry Version3
Larry took over an old JetBot frame that I built a while back with the jetson nano that would always blow up and the drivers for all the software was garbage.


![](https://github.com/danielwilczak101/LarryLabBot/blob/media/images/larryv3.jpg)

# LarryLabBot V2
Larry got some new wheels and a new frame.

![](https://raw.githubusercontent.com/danielwilczak101/LarryLabBot/media/images/IMG_3665.JPG)


# LarryLabBot V1
OG LARRY from when we started.

![](https://raw.githubusercontent.com/danielwilczak101/LarryLabBot/media/images/IMG_3472.jpg)


