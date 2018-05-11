'''
https://www.paraview.org/ParaView/Doc/Nightly/www/py-doc/paraview.simple.StreamTracer.html
'''

from paraview.simple import *
import numpy as np

#OpenDataFile(filename="foam.foam")
#POpenFOAMReader(filename="foam.foam")
Boundary=GetActiveSource() #przypisuje zmiennej aktywne zrodlo (obiekt, w ktorym chcemy stworzyc streamline)
#ColorArrayName='U'

line = StreamTracer(Boundary, SeedType="High Resolution Line Source", MaximumStreamlineLength=50, IntegrationDirection="FORWARD", Vectors=['POINTS','U']) #tworzy streamline zgodnie z dokumentacja
line.SeedType.Point1 = [0, 1.286, 0.0] 				#wspolrzedne pierwszego punktu
line.SeedType.Point2 = [0, 1.450, 0.0]				#wspolrzedne drugiego punktu
line.SeedType.Resolution = 20					#rozdielczosc streamline, ile lini ma zrobic
renderView = GetActiveView()					#pobniera aktywny widok (ustawienie kamery)
display = GetDisplayProperties(line)			#przypisuje zmiennej wlasciwosci zmiennej lini
display.ColorArrayName='U'						#definiuje zmienna, wedlug ktorej ma kolorowac
display.LookupTable = MakeBlueToRedLT(0.0,40)	#zmienia colormap na ludzką i definiuje zakres
display.SetScalarBarVisibility(renderView, True)#wyswietla skale
Render()										#wyswietla streamline
#DataRepresentation = Show()
line.UpdatePipeline()

name=2
for z in np.arange (0.005,0.052,0.005):
	line=str(name) #tworzy zmienna line i zamienia jej typ na string
	line = StreamTracer(Boundary, SeedType="High Resolution Line Source", MaximumStreamlineLength=50, IntegrationDirection="FORWARD", Vectors=['POINTS','U']) #tworzy streamline zgodnie z dokumentacja
	line.SeedType.Point1 = [0, 1.286, z] 				#wspolrzedne pierwszego punktu
	line.SeedType.Point2 = [0, 1.450, z]				#wspolrzedne drugiego punktu
	line.SeedType.Resolution = 20					#rozdielczosc streamline, ile lini ma zrobic
	#renderView = GetActiveView()					#pobniera aktywny widok (ustawienie kamery)
	display = GetDisplayProperties(line)			#przypisuje zmiennej wlasciwosci zmiennej lini
	display.ColorArrayName='U'						#definiuje zmienna, wedlug ktorej ma kolorowac
	display.LookupTable = MakeBlueToRedLT(0.0,40)	#zmienia colormap na ludzką i definiuje zakres
	#display.SetScalarBarVisibility(renderView, True)#wyswietla skale
	Render()										#wyswietla streamline
	#DataRepresentation = Show()
	line.UpdatePipeline()
	name=name+1