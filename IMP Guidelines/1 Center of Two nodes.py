#FLM: Center of Two Nodes

# Description:
# Place guidelines in the middle of 2 nodes
# If the nodes are in the same line, only 1 guideline will be placed
# If the nodes are in different lines, 2 guidelines will be placed

# Credits:
# Pablo Impallari
# http://www.impallari.com

from FL import *

# Get current Glyphs
g = fl.glyph

# Check for 2 nodes to be selected
if g.SelectedCount() == 2:

	# Enable Undo
	fl.SetUndo()

	# Get X and Y position of selected nodes
	i = 1
	s = 1
	misNodosX = {}
	misNodosY = {}
	while i < len(g.nodes):
		n = g[i]
		if n.selected:
			misNodosX[s] = int(n.x)
			misNodosY[s] = int(n.y)
			s += 1
		i += 1
	
	# print misNodosX
	# print misNodosY
	
	# Calculate intermediate X coordinates
	menorX = misNodosX[1]
	mayorX = misNodosX[2]
	if misNodosX[1] > misNodosX[2]:
			menorX = misNodosX[1]
			mayorX = misNodosX[2]
	medioX = menorX + ( mayorX - menorX ) / 2
	if menorX == mayorX:
		medioX = 0

	# Calculate intermediate Y coordinates
	menorY = misNodosY[1]
	mayorY = misNodosY[2]
	if misNodosY[1] > misNodosY[2]:
			menorY = misNodosY[1]
			mayorY = misNodosY[2]
	medioY = menorY + ( mayorY - menorY ) / 2
	if menorY == mayorY:
		medioY = 0
			
	# Add Guidelines
	if medioX != 0:
		g.vguides.append(Guide(medioX))

	if medioY != 0:
		g.hguides.append(Guide(medioY))
	
	# Update font
	fl.UpdateGlyph()

else:
	print "Select 2 nodes"


