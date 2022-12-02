from gl import Gl

SIZE = 800

r = Gl()
r.glInit()
r.glCreateWindow(SIZE, SIZE)
r.glViewPort(0, 0, SIZE, SIZE)
polys = []


poly_1 = [
    (165, 380), (185, 360), (180, 330), (207, 345), (233, 330),
    (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)
]

poly_2 = [(321, 335),(288, 286),(339, 251),(374, 302),]

poly_3 = [(377, 249),(411, 197),(436, 249)]

poly_4 = [
    (413, 177-50),(448, 159-50),(502,  88-50),(553,  53-50),(535,  36-50),(676,  37-50),(660,  52-50),
    (750, 145-50),(761, 179-50),(672, 192-50),(659, 214-50),(615, 214-50),(632, 230-50),(580, 230-50),
    (597, 215-50),(552, 214-50),(517, 144-50),(466, 180-50)
]

poly_5 = [
    (682, 175-300),(708, 120-300),(735, 148-300),(739, 170-300)
]

#for poly in po

polys.append(poly_1)
polys.append(poly_2)
polys.append(poly_3)
polys.append(poly_4)
polys.append(poly_5)



### for poly in polys:
###     print('\n')
###     for e in poly:
###         print(e)
### 
### 
### print('\n\n')

polys2 = []


for i in range(len(polys)):
    poly_temp = []
    for j in range(len(polys[i])):
        temp = []
        for k in range(len(polys[i][j])):
            #polys[i][j][k] = 
            #print(k)
            dummy = polys[i][j][k]
            #print(dummy)
            temp.append( (polys[i][j][k]) / SIZE)
        poly_temp.append(temp)
    polys2.append(poly_temp)



#       for poly in polys2:
#           print('\n')
#           for e in poly:
#               print(e)

colors = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1]
]


#i = 0

for i in range(2):

    c = 0

    for poly in polys2:
        r.glColor(colors[c][0], colors[c][1], colors[c][2])
        temp = (-1, -1)
        for e in poly:
            #r.glLine
            if temp != (-1, -1):
                r.glLine(temp[0], temp[1], e[0], e[1])
                #r.Gl
            temp = e
        #r.glLine(temp[0]/SIZE, temp[1]/SIZE, poly[0][0]/SIZE, poly[0][1]/SIZE)
        r.glLine(temp[0], temp[1], poly[0][0], poly[0][1])
        c += 1
        #r.glFill()


###   print(r.getMAXMIN(poly_1))
###   print(r.getMAXMIN(poly_2))
###   print(r.getMAXMIN(poly_3))
###   print(r.getMAXMIN(poly_4))

#r.glLine(-1, 0, 1, 0)
#print(r.getMAXMIN(polys2[0]))
####    max_mins = []
####        max_mins.append(r.getMAXMIN(poly))
####    
####    f = 0
####    for e in polys2:
####        r.glFill(max_mins[f][0], max_mins[f][1], max_mins[f][2], max_mins[f][3])
####        f += 1
####        #r.glFillPolygon(e)
####    
####    

#print('\n\n')

for e in polys2:
    #print(e)
    r.glFillPolygon(e)
    #print('\n\n\n\n\n\n')
    print(e)
    #print('\n\n\n\n\n\n')



#for e in polys2:
#    #r.glFill(e, colors[polys2.index(e)])
#    print(r.getMAXMIN(e))

#filling = [255, 0, 0]

#r.glFill()


r.glFinish()
