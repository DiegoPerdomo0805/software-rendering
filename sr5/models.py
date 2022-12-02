import struct
from structs import color

class Obj(object):
    def __init__(self, filename):
        with open(filename) as file:
            self.lines = file.read().splitlines()
        
        self.vertices = []
        self.faces = []
        self.t_vertices = []
        self.read()
    
    def read(self):
        for line in self.lines:
            if line:
                #print(line)
                prefix, value = line.split(' ', 1)
                
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    #self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])
                    temp = [list(map(int, face.split('/'))) for face in value.split(' ')]

                    for e in temp:
                        if len(e) < 3:
                            while len(e) < 3:
                                e.append(0)
                    self.faces.append(temp)

                elif prefix == 'vt':
                    temp  =  []
                    for i in value.split(' '):
                        temp.append(float(i))
                    
                    if len(temp) == 2:
                        temp.append(0)
                    self.t_vertices.append(temp)
                    #self.t_vertices.append(list(map(float, value.split(' '))))
    



class Texture(object):
    
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, 'rb')
        image.seek(10)
        header_size = struct.unpack('=l', image.read(4))[0]
        image.seek(14 + 4)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]
        self.pixels = []
        image.seek(header_size)
        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.pixels[y].append(color(r, g, b))
        image.close()

    def getColor(self, tx, ty, intensity = 1):
        x = int(tx * self.width)
        y = int(ty * self.height)
        try:
            return bytes(map(lambda b: round(b * intensity) if b * intensity > 0 else 0 , self.pixels[y][x]))
        except:
            return bytes([0, 0, 0])
        #return 


