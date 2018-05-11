from paraview.simple import *

Line1 = StreamTracer(SeedType="High Resolution Line Source")
DataRepresentation = Show()
Line1.SeedType.Point1 = [0, 1.286, 0.0]
Line1.SeedType.Point2 = [0, 1.286, 0.1]
Line1.SeedType.Resolution = 50
writer = CreateWriter("P:/01_REDOS/06_URANS/OF/line1.csv", Line1)
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer