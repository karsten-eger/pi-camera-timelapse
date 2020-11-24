# pi-camera-timelapse

Forked from 
https://github.com/aawobdev/pi-camera-timelapse


Heavily inspired by:
* Armin Hinterwirth (https://github.com/amphioxus) - https://www.amphioxus.org/content/timelapse-time-stamp-overlay

## Click to view Video below
[![PiCam Timelapse](https://i9.ytimg.com/vi/auIuiP3BAKg/mq3.jpg?sqp=CID0sPgF&rs=AOn4CLDYb8buEuuwAdGCJPEfYO4Z-TcCuQ)](https://youtu.be/auIuiP3BAKg)

## Some helpful Python scripts for achieving a timelapse with your Rapsberry Pi Camera

```timelapse.py``` is the main script

### Dependencies on 
* ```video_stitcher.py``` 
* ```timestamper.py```
### Python lib dependencies are:
* ffmpeg (usually comes with Pi OS)
* Pillow (aka PIL, also should ship with Pi)
### Font dependencies
* /usr/share/fonts/truetype/freefont/FreeMono.ttf

## Steps
* Initial Images will be outputted to ```imgXXXXXX.jpg``` inside the ```output``` folder
* If wanted: Next, timestamps are drawn onto the images, they're stored as ```imgXXXXXX-resized.jpg```
* If wanted: Finally the images (depending on if you chose to create the timestamp images, ```imgXXXXXX-resized.jpg``` or ```imgXXXXXX.jpg``` are used) are stitched into a video inside ```output/video``` folder as ```timelapse_YYYY-MM-DD_HHmmSS.mp4```
* Modify ```main()``` inside ```timelapse.py``` to use what you need

## Usage examples
```
python3 timelapse.py [length in seconds] [interval in seconds] [boolean 1/0 if resizing wanted] [boolean 1/0 if video creation wanted] [directory to output]
```

### Example 1) Run for 1 hour with 1 minute intervals, output to /home/pi/Camera
```
python3 timelapse.py 3600 60 1 1 /home/pi/Camera
```

### Example 2) Run for 8 hours with 1 hour intervals, output to /home/pi/Camera
```
python3 timelapse.py 28800 3600 1 1 /home/pi/Camera
```

### Example 3) Run for 1 minute with 1 second intervals, output to /home/pi/Camera
```
python3 timelapse.py 60 1 1 1 /home/pi/Camera
```

### Example 4) Run for 1 minute with 1 second intervals, do not resize, create video, output to /home/pi/Camera
```
python3 timelapse.py 60 1 0 1 /home/pi/Camera
```

### Example 5) Run for 1 minute with 1 second intervals, do not resize, do not create video, output to /home/pi/Camera
```
python3 timelapse.py 60 1 0 0 /home/pi/Camera
```

### Example 6) Run for 1 minute with 1 second intervals, do resize, do not create video, output to /home/pi/Camera
```
python3 timelapse.py 60 1 1 0 /home/pi/Camera
```


## Run in background

### Example 7) Will do the following:
* Run as cronjob for 1 minute with 1 second intervals
* Output images and video to /home/pi/Camera
* Run at 4AM every morning
* Output the Logs to a file inside my Camera folder

#### Open cron config
```
crontab -e
```
#### Add line to the end of the file
```
0 4 * * * python3 /home/pi/Camera/timelapse.py 60 1 1 1 /home/pi/Camera >> /home/pi/Camera/output.log 2>$
```
#### CTRL+X and 'y' to confirm saved changes

## Some helpful links
* https://crontab.guru/
* https://www.raspberrypi.org/documentation/usage/camera/raspicam/
* https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
* https://picamera.readthedocs.io/en/release-1.10/api_camera.html
