#import the necessary modules
import subprocess
import picamera 
import time
from twython import Twython
	

choice = raw_input("Would you like to take a photo? y/n: ").lower()


if choice == "y":
	#create a timestamped filename and append to a user chosen name
	filename = (time.strftime("%d-%m-%y %H:%M:%S ") + raw_input("Give the file a name:")+ ".jpg")

	print "Taking photo: %s" % filename
	
	#take the photoe
	camera = picamera.PiCamera()
	camera.capture(filename)

	#choice3 = raw_input("Do you want to tweet the image? y/n: ").lower()
	
	#if choice3 == "y":
	#	
	#	#load the config file
	#	config = {}
	#	execfile("twit_conf.py", config)
	#
	#	#create Twitter API object
	#	twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])
	#	
	#	message = raw_input("What is your message? ",)
	#	
	#	photo = open(filename, 'rb') 
	#	response = twitter.upload_media(media = photo)
	#	
	#	print "Tweeting images and message"
	#
	#	twitter.update_status(status = message, media_ids=[response['media_id']])


#choice1 = raw_input("Would you like to take a video? y/n: ").lower()


#if choice1 == "y":
#	filename2 = (time.strftime("%d-%m-%y %H:%M:%S ") + raw_input("Give the file a name:")+ ".h264")
#	rec_time = int(raw_input("How many seconds of footage?"))
#	
#	print "Recording %s second video: %s" % (rec_time, filename2)
#	camera.start_recording(filename2)
#	sleep(rec_time)
#	camera.stop_recording()

if choice == "y":
	print "Uploading image to dropbox"
	subprocess.check_call(["/home/pi/DropBox/Dropbox-Uploader/dropbox_uploader.sh"," upload ", filename, "/myDir"])
	print "Upload successful"
	print "Removing image file - %s from local folder" %filename
	subprocess.check_call(["sudo","rm",filename])
	print "Image file removed"

#if choice1 == "y":
#	print "Uploading video to dropbox"
#	subprocess.check_call(["./dropbox_uploader.sh"," upload ", filename2, "/myDir"])
#	print "Upload successful"
#	print "Removing video file - %s from local folder" %filename2
#	subprocess.check_call(["sudo","rm", filename2])
#	print "Video file removed"


