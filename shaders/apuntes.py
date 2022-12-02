#Gouraud Shading

#####def shader(render, **kwargs):
#####    L = kwargs['light']
#####    w, v, u = kwargs('bar')
#####    tA, tB, tC = kwargs('texture_c')
#####    A, B, C = kwargs('vertices')
#####    nA, nB, nC = kwargs['norms']
#####
#####    iA = nA.norm() @ L.norm()
#####    iB = nB.norm() @ L.norm()
#####    iC = nC.norm() @ L.norm()
#####    i = iA * 

    #if render.active_text:
     #   tx = tA.x 
    #y = kwargs['y']
    #if(y<100):
    #    return color(255, 0, 0)
    #elif (y>= 100 and y<150):
    #    return color(200, 50, 50)
    #elif (y>= 150 and y<200):
    #    return color(200, 50, 50)
    #elif (y>= 200 and y<250):
    #    return color(200, 50, 50)

def shader(render, **kwargs):
    w, u, v = kwargs['bar']
    L = kwargs['light']
    A, B, C = kwargs['vertices']
    tA, tB, tC = kwargs['texture_coords']
    nA, nB, nC = kwargs['normals']

    iA = nA.norm() @ L.norm()
    iB = nB.norm() @ L.norm()
    iC = nC.norm() @ L.norm()

    i = iA * w + iB * u + iC * v

    if render.active_texture:
        tx = tA.x * w + tB.x * u + tC.x * v
        ty = tA.y * w + tB.y * u + tC.y * v

        return render.active_texture.get_color_with_intensity(tx, ty, i)


self.current_color = self.active_shader(self, y = y)

