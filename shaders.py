from gl import *

#sphere is gonna use it
def moon(render, **kwargs):
  # barycentric
  w, v, u = kwargs['bar']
  # texture
  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)
  # normals
  nA, nB, nC = kwargs['varying_normals']

  # light intensity
  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC
  intensity = intensity**2
  if(tcolor):
    return color(
        int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
        int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
        int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
      )
  else:
    return color(0,0,0)

#for the characters
def gourad(render, **kwargs):
  # barycentric
  w, v, u = kwargs['bar']
  # texture
  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)
  # normals
  nA, nB, nC = kwargs['varying_normals']

  # light intensity
  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC

  return color(
      int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
      int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
      int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
    )
