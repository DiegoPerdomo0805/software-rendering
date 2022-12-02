import struct
from vector import *

def char(c):
    return struct.pack("=c", c.encode('ascii'))

def word(w):
    return struct.pack("=h", w)

def dword(d):
    return struct.pack("=l", d)

def color(r, g, b):
    return bytes([b, g, r])

def bounding_box(self, points):
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    return xmin, xmax, ymin, ymax
 
def bounding_box_2(*v):
    xs = [p.x for p in v]
    ys = [p.y for p in v]
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    return xmin, xmax, ymin, ymax



class Render(object):
    def glInit(self, width, height):
        self.bg = color(0, 0, 0)
        self.color = color(255, 255, 255)
        self.clear()

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    def glViewPort(self, x, y, width, height):
        self.viewport = (x, y, width, height)
    
    def glClear(self):
        self.pixels = [[self.bg for x in range(self.width)] for y in range(self.height)]
    
    def glClearColor(self, r, g, b):
        self.bg = color(r, g, b)
        self.clear()
    
    def glVertex(self, x, y):
        self.vertex(x, y)
    
    def glColor(self, r, g, b):
        self.Rcolor(r, g, b)
    
    def glFinish(self, filename):
        self.filename = filename
        self.write()


    def clear(self):
        self.glClear()
    
    def point(self, x, y, color):
        self.pixels[y][x] = color
    
    def line(self, x0, y0, x1, y1, color):
        print("no estoy listo")
    
    
    def triangle(a, b, c, color):
        print("no estoy listo")
    
    def write(self):
        f = open(self.filename, "bw")
    
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))
    
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
    
        for x in range(self.width):
            for y in range(self.height):
                f.write(self.pixels[x][y])
        f.close()

    def Rcolor(self, r, g, b):
        self.color = color(r, g, b)
    
