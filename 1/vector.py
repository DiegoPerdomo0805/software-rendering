

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
        return self / self.mag()

    def round(self):
        return V3(round(self.x), round(self.y), round(self.z))



    