
from ctypes import *

class Vector2(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

class Vector3(Structure):
    _fields_ = [("x", c_int), ("y", c_int), ("z", c_int)]



# ray.o
RAY_LIB = CDLL("engine/lib/ray.o")

RAY_SHOOT = RAY_LIB.shoot
RAY_SHOOT.argtypes = [POINTER(Vector2), POINTER(Vector3), POINTER(Vector3)]

RAY_ECHO = RAY_LIB.echo
RAY_ECHO.restype = c_int