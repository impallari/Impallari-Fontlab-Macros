#FLM: Clean-up Tracings in all selected Glyphs
# Based on a macro by Insigne

from robofab.world import *
from robofab.pens.filterPen import thresholdGlyph

f = CurrentFont()
todo = f.selection

# Set minimun Distance
distance = 8

for c in todo:
	
	g = f[c]
	
	# Cleanup
	thresholdGlyph(g, distance)
	
	# Eliminar Contornos Chiquitos
	for contour in g:
	    for contourIndex in reversed(range(len(g))):
	        contour = g[contourIndex]
	        if len(contour) <= 2:
	            g.removeContour(contourIndex)

	#Marco
	g.mark = 130
	
	g.update()