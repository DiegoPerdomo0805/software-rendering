from gettext import translation
import numpy as np

self.view = None

def V3(x, y, z):
    return np.array([x, y, z, 1])


def loadViewMatrix(self, x, y, z, center):
    M1 = matrix([
        [x.x, x.y, x.z, 0],
        [y.x, y.y, y.z, 0],
        [z.x, z.y, z.z, 0],
        [0, 0, 0, 1]
    ])
    M2 = matrix([
        [1, 0, 0, -center.x],
        [0, 1, 0, -center.y],
        [0, 0, 1, -center.z],
        [0, 0, 0, 1]
    ])
    self.view =  M1 * M2


def matrix(matrix):
    return np.array(matrix)


def lowmodel_matrix(self, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
    #translation_matrix = np.array([[1, 0, 0, translate[0]], [0, 1, 0, translate[1]], [0, 0, 1, translate[2]], [0, 0, 0, 1]])
    #scale_matrix = np.array([[scale[0], 0, 0, 0], [0, scale[1], 0, 0], [0, 0, scale[2], 0], [0, 0, 0, 1]])
    #rotation_matrix = np.array([[np.cos(rotate[0]), -np.sin(rotate[0]), 0, 0], [np.sin(rotate[0]), np.cos(rotate[0]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])   
    translate = V3(*translate)
    scale = V3(*scale)
    rotate = V3(*rotate)
    translation_matrix = matrix([
        [1, 0, 0, translate.x],
        [0, 1, 0, translate.y],
        [0, 0, 1, translate.z],
        [0, 0, 0, 1]
    ])

    scale_matrix = matrix([
        [scale.x, 0, 0, 0],
        [0, scale.y, 0, 0],
        [0, 0, scale.z, 0],
        [0, 0, 0, 1]
    ])
    rotation_x = matrix([
        [1, 0, 0, 0],
        [0, np.cos(rotate.x), -np.sin(rotate.x), 0],
        [0, np.sin(rotate.x), np.cos(rotate.x), 0],
        [0, 0, 0, 1]
    ])
    rotation_y = matrix([
        [np.cos(rotate.y), 0, np.sin(rotate.y), 0],
        [0, 1, 0, 0],
        [-np.sin(rotate.y), 0, np.cos(rotate.y), 0],
        [0, 0, 0, 1]
    ])
    rotation_z = matrix([
        [np.cos(rotate.z), -np.sin(rotate.z), 0, 0],
        [np.sin(rotate.z), np.cos(rotate.z), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    rotation_matrix = rotation_x @ rotation_y @ rotation_z

    self.model = translation_matrix @ rotation_matrix @ scale_matrix




def loadProjectionMatrix(self):
    self.projection = matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def lookAt(self, eye, center, up):
    z =(eye - center).normalize()
    x = (up * z).normalize()
    y = (z * x).normalize()

    self.loadViewMatrix(x, y, z, center)
    self.loadProjectionMatrix()



def transform_vertex(self, vertex):
    #vertex = V3(*vertex)
    augmented_vertex = [
        vertex.x,
        vertex.y,
        vertex.z,
        1
    ]
    #transformed_vertex = translation_matrix @ scale_matrix @ rotation_matrix @ augmented_vertex
    transformed_vertex = self.viewport @ self.view @ self.Model @ augmented_vertex
    #transfrom_vertex = V3|transformed_vertex[0], transformed_vertex[1], transformed_vertex[2]
    transformed_vertex = V3(transformed_vertex)
    return V3(
        transformed_vertex.x / transformed_vertex.w,
        transformed_vertex.y / transformed_vertex.w,
        transformed_vertex.z / transformed_vertex.w
    )

    return V3(transformed_vertex[0], transformed_vertex[1], transformed_vertex[2])

def load_model(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
    model = Model()
    model.load(filename)
    model.lowmodel_matrix(translate, scale, rotate)
    return model

def load_texture(self, filename):
    texture = Texture()
    texture.load(filename)
    return texture

def load_shader(self, vertex_filename, fragment_filename):
    shader = Shader()
    shader.load(vertex_filename, fragment_filename)
    return shader

def load_camera(self, position, rotation):
    camera = Camera()
    camera.load(position, rotation)
    return camera

def load_light(self, position, color):
    light = Light()
    light.load(position, color)
    return light

def load_material(self, color):
    material = Material()
    material.load(color)
    return material

def load_mesh(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
    mesh = Mesh()
    mesh.load(filename)
    mesh.lowmodel_matrix(translate, scale, rotate)
    return mesh

def lookAt(self, eye, center, up):
    z = (eye - center).norm() #(eye - center) / np.linalg.norm(eye - center)
    x = (up @ z ).norm()
    y = (z @ x).norm()


    return loadViewMatrix(eye, center, up)

    
    
def loadViewportMatrix(self, width, height):
    x= 0
    y = 0
    self.viewport = matrix([
        [width / 2, 0, 0, x + width / 2],
        [0, height / 2, 0, y + height / 2],
        [0, 0, 128, 0],
        [0, 0, 0, 1]
    ])




    #f = center - eye
    #f = f / np.linalg.norm(f)
    #s = up @ f
    #s = s / np.linalg.norm(s)
    #u = f @ s
    #M = np.array([
    #    [s.x, s.y, s.z, 0],
    #    [u.x, u.y, u.z, 0],
    #    [-f.x, -f.y, -f.z, 0],
    #    [0, 0, 0, 1]
    #])
    #T = np.array([
    #    [1, 0, 0, -eye.x],
    #    [0, 1, 0, -eye.y],
    #    [0, 0, 1, -eye.z],
    #    [0, 0, 0, 1]
    #])
    #return M @ T

    load_model(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0))