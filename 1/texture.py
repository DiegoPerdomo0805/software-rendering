import struct
from gl import *

class Texture:
    def __init__(self, path):
        self.path = path
        self.read()
    
    def read(self):
        with open(self.path, "rb") as image:
            image.seek(2 + 4 + 2 + 2)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(2+4+2+2+4+4)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)

            self.pixels = []
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    self.pixels[y].append(color(r, g, b))


    #def getColor(self, tx, ty):
    #    #_x = tx % self.width
    #    #_y = ty % self.height
    #    x = round(tx * self.width) #% self.width
    #    y = round(ty * self.height)# % self.height
    #    return self.pixels[y][x]#

    def getColor_i(self, tx, ty, i):
        x = round(tx * self.width) 
        y = round(ty * self.height)
        b = self.pixels[y][x][0] * i
        g = self.pixels[y][x][1] * i
        r = self.pixels[y][x][2] * i
        return color(r, g, b)
t = Texture("./textures/")
#print(t.getColor(0.5, 0.5))
print(t.getColor_i(0.5, 0.5, 0.5))