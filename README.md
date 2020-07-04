# pi-camera-timelapse

## Some helpful Python scripts for achieving a timelapse with your Rapsberry Pi Camera

### ```timelapse.py``` is the main script
### Dependencies on ```video_stitcher.py``` and ```timestamper.py```
### Python lib dependencies are:
* ffmpeg (usually comes with Pi OS)
* Pillow (aka PIL, also should ship with Pi)
### Font dependencies
* /usr/share/fonts/truetype/freefont/FreeMono.ttf

### Initial Images will be outputted to imgXXXXXX.jpg inside the output folder
### Next, timestamps are drawn onto the images, they're stored as imgXXXXXX-resized.jpg
### Finally the imgXXXXXX-resized.jpg images are stitched into a video inside output/video folder as timelapse_YYYY-MM-DD_HHmmSS.mp4
### Modify main() inside timelapse.py to use what you need

## Usage examples
```
python3 timelapse.py [length in seconds] [interval in seconds] [directory to output]
```

### Example 1) Run for 1 hour with 1 minute intervals, output to /home/pi/Camera
```
python3 timelapse.py 3600 60 /home/pi/Camera
```

### Example 2) Run for 8 hours with 1 hour intervals, output to /home/pi/Camera
```
python3 timelapse.py 28800 3600 /home/pi/Camera
```

### Example 3) Run for 1 minute with 1 second intervals, output to /home/pi/Camera
```
python3 timelapse.py 60 1 /home/pi/Camera
```
