from gl import Gl   #, barycentric, V3, V2

r = Gl()
r.glInit()
r.glCreateWindow(1000, 1000)
r.glViewPort(0, 0, 1000, 1000)
r.glClearColor(0, 0, 0)
r.glClear()
#r.glLoad('./mo_MaleniaSKethc.obj')
#r.glLoad('./bear.obj', (0,-1), (0.5, 0.5))
r.glColor(1,0,0)

r.glLoad('./malenia.obj', (0,-2,0), (120, 120, 120))

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