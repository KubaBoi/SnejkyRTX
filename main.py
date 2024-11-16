import struct

from engine.lib import *
from PIL import Image, ImageColor

camera_pos = (NUM_TYPE * 3)(0, 0, 0)

lights_count = 1
triangles_count = 1

camera_dir = (NUM_TYPE * CAMERA_SIZE)(100,0,0, 0,1,0, 0,0,1)
lights = (NUM_TYPE * LIGHT_SIZE)(0,0,0, 0)
triangles = (NUM_TYPE * TRIANGLE_SIZE)(2000,0,2000, # vertex 1
                                        2000,-2000,-2000, # vertex 2
                                        2000,2000,-2000, # vertex 3
                                        25,25,0) # colors                     

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
HALF_HEIGHT = int(SCREEN_HEIGHT / 2)
HALF_WIDTH = int(SCREEN_WIDTH / 2)

screen_pos = (NUM_TYPE * 2)(0, 0)

img = Image.new("RGB", (SCREEN_WIDTH,SCREEN_HEIGHT))

"""color = RAY_SHOOT(screen_pos, camera_pos, camera_dir, 
                lights, lights_count, 
                triangles, triangles_count)
print(color)
byte_arr = struct.pack("<I", color)
print(byte_arr)"""


for y in range(SCREEN_HEIGHT):
    for x in range(SCREEN_WIDTH):
        screen_pos[0] = x - HALF_WIDTH
        screen_pos[1] = y - HALF_HEIGHT
        color = RAY_SHOOT(screen_pos, camera_pos, camera_dir, 
                lights, lights_count, 
                triangles, triangles_count)
        if (color < 0): 
            img.putpixel((x, y), (255, 255, 255))
            continue
        #print(x, y, color)
        byte_arr = struct.pack("<I", color)
        img.putpixel((x, y), (byte_arr[0], byte_arr[1], byte_arr[2]))
        #img.putpixel((x, y), (0,25,0))

img.save("test.png", format="png")