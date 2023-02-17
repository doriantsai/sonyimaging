#! /usr/bin/env python3

import os
import subprocess
import gphoto2 as gp
from datetime import datetime
import time


camera = gp.Camera()
camera.init()

file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))

dt = datetime.now().strftime("%Y%m%d_%H%M%S")
targetname = dt + '.jpg'

target = os.path.join('/home/agkelpie/Code/sonyimaging', targetname)
print('Copying image to', target)

camera_file = camera.file_get(
    file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
camera_file.save(os.path.join(target))

camera.exit()

print('Done')

import code
code.interact(local=dict(globals(), **locals())) 