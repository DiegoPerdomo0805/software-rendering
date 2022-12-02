from signal import raise_signal
import struct

def char(c):
    return struct.pack("=c", c.encode('ascii'))

def word(w):
    return struct.pack("=h", w)

def dword(d):
    return struct.pack("=l", d)

def color(r, g, b):
    return bytes([b, g, r]) 

class Gl(object):
    def glInit(self):
        self.color = color(255, 255, 255)
        self.clear_Color = color(0, 0, 0)
        
        self.width = 0
        self.height = 0
        
        self.OffsetX = 0
        self.OffsetY = 0
        
        self.ImageH = 0
        self.ImageW = 0
        
        self.pixels = [[]]
        
        self.fileName = 'r.bmp'

    def glClear(self):
        self.pixels = [
            [self.clear_Color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def glClearColor(self, r, g, b):
        if (r < 0 or r > 1) or (g < 0 or g > 1) or (b < 0 or b > 1):
            raise Exception("Error: r, g, b must be between 0 and 1")
        self.clear_Color = color(r*255, g*255, b*255)
    
    def glVertex(self, x, y):
        #x = int( (x+1)*(self.ImageW/2)+self.OffsetX )
        #y = int( (y+1)*(self.ImageH/2)+self.OffsetY )
        y0 = int(self.OffsetY + (y+1) * (self.ImageH / 2) )#+ (self.ImageH / 2))
        x0 = int(self.OffsetX + (x+1) * (self.ImageW / 2) )#+ (self.ImageW / 2))
        self.pixels[y0-1][x0-1] = self.color
    
    def glColor(self, r, g, b):
        if (r < 0 or r > 1) or (g < 0 or g > 1) or (b < 0 or b > 1):
            raise Exception("Error: r, g, b must be between 0 and 1")
        self.color = color(r*255, g*255, b*255)
    

    def glPoint(self, x, y):
        if x < -1 or y < -1 or x > 1 or y > 1:
            raise Exception("Error: x and y must be greater or equal to -1 and less or equal to 1")
        #if not (-1 <= x <= 1) or not (-1 <= y <= 1):
        #    raise Exception('unexpected value')
        #self.pixels[y][x] = self.color
        self.glVertex(x, y)

    def glLine(self, x0, y0, x1, y1):
        x0 = int( (x0+1)*(self.ImageW/2)+self.OffsetX )
        y0 = int( (y0+1)*(self.ImageH/2)+self.OffsetY )
        x1 = int( (x1+1)*(self.ImageW/2)+self.OffsetX )
        y1 = int( (y1+1)*(self.ImageH/2)+self.OffsetY )
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        #if x0 < 0 or y0 < 0 or x1 < 0 or y1 < 0:
        #    raise Exception("Error: x and y must be greater than 0")
        steep = dy > dx
        
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        offset = 0 * 2 * dx
        threshold = dx * 2 * 0.5
        y = y0
        
        points = []

        for x in range(x0, x1):
            if steep:
                points.append((y, x))
            else:
                #self.glPoint(x, y)
                points.append((x, y))
            offset += (dy/dx) * 2 * dx
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += 2 * dx

        for point in points:
            self.glPoint(
                (point[0] - self.OffsetX)*(2/self.ImageW) - 1,
                (point[1] - self.OffsetY)*(2/self.ImageH) - 1
            )

    def glSquare(self, x0, y0, x1, y1):
        self.glLine(x0, y0, x1, y0)
        self.glLine(x1, y0, x1, y1)
        self.glLine(x1, y1, x0, y1)
        self.glLine(x0, y1, x0, y0)



    def glFinish(self):
        file = open(self.fileName, 'wb')
        #file header
        file.write(char('B'))
        file.write(char('M'))
        file.write(dword(14 + 40 + self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(14 + 40)) 
        #image header
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        #bitmap
        for x in range(self.height):
            for y in range(self.width):
                file.write(self.pixels[x][y])
        file.close()
    
    
    def glCreateWindow(self, width, height):
        if width < 0 or height < 0:
            raise Exception("Error: width and height must be greater than 0")
        self.width = width
        self.height = height
        self.glClear()

    def glViewPort(self, x, y, width, height):
        if width > self.width or height > self.height:
            raise Exception("Error: width and height must not be greater than the window size")
        self.OffsetX = x
        self.OffsetY = y
        self.ImageW = width
        self.ImageH = height
    