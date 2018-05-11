'''
https://www.paraview.org/ParaView/Doc/Nightly/www/py-doc/paraview.simple.Glyph.html
'''

from paraview.simple import *
import numpy as np

Boundary=GetActiveSource()

#== create the filter and setting
my_slice = Slice(Boundary)
#== set the type of slice : plane
my_slice.SliceType = 'Plane'
#== set the plane properties
# origin : reference position
my_slice.SliceType.Origin = [0.0, 0.0, 0.005]
# normal to the plane
my_slice.SliceType.Normal = [0.0, 0.0, 1.0]
# distance of the plane from the origin
my_slice.SliceType.Offset = 0.0
#== other properties of the slice
# crinkle : 0=cut cells and create new polygons, 1=keep full cells
my_slice.Crinkleslice = 0
# triangulate : will create a triangle mesh on the slice
my_slice.Triangulatetheslice = 1
# list of distances to the origin : to create several parallel planes
my_slice.SliceOffsetValues = [0.0]

display = GetDisplayProperties(my_slice)
display.ColorArrayName='U'
display.LookupTable = MakeBlueToRedLT(0.0,40)
Render()

w_Boundary=GetActiveSource()
wektory = Glyph(w_Boundary)
wektory.Vectors = 'U'
wektory.ScaleFactor = 0.1
wektory.Seed = 100000
wektory.MaximumNumberOfSamplePoints = 100000
display = GetDisplayProperties(wektory)
#display.DiffuseColor = [255.0, 255.0, 255.0]
display.ColorArrayName='' #w ten sposób zdefiniowany jest Solid Color
display.DiffuseColor = [0.0, 0.0, 0.0] #określa kolor zgodznie z RGB
#display.LookupTable = MakeBlueToRedLT(0.0,40)
Render()
