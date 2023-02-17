#! /usr/bin/env python3

"""_summary_
set configuration using gphoto2
"""

import os
import subprocess
import gphoto2 as gp
from datetime import datetime
import time


camera = gp.Camera()
camera.init()

# get camera abilities
abilities = camera.get_abilities()

# set iso
config = camera.get_config()
OK, iso_config = gp.gp_widget_get_child_by_name(config, 'iso')
if OK >= gp.GP_OK:
    iso = iso_config.get_value()
    print(f'iso currently: {iso}')
    # iso_range = iso_config.get_range()
    # print(f'iso range: {iso_range}')
    iso_set = str(200)
    iso_config.set_value(iso_set)
    iso_now = iso_config.get_value()
    # set the config
    print(f'iso set: {iso_now}')
    # apply config to camera
    camera.set_config(config)

# set shutterspeed
config = camera.get_config()
OK, speed_config = gp.gp_widget_get_child_by_name(config, 'shutterspeed')
if OK >= gp.GP_OK:
    shutterspeed = speed_config.get_value()
    print(f'shutterspeed currently: {shutterspeed}')
    shutterspeed_set = "1/10"
    speed_config.set_value(shutterspeed_set)
    shutterspeed_now = speed_config.get_value()
    # set the config
    print(f'shutterspeed_now set: {shutterspeed_now}')
    # apply config to camera
    camera.set_config(config)

# set whitebalance
config = camera.get_config()
OK, wb_config = gp.gp_widget_get_child_by_name(config, 'whitebalance')

# import code
# code.interact(local=dict(globals(), **locals())) 
if OK >= gp.GP_OK:
    wb = wb_config.get_value()
    print(f'wb currently: {wb}')
    wb_set = "Preset 1"
    wb_config.set_value(wb_set)
    time.sleep(1)
    wb_now = wb_config.get_value()
    # set the config
    print(f'wb_now set: {wb_now}')
    # apply config to camera
    camera.set_config(config)

# get configuration tree
# config_list = gp.check_result(gp.gp_camera_list_config(camera))
# for n in range(len(config_list)):
#     print(config_list.get_name(n), config_list.get_value(n))




    



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