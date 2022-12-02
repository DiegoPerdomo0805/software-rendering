from gl import Gl, Texture   #, barycentric, V3, V2


r = Gl()
r.glInit()
#r.glClearColor(0.8, 0.8, 0.8)
SIZE  =  500
r.glCreateWindow(SIZE, SIZE)
r.glViewPort(0, 0, SIZE, SIZE)
r.glClearColor(0, 0, 0)
r.glClear()
#r.glLoad('./mo_MaleniaSKethc.obj')
#r.glLoad('./bear.obj', (0,-1), (0.5, 0.5))
r.glColor(1,0,0)


#t = Texture('./src/xnhzrcu99lp81.bmp')
#bckgrnd = Texture('./src/caelid_malenia.bmp', 2)
bckgrnd = Texture('./src/xnhzrcu99lp81.bmp', 2)

sekiro = Texture('./src/sekiro_.bmp')

bear  = Texture('./src/BEAR_KDK.bmp')

metal = Texture('./src/30306.bmp')

#r.pixels = bckgrnd.pixels


#print(t.getColor(0.5, 0.5))


#r.glLoad('./src/dummy.obj', (0,-6,0), (25, 25, 25 ))# , texture= t )#, t)







r.glColor(0.7,0,0)
r.glLoadWire('./src/malenia.obj', (-5, -7, -1), (0.1125, 0.1125, 0.1125) )#,  t)')

#bigger_smaller = True
for flower in range(0, 7):
    F_SIZE = 500
    r.glLoad('./src/flower.obj', (-0.75 + (flower*0.25), -3, 2), (F_SIZE, F_SIZE, F_SIZE), texture= bckgrnd )#, t)
##r.glLoad('./src/flower.obj', (-0.75, -3.00, 0), (500, 500, 500)   )#,  t)



r.glLoad('./src/bear.obj'  , ( 1.5, -2, 0), (250, 250, 250)  , bear )#,  t)
r.glLoad('./src/sekiro.obj', (0.35, -1.95, 0), (250, 250,250), sekiro)#,  t)


r.glLoad('./src/Axe.obj'  , ( 3.5, 4, 0), (80, 80, 80)  , metal )#,  t)
#r.glLoad('./src/pot.obj', (-0.25, -1.95, 0), (5,5,5), bear)#,  t)
r.glLoad('./src/sphere.obj', (-1.00,  1.70, 0), (250, 250, 250) , metal  )#,  t)


#r.glLoad('./src/flower.obj', (0,0,0), (1, 1, 1), texture= t)



#r.glLoad('./src/bear.obj', (-3,-2,0), (240, 240, 240)   )
#r.glLoad('./src/bear.obj', (-1,-2,0), (240, 240, 240)   #)
#r.glLoad('./src/bear.obj', (1,-2,0), (240, 240, 240)   )
#, t )#, t)

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