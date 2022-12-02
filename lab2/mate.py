class V2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return V2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return V2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return V2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return V2(self.x / other, self.y / other)



class V3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z

    def __repr__(self):
        return "V3(%s, %s, %s)" % (self.x, self.y, self.z)

    def __add__(self, other):
        return V3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return V3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return V3(self.x * other, self.y * other, self.z * other)
    
    def __truediv__(self, other):
        return V3(self.x / other, self.y / other, self.z / other)

    def punto(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
        # si el producto punto es 0, los vectores son paralelos
        # si el producto punto es > 0, los vectores son ortogonales
        # si el producto punto es < 0, los vectores son anti-ortogonales
        # si el producto punto es 1, los vectores tienen la misma direccion
        # su el producto punto es -1, los vectores son perpendiculares  

    def cruz(self, other): ## producto cruz
        return V3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def mag(self): #magnitud de un vector
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def normalize(self):#vector unitario de un vector
        if self.mag() == 0:
            return V3(0, 0, 0)
        else:
            return self / self.mag()
        #return self / self.mag()

    def round(self):
        return V3(round(self.x), round(self.y), round(self.z))


def cruz(a, b):
    return V3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)


def barycentric(A, B, C, P):
    c = cruz(
        V3(B.x - A.x, C.x - A.x, A.x - P.x),
        V3(B.y - A.y, C.y - A.y, A.y - P.y)
    )

    cx, cy, cz = c.x, c.y, c.z

    if abs(cz) < 1:
        return -1, -1, -1
    u = cx/cz
    v = cy/cz
    w = 1 - ((cx + cy)/cz)
    return w, v, u

def norm(v0, v1, v2):
    return cruz(v1 - v0, v2 - v0).normalize()


def bbox(A, B, C):
    xs = [A.x, B.x, C.x]
    ys = [A.y, B.y, C.y]
    xs.sort()
    ys.sort()
    #return V2(xs[0], ys[0]), V2(xs[2], ys[2])
    return xs[0], xs[-1], ys[0], ys[2]