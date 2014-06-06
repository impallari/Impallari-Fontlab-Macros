# FLM: Select between points

# Description:
# In your glyph windows select 2 nodes that are far appart
# The script will selec the intermediate ones
# Sometimes can be usefull to clean handwritting autotracing with lots of nodes
# But it's not perfect

# Credits:
# Josh at the Robofab discussion list
# https://groups.google.com/d/msg/robofab/tz-kCXMuJwc/GcDogqvXODwJ

from robofab.world import CurrentGlyph

glyph = CurrentGlyph()

selectedPoints = []

for contour in glyph.contours:
    if contour.selected:
        for point in contour.bPoints:
            if point.selected:
                selectedPoints.append(point)
if len(selectedPoints) > 0:
    fl.SetUndo()
    
allPoints = []
pointIndexes = []
for i in selectedPoints:
	pointIndexes.append(i.index)

pt1 = min(pointIndexes)
pt2 = max(pointIndexes)

for contour in glyph.contours:
    if contour.selected:
        for point in contour.bPoints:
        	allPoints.append(point)

for point in allPoints:
	if point.index in range(pt1, pt2):
		selectedPoints.append(point)

for i in selectedPoints:
	i.select(state=True)

glyph.update()