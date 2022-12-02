from gl import Gl

r = Gl()
r.glInit()
r.glCreateWindow(1000, 1000)
r.glViewPort(0, 0, 1000, 1000)
r.glClearColor(0, 0, 0)
r.glClear()
#r.glLoad('./mo_MaleniaSKethc.obj')
#r.glLoad('./bear.obj', (0,-1), (0.5, 0.5))
r.glColor(1,0,0)
r.glLoad('./malenia.obj', (0,-2), (0.15, 0.15))




#r.glFinish()

r.glFinish()