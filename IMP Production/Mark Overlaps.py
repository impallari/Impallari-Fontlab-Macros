#FLM: Mark Overlaps

# Description:
# Mark in color all glyph having Overlaps

# Credits:
# By James Puckett and Jens Kutilek
# http://typophile.com/node/84799



# make a copy of the current font
f = Font(fl.font)

for glyphIndex in range(len(f.glyphs)):
	g = f[glyphIndex]
	if (len(g.components) > 1) or (len(g) > 0 and len(g.components) > 0):
		# only decompose composites made up of more than one component
		g.Decompose()
	if len(g) > 0:
		# glyph has outlines
		g2 = Glyph(g)
		g2.RemoveOverlap()
		if len(g) != len(g2):
			# different number of nodes
			fl.font[glyphIndex].mark = 10
		else:
			# check nodes
			for nodeIndex in range(len(g.nodes)):
				n = g.nodes[nodeIndex]
				n2 = g2.nodes[nodeIndex]
				if len(n) != len(n2):
					# nodes don't have the same number of points
					fl.font[glyphIndex].mark = 20
					break
				else:
					# check points
					for pointIndex in range(len(n.points)):
						if n[pointIndex].x != n2[pointIndex].x or n[pointIndex].y != n2[pointIndex].y:
							fl.font[glyphIndex].mark = 30
							break
fl.UpdateFont()

print "Done!"