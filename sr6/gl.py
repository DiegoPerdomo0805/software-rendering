import struct
import time
from mate import *
from models import *
from structs import *

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
        self.z_buffer = [[]]
        
        self.fileName = 'r.bmp'

    def glClear(self):
        self.pixels = [
            [self.clear_Color for x in range(self.width)]
            for y in range(self.height)
        ]

        self.z_buffer = [
            [-float('inf') for x in range(self.width)]
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
        self.glVertex(x, y)

    def glLine(self, x0, y0, x1, y1):
        x0 = int( (x0+1)*(self.ImageW/2)+self.OffsetX )
        y0 = int( (y0+1)*(self.ImageH/2)+self.OffsetY )
        x1 = int( (x1+1)*(self.ImageW/2)+self.OffsetX )
        y1 = int( (y1+1)*(self.ImageH/2)+self.OffsetY )
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        #print(dy, dx)
        
        #if x0 < 0 or y0 < 0 or x1 < 0 or y1 < 0:
        #    raise Exception("Error: x and y must be greater than 0")
        steep = dy > dx
        #hay un problema con las coordenas en y.
        #Listo, el problema era que el y estaba al reves
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        #if x0 > x1:
        #    x0, x1 = x1, x0
        #    y0, y1 = y1, y0
        
            dy = abs(y1 - y0)
            dx = abs(x1 - x0)

        offset = 0 * 2 * dx
        threshold = 2 * 0.5 * dx
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


    #loadmodel wireframe
    def glLoadWire(self, filename, translate=(0,-1, 0), scale=(0.1,0.1,0.1)):
        model = Obj(filename)
        light = V3(0, 0, 1)
        for face in model.faces:
            vcount = len(face)
            #print(' - ',vcount)
            #print(' + ', vcount if vcount == 3 else 'chi')
            for j in range(vcount):
                f1 = face[j][0] 
                f2 = face[(j+1) % vcount][0] 
#
                v1 = model.vertices[f1-1]
                v2 = model.vertices[f2-1]
#
                x1 = (v1[0] + translate[0]) * scale[0]
                y1 = (v1[1] + translate[1]) * scale[1]
                x2 = (v2[0] + translate[0]) * scale[0]
                y2 = (v2[1] + translate[1]) * scale[1]
                #print(x1, y1, x2, y2)
                self.glLine(x1, y1, x2, y2)

    def glLoad(self, filename, translate=(0, 0, 0), scale=(1,1,1), texture=None):
        model = Obj(filename)
        light = V3(0, 0, 1)
        
        for face in model.faces:
            vcount = len(face)
            if vcount == 3:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1

                #print(f1, f2, f3)

                #print(model.vertices[f1], model.vertices[f2], model.vertices[f3])
                #t1 = time.time()
                #a = V3(*model.vertices[f1])
                #b = V3(*model.vertices[f2])
                #c = V3(*model.vertices[f3])
                a = self.transform(model.vertices[f1], translate, scale)
                b = self.transform(model.vertices[f2], translate, scale)
                c = self.transform(model.vertices[f3], translate, scale)
                #print(a, b, c)

                normal = norm(a, b, c)
                intensity = normal.punto(light)
                if texture == None:
                    grey = round(255 * intensity)
                    if intensity < 0:
                        continue
                    #print(grey)
                    self.Triangles(a, c, b, color= color(grey, grey, grey)) 
                else:
                    #print(face[0][1]-1, face[1][1]-1, face[2][1]-1)
                    # print(face[0][1]-1, face[1][1]-1, face[2][1]-1)
                    tA = model.t_vertices[face[0][1] - 1]
                    tB = model.t_vertices[face[1][1] - 1]
                    tC = model.t_vertices[face[2][1] - 1]
                    #print(tA, tB, tC)
                    self.Triangles(a, c, b , texture=texture, texture_coords= (tA, tB, tC), intensity=intensity)
                #t2 = time.time()
                #print(t2-t1)

            else:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1
                f4 = face[3][0] - 1

                v = [	
                    self.transform(model.vertices[f1], translate, scale),
                    self.transform(model.vertices[f2], translate, scale),
                    self.transform(model.vertices[f3], translate, scale),
                    self.transform(model.vertices[f4], translate, scale)
                ]

                normal = norm(v[0], v[1], v[2])
                intensity = normal.punto(light)
                if texture == None:
                    grey = round(255 * intensity)
                    if grey < 0:
                        continue
                    #t1 = self.Triangles(v[0], v[1], v[2], color(grey, grey, grey))
                    #t2 = self.Triangles(v[0], v[2], v[3], color(grey, grey, grey))

                    self.Triangles(v[0], v[1], v[2], color= color(grey, grey, grey))
                    self.Triangles(v[0], v[2], v[3], color= color(grey, grey, grey))
                #self.triangle(t1, t2, color(grey, grey, grey))  
                else:
                    tA = model.t_vertices[face[0][1] - 1]
                    tB = model.t_vertices[face[1][1] - 1]
                    tC = model.t_vertices[face[2][1] - 1]
                    tD = model.t_vertices[face[3][1] - 1]
                    self.Triangles(v[0], v[1], v[2], texture= texture, texture_coords= (tA, tB, tC), intensity= intensity )
                    self.Triangles(v[0], v[2], v[3], texture= texture, texture_coords= (tA, tC, tD), intensity= intensity )

                
    



    def Triangles(self, A, B, C, color = None, texture = None, texture_coords=(), intensity = 1):
        #print(A, B, C)


        # MUY LENTO
        #x_min = int(min(A.x, B.x, C.x) * self.width)
        #x_max = int(max(A.x, B.x, C.x) * self.width)
        #y_min = int(min(A.y, B.y, C.y) * self.height)
        #y_max = int(max(A.y, B.y, C.y) * self.height)


        # MUY RAPIDO
        x_min, x_max, y_min, y_max = bbox(A, B, C)

        


        #print(x_min, x_max, y_min, y_max)

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                w, v, u = barycentric(A, B, C, V2(x, y))
                if w < 0 or v < 0 or u < 0:
                    continue

                z = A.z * w + B.z * v + C.z * u

                if texture:
                    tA, tB, tC = texture_coords
                    tx = tA[0] * w + tB[0] * v + tC[0] * u
                    ty = tA[1] * w + tB[1] * v + tC[1] * u
                    #color = texture.getColor(tx, ty)
                    color = texture.getColor(tx, ty, intensity)
                
                #print(color)
                #print(bytes(color))

                temp_x = int(((x/self.width)  + 1) * (self.ImageW/2) + self.OffsetX)
                temp_y = int(((y/self.height) + 1) * (self.ImageH/2) + self.OffsetY)

                #print(x, y, z, temp_x, temp_y)

                #print(self.z_buffer)
                try:

                    if z > self.z_buffer[temp_x][temp_y]:
                        #DEMASIADO LENTO
                        #self.glPoint(x, y, color)

                        #MUY RAPIDO
                        self.color = color
                        #print(self.current_color)
                        self.glVertex(x/self.width, y/self.height)
                        #print('pintado')
                        self.z_buffer[temp_x][temp_y] = z
                except:
                    pass



                #if color:
                #    self.glPoint(x, y, color)
                #else:
                #    self.glPoint(x, y, color = color)
        
        
    def transform(self, vertex, translate=(0,0,0), scale=(1,1,1)):
        #print(vertex)
        return V3(
            round((vertex[0] + translate[0]) * scale[0]),
            round((vertex[1] + translate[1]) * scale[1]),
            round((vertex[2] + translate[2]) * scale[2])
        )   



#r = Gl()
#r.glInit()
#
#SIZE  =  500
#r.glCreateWindow(SIZE, SIZE)
#r.glViewPort(0, 0, SIZE, SIZE)
#r.glClearColor(0, 0, 0)
#r.glClear()
##r.glLoad('./mo_MaleniaSKethc.obj')
##r.glLoad('./bear.obj', (0,-1), (0.5, 0.5))
#r.glColor(1,0,0)
#
#t = Texture('./src/BEAR_KDK.bmp')
##print(t.getColor(0.5, 0.5))
#
#
##r.glLoad('./src/dummy.obj', (0,-6,0), (25, 25, 25 ))# , texture= t )#, t)
#
#
##r.glLoad('./src/bear.obj', (-3,-2,0), (240, 240, 240)   )
#r.glLoad('./src/bear.obj', (-1,-2,0), (240, 240, 240)   
##r.glLoad('./src/bear.obj', (1,-2,0), (240, 240, 240)   )
#, t )#, t)
#
##r.glLoadWire('./bear.obj', (0, -1, 0), (0.5, 0.5, 0.5))
#
##r.glLoad('./malenia.obj', (0, -1, 0), (0.5, 0.5, 0.5))
##r.glLoadWire('./malenia.obj', (0, -1, 0), (0.1, 0.1, 0.1))
#
#### a = V2(500, 500)
#### b = V2(600, 600)
#### c = V2(500, 600)
#### p = V2(550, 550)
#### 
#### print(barycentric(a, b, c, p))
#
#
#
##r.glFinish()
#
#r.glFinish()