from gl import Gl, Texture   #, barycentric, V3, V2


r = Gl()
r.glInit()

SIZE  =  500
r.glCreateWindow(SIZE, SIZE)
r.glViewPort(0, 0, SIZE, SIZE)
r.glClearColor(0, 0, 0)
r.glClear()
#r.glLoad('./mo_MaleniaSKethc.obj')
#r.glLoad('./bear.obj', (0,-1), (0.5, 0.5))
r.glColor(1,0,0)

t = Texture('./src/BEAR_KDK.bmp')
#print(t.getColor(0.5, 0.5))


#r.glLoad('./src/dummy.obj', (0,-6,0), (25, 25, 25 ))# , texture= t )#, t)


#r.glLoad('./src/bear.obj', (-3,-2,0), (240, 240, 240)   )
r.glLoad('./src/bear.obj', (-1,-2,0), (240, 240, 240)   #)
#r.glLoad('./src/bear.obj', (1,-2,0), (240, 240, 240)   )
, t )#, t)

#r.glLoadWire('./bear.obj', (0, -1, 0), (0.5, 0.5, 0.5))

#r.glLoad('./malenia.obj', (0, -1, 0), (0.5, 0.5, 0.5))
#r.glLoadWire('./malenia.obj', (0, -1, 0), (0.1, 0.1, 0.1))

### a = V2(500, 500)
### b = V2(600, 600)
### c = V2(500, 600)
### p = V2(550, 550)
### 
### print(barycentric(a, b, c, p))



#r.glFinish()

r.glFinish()