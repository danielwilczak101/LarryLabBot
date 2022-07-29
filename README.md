# LarryLabBot V2
EPPL larry the lab bot. Fun project for driving a small bot inside the lab.

#### Start up commands
Connect to the pi once powered on.
```bash
ssh-keygen -R raspberrypi.local // Remove old pi connection from pc
ssh pi@raspberrypi.local // connect to one and old raspberry pi on local
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

![](https://raw.githubusercontent.com/danielwilczak101/LarryLabBot/media/images/IMG_3665.JPG)
![](https://raw.githubusercontent.com/danielwilczak101/LarryLabBot/media/images/IMG_3664.JPG)

# LarryLabBot V1
![](https://raw.githubusercontent.com/danielwilczak101/LarryLabBot/media/images/IMG_3472.jpg)
![](https://raw.githubusercontent.com/danielwilczak101/LarryLabBot/media/images/IMG_3473.jpg)

