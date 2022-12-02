from gl import Gl

r = Gl()
r.glInit()
r.glCreateWindow(500, 500)
r.glViewPort(0, 0, 500, 500)
#r.glColor(255, 255, 255)
r.glColor(1, 0, 1)
r.glVertex(0, 0)
#r.glPoint(1, 1)
#r.glLine(-1, -1, 1, 1)
#for i in range()

#r.glLine(-0.5, -0.5, -0.5, 0)
#const = 0.5/500
#for i in range(500):
#    r.glLine(-0.5, -0.5, -0.5+const*i, 0)

#for i in range(500):
#    r.glLine(-0.5, -0.5, -0.5, 0-const*i)

r.glSquare(-0.375, -0.375, 0.125, 0.125)
#r.glSquare(0, -0.5, 0.125, 0.125)
r.glLine(0, -0.5, 0.125, -0.375)
r.glLine(-0.5, 0, -0.375, 0.125)
#r.glLine(-0.5, -0.5, -0.375, -0.375)
r.glLine(0, 0, 0.125, 0.125)

#clean
r.glColor(0, 0, 0)
r.glLine(-0.375, -0.375, -0.375, -0.001)
r.glLine(-0.375, -0.375, -0.001, -0.375)
r.glLine(-0.375, 0.001, -0.375, 0.124)
r.glLine(-0.001, -0.375, 0.124, -0.375)

#r.glLine(-0.5, -0.5, -0.5, -0.375)

#puerta
r.glColor(1, 0, 1)
r.glSquare(-0.3, -0.5, -0.2, -0.3)
r.glSquare(-0.5, -0.5, 0, 0)


#ventanas
r.glSquare(-0.4, -0.2, -0.3, -0.1)
r.glSquare(-0.2, -0.2, -0.1, -0.1)


r.glFinish()
