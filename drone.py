from squid import *
import time
import picamera
import os

rgb = Squid(18, 23, 24)

# CONFIG
###########################
VIDEO_TIME = 60
NUMBER_OF_PICS = 10
TIME_BETWEEN = 7
###########################

import logging
logger = logging.getLogger('myapp')
timestr = time.strftime("%Y%m%d-%H%M%S")
hdlr = logging.FileHandler('/home/pi/logs/drone_log_%s.log'%(timestr), mode='w')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

def flasher(colour1=RED,colour2=BLUE,runtime=10,delay=0.2):
  t_end = time.time() + runtime
  while time.time() < t_end:
    rgb.set_color(colour1)
    time.sleep(delay)
    rgb.set_color(colour2)
    time.sleep(delay)

# main program
logger.info('*****************')
logger.info('Program starting')

logger.info('VIDEO_TIME %s'%(VIDEO_TIME))
logger.info('NUMBER_OF_PICS %s'%(NUMBER_OF_PICS))
logger.info('TIME_BETWEEN %s'%(TIME_BETWEEN))

logger.info('*****************')


logger.info('Red')
rgb.set_color(RED)
time.sleep(5)
logger.info('Blue')
rgb.set_color(BLUE)
time.sleep(5)
logger.info('Green')
rgb.set_color(GREEN)


logger.info('=========================')


logger.info('recording video for %s seconds'%(VIDEO_TIME))
logger.info('Start video recording')

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (1920, 1080)
#camera.resolution = (1280, 720)
timestr = time.strftime("%Y%m%d-%H%M%S")
camera.start_recording('/home/pi/video/my_video_%s.h264'%(timestr))
time.sleep(VIDEO_TIME)
# camera.wait_recording(VIDEO_TIME)
camera.stop_recording()

logger.info('Stop video recording')

# end video recording
flasher(BLUE,WHITE,10,0.2)


camera.resolution = (3280, 2464)
camera.rotation = 180

logger.info('=========================')

logger.info('Start photo recording')
logger.info('recording %s pics'%(NUMBER_OF_PICS) + ' with %s seconds gaps'%(TIME_BETWEEN))

frameCount = 0
while frameCount < NUMBER_OF_PICS:
    imageNumber = str(frameCount).zfill(7)
    stamp_string = '_' + time.strftime("%Y%m%d-%H%M%S") + '_' + imageNumber
    camera.capture('/home/pi/photo/image%s.jpg'%(stamp_string))
    logger.info('photo recorded to /home/pi/photo/image%s.jpg'%(stamp_string))
    frameCount += 1
    time.sleep(TIME_BETWEEN)

logger.info('Stop photo recording')

logger.info('=========================')

# end video recording
flasher(RED,GREEN,20,0.2)

logger.info('Program end')
logger.info('')

# Shutdown
logger.info('Shutting down pi - disabled')
logger.info('*****************')


# os.system('sudo shutdown now -h')
