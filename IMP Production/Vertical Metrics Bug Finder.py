#FLM: Vertical Metrics Bug Finder

# Description:
# Mark in color glyphs that exceeds the BBox limits 
# defined in metricsMax and metricsMin variables

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Variables
# Tweak to fit your font
metricsMax = 1004
metricsMin = -246

# Dependencies
from robofab.world import CurrentFont, CurrentGlyph
f = CurrentFont()
glyphs = f.glyphs

for g in glyphs:
	bbox = g.box
	# print bbox
	if bbox[3] > int(metricsMax):
		# print g.name + " xMax: " + str(bbox[3])
		g.mark = 240
	if bbox[1] < int(metricsMin):
		# print g.name + " xMin: " + str(bbox[1])
		g.mark = 220
		
f.update()

print "Done!"
