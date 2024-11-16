
from ctypes import *

CAMERA_SIZE = 9
TRIANGLE_SIZE = 12
LIGHT_SIZE = 4
NUM_TYPE = c_double

# ray.o
RAY_LIB = CDLL("engine/lib/ray.o")

RAY_SHOOT = RAY_LIB.shoot
RAY_SHOOT.argtypes = [POINTER(NUM_TYPE), POINTER(NUM_TYPE), 
                      POINTER(NUM_TYPE), # camera_dir
                      POINTER(NUM_TYPE), # lights
                      c_int,
                      POINTER(NUM_TYPE), # triangles
                      c_int]
RAY_SHOOT.restype = c_int32