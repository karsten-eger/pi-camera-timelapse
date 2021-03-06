#!/usr/bin/env python3

# [START includes]
from subprocess import check_output
from re import findall
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from video_stitcher import stitch_video
from timestamper import write_timestamps
import argparse
from datetime import datetime
import time
import picamera
import sys
import os
import logging
from shutil import copyfile

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

__output_folder_name__= sys.argv[5] + '/output'

def clean_directory():
    os.system('rm -f '+__output_folder_name__+'/*.jpg')

def capture_images(length_in_seconds,interval_in_seconds):
    count = length_in_seconds / interval_in_seconds
    logging.info('Taking {} shots...'.format(count))
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        for filename in camera.capture_continuous(__output_folder_name__+'/img{counter:06d}.jpg'):
            copyfile(filename, '/home/pi/camera/snap.jpg')
            time.sleep(interval_in_seconds) # wait <interval_in_seconds> seconds
            count -= 1
            if count <= 0:
                break

# [START]
def main():
    # Start with cleanup
    start_time = time.time()
    if not os.path.exists(__output_folder_name__):
        os.makedirs(__output_folder_name__)
    logging.info('Running clean script...')
    clean_directory()

    # Take pictures
    logging.info('Opening camera...')
    capture_images(int(sys.argv[1]),int(sys.argv[2]))
    logging.info('Writing timestamps...')

    # Write timestamps to images
    if int(sys.argv[3]) == 1:
        logging.info('Writing timestamps and resizing images')
        write_timestamps(72,32,__output_folder_name__)
        logging.info('Captured images {} seconds to run'.format(str(time.time() - start_time)))
    else:
        logging.info('resizing and timestamps skipped')
    # Create video
    if int(sys.argv[4]) == 1:
        logging.info('Making video...')
        timestamp = str(datetime.now().strftime('%Y-%m-%d_%H%M%S'))
        if int(sys.argv[3]) == 1:
            logging.info('using resized images with timestamp')
            stitch_video('timelapse_'+timestamp+'.mp4','warning',__output_folder_name__,'video','img%06d-resized.jpg')
        else:
            logging.info('using full size, no timestamp')
            stitch_video('timelapse_'+timestamp+'.mp4','warning',__output_folder_name__,'video','img%06d.jpg')
    else:
        logging.info('video creation skipped')
    logging.info('Done!')
    logging.info('Creating video {} seconds to run'.format(str(time.time() - start_time)))
if __name__ == '__main__':
    main()
