from gl import Gl

r = Gl()
r.glInit()
r.glCreateWindow(100, 100)
r.glViewPort(0, 0, 50, 50)
#r.glColor(255, 255, 255)
r.glColor(1, 0, 1)
r.glVertex(1, 1)
r.glFinish()
