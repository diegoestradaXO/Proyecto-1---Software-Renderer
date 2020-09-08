import struct

#Este script sirve para poder cargar modelos en archivos .obj
#guarda informacion de las caras, vertices, tvertices, normales
#De igual manera, lee un archivo .bmp que es la textura a aplicar al modelo cargado
#anteriormente

def color(r, g, b):
  return bytes([b, g, r])


def try_int_minus1(s, base=10, val=None):
  try:
    return int(s, base) - 1
  except ValueError:
    return val


class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        self.vertices = []
        self.tvertices = []
        self.faces = []
        self.normals = []
        self.read()

    def read(self):
        #Lectura del archivo linea por linea
        for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    prefix = ''
                if prefix == 'v':
                    if value[0]==' ':
                        value = value[1:]
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vt':
                    self.tvertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vn':
                    self.normals.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(map(try_int_minus1, face.split('/'))) for face in value.split(' ')])
        for tv in self.tvertices:
            if(len(tv)==2):
                tv.append(float(0.0))


class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, "rb")
        image.seek(2 + 4 + 4) 
        header_size = struct.unpack("=l", image.read(4))[0]  #header size
        image.seek(2 + 4 + 4 + 4 + 4)
        
        self.width = struct.unpack("=l", image.read(4))[0]  #  width
        self.height = struct.unpack("=l", image.read(4))[0]  #  height
        self.pixels = []
        image.seek(header_size)
        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.pixels[y].append(color(r,g,b))
        image.close()

    def get_color(self, tx, ty, intensity=1):
        x = int(tx * self.width)
        y = int(ty * self.height)
        try:
            return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.pixels[y][x]))
        except:
            pass