#FLM: Clean-up Tracings in current glyph
# Based on a macro by Insigne

from robofab.world import *
from robofab.pens.filterPen import thresholdGlyph
g = CurrentGlyph()

# Set minimun Distance
distance = 12

# Antes
contornos_antes = len(g)
puntos_antes = 0
i = 0
for contour in g.contours:
	puntos_antes = puntos_antes + len(g[i].points)
	i = i + 1

# Cleanup
thresholdGlyph(g, distance)

# Eliminar Contornos Chiquitos
for contour in g:
    for contourIndex in reversed(range(len(g))):
        contour = g[contourIndex]
        if len(contour) <= 2:
            g.removeContour(contourIndex)

# Despues
contornos_despues = len(g)
puntos_despues = 0
i = 0
for contour in g.contours:
	puntos_despues = puntos_despues + len(g[i].points)
	i = i + 1

# Reporta
print "-----------------------------------"
print g.name
print " "
print str( contornos_antes - contornos_despues ) + " Contornos Eliminados"
print str( puntos_antes - puntos_despues ) + "  Puntos Elimiados"
print " "
print "Quedaron " + str(contornos_despues) + " contornos"
print "-----------------------------------"

