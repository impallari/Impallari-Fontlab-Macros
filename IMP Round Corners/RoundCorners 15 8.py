#FLM: Round Corners 15 15 .8

"""
RADIUS is a Point instance that represents the x and y radius of the corner

HANDLELENGTH is a number between 0. and 1. that determines how long the 
bezier handles should be, affecting the steepness of the curve
"""

import math
	
def getContourRange(nid,g):
	cID = g.FindContour(nid)
	cStart = g.GetContourBegin(cID)
	cEnd = cStart + g.GetContourLength(cID) - 1
	return cStart,cEnd

def getNextNode(nid,g):
	cStart,cEnd = getContourRange(nid,g)
	if nid == cEnd:
		return g[cStart]
	else:
		return g[nid + 1]
	
def getPrevNode(nid,g):
	cStart,cEnd = getContourRange(nid,g)
	if nid == cStart:
		return g[cEnd]
	else:
		return g[nid - 1]

def normalizeVector(p):
	m = getMagnitude(p);
	if m != 0:
		return p*(1/m)
	else:
		return Point(0,0)

def getMagnitude(p):
	return math.sqrt(p.x*p.x + p.y*p.y)

def roundCorner(g,nid,_radius,handleLength = .7):
	
	handleLength = 1 - handleLength
	radius = Point()
	if isinstance(_radius,int):
		radius.x = _radius
		radius.y = _radius
	else:
		radius = _radius
		
	n = g[nid]
	p = Point(n.x, n.y)
	nn = getNextNode(nid, g)
	pn = getPrevNode(nid, g)
	nVect = normalizeVector(Point(-p.x + nn.x, -p.y + nn.y))
	pVect = normalizeVector(Point(-p.x + pn.x, -p.y + pn.y))
	
	pOffset = Point(round(pVect.x * radius.x), round(pVect.y * radius.y))
	nOffset = Point(round(nVect.x * radius.x), round(nVect.y * radius.y))

	n.x += int(pOffset.x)
	n.y += int(pOffset.y)
	
	g.Insert(Node(nCURVE,Point(p.x,p.y)), nid+1)
	n1 = g[nid+1]
	
	n1.x += int(nOffset.x)
	n1.y += int(nOffset.y)
	n1[1].x = p.x + round(pVect.x * radius.x * handleLength)
	n1[1].y = p.y + round(pVect.y * radius.y * handleLength)
	n1[2].x = p.x + round(nVect.x * radius.x * handleLength)
	n1[2].y = p.y + round(nVect.y * radius.y * handleLength)

# RADIUS allows the x and the y radius to be adjusted separately
RADIUS = Point(15,15)

# HANDLELENGTH is a number between 0. and 1. that determines how long the 
# bezier handles should be, affecting the steepness of the curve
HANDLELENGTH = .8
	
g = fl.glyph
fl.SetUndo()
i = 0
while i < len(g.nodes):
	n = g[i]
	if n.selected:
		roundCorner(g,i,RADIUS,HANDLELENGTH)
	i += 1

fl.UpdateGlyph()