from gl import *



r = Render(800, 800)

bg = Texture('./models/city.bmp')
r.pixels = bg.pixels

t = Texture('./models/spiderman.bmp')
r.light = V3(0, 0, 1)
r.active_texture = t
r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
#r.load('./models/model.obj', translate=(400, 300, 300), scale=(200, 200, 200), rotate=(0, 0, 0))
r.load('./models/spiderman.obj', translate=(-0.9, -1, -0.5), scale=(0.4, 0.4, 0.4), rotate=(0, 0.3, 0))
r.draw_arrays('TRIANGLES')

t = Texture('./models/sonic.bmp')
r.active_texture = t
r.load('./models/sonic.obj', translate=(0.7, -0.8, 0), scale=(0.09, 0.09, 0.09), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

t = Texture('./models/hulk.bmp')
r.active_texture = t
r.load('./models/hulk.obj', translate=(0.5, -1, 0), scale=(0.2, 0.2, 0.2), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')


t = Texture('./models/camaro.bmp')
r.active_texture = t
r.load('./models/camaro.obj', translate=(-0.2, -0.9, 0), scale=(0.5, 0.5, 0.5), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

t = Texture('./models/tex.bmp')
r.active_texture = t
r.load('./models/sphere.obj', translate=(0, 0.8, 0), scale=(0.2, 0.2, 0.2), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

r.write('out.bmp')
