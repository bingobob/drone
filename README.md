# Raspberry Pi Drone Project
Syma drone with Raspberry Zero W and RGB LED
El cheapo syma drone modded with Raspberry pi zero w / Pi Camera v2.1 and monkmakes RGB LED (aka the squid).

![fly-pi](/img/fly_pi.jpg?raw=true "fly-pi")

## Summary

I know a little bit of programming, a little pi, a little electronics and I've put it all together in this project - soldering has been a great skill to learn. It's been a heck of a lot of fun and I'm still working on it. I'd love to hear more from anyone with tips or code comments. This has got to be one of the most enjoyable pi projects I've done and it's inspired me to write this and publish it here - my first github repo.

## Bill of materials

| Items                             | Amazon Link            | Rough Cost |
| --------------------------------- | ---------------------- |       ---: |
| Syma drone - Syma X5SC/X5SC-1     | http://amzn.to/2mC9hP7 | £40        |
| Pi Zero W                         | http://amzn.to/2ngRIYi | £10        |
| Pi Camera v2.1                    | http://amzn.to/2mCuIPO | £20        |
| Monkmakes RGB LED (aka the squid) | http://amzn.to/2mCmebz | £5         |


### Tools

| Items                             | Amazon Link            | Rough Cost |
| --------------------------------- | ---------------------- |       ---: |
| Soldering iron kit                | http://amzn.to/2mC21CQ | £20        |
| Hot Glue gun                      | http://amzn.to/2ngUxbL | £10        |
| Dremel type multi-tool            | http://amzn.to/2ngYbT2 | £20        |


## Method

I've added a Pi Zero, Pi Camera and RGB LED to the drone. everything on the drone is powered from the original drone LIPO battery.

Currently the rough flight sequence is as follows.

1. drone is powered on (by connecting the drone's lipo battery)
2. pi zero boots, as it's fed off the drone's power
3. pi zero launches the drone.py python script (in the repo)
4. drone.py reads config variables in top of file
5. drone.py activates the LEDs to indicate status to pilot
6. Take off
7. After the green light, drone.py actvates video recording for specified time (default 2 mins)
8. LEDs change to indicate video recording finished and photo sequence commencing
9. Photo stage begins and camera takes a sequence of high resolution photos
10. LED indicates python script has finished
11. Pi shutdown command is issued (have disabled this currently)

The Pi is on my home wifi network so after the flight I connect to the pi and SCP the files and videos off it.

## Enhancements

I've got many ideas for how to enhance this project but need to keep in mind weight at all times. I think I'm at the limit of the payload for this drone as it is. However I'd like to investigate the following.

- GPS module, would be great to add altitude figures to the images/videos and perhaps add these to the flight log
- Barometer maybe use this instead of the GPS module, lighter and cheaper although less accurate I believe
- Try the whole thing on a different drone - I beleive the X8C is more powerful
- Add buttons / switches to the pi to allow it to be shutdown elegantly by the user
- Yellow wire - there's a yellow wire running from the syma control board that was used with the original camera, you pressed a function on the remote control unit and it signalled to the camera to start / stop recording or take a photo. I wonder if it would be possible to connect this yellow wire to the Pi GPIO directly and have the remote unit send signals to the Pi, e.g. take a photo, or shutdown.
- Access point, currently the pi zero w is set to connect as a client to my home wifi network, this works well however it might be more useful if I set it up as a wifi access point (a flying one)!
- Airborn wifi network ESSID scanning, could be useful to scan for ESSIDs as the drone flies
- some sort of more automated way to get the photos/ videos off the pi
- maybe a light webserver and interface on the pi to access flight photos/ videos/ data post flight

## drone on the bench

![bench1](/img/bench1.jpg?raw=true "bench1")
![bench2](/img/bench2.jpg?raw=true "bench2")
![bench3](/img/bench3.jpg?raw=true "bench3")
![bench4](/img/bench4.jpg?raw=true "bench4")
![bench5](/img/bench5.jpg?raw=true "bench5")

## drone in flight

![flight_pic1_road.jpg](/img/flight_pic1_road.jpg?raw=true "flight_pic1_road.jpg")
![flight_pic2_football_match.jpg](/img/flight_pic2_football_match.jpg?raw=true "flight_pic2_football_match.jpg")
![flying.jpg](/img/flying.jpg?raw=true "flying.jpg")
