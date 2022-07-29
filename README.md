# Larry The Lab Bot
Larry got new mecanum wheels and a 8BitDo SN30 controller to control all of his movements. The website looks funny because of all the movements he can now do.

![](https://github.com/danielwilczak101/LarryLabBot/blob/media/images/LarryV4.jpg)

YOUTUBE VIDEO

## Start up commands
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


