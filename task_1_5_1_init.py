import time
import gc

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('deleted')


pt = Point(1,1)
pt = 1
gc.collect()

