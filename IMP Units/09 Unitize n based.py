#FLM: Calculate n-based units for Current Font

# Description:
# Unitize a font based on the n width

# Credits:
# Pablo Impallari
# http://www.impallari.com

# In how many units do you want to divide your lowercase n
# Always add .0 at the end !!!!
ngrid = 32.0

#scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["space", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
punct = ["period", "hyphen"]
# basic = lower + upper + punct + numbers
basic = lower

# Clear Output windows
from FL import *
fl.output=""

# Dependencies
from robofab.world import CurrentFont
from decimal import *

# Get Current font
f = CurrentFont()

# Calculate Unit Value
unit = f['n'].width / ngrid

# Find the Wider Glyph
wider = 0

for g in basic:
	if f.has_key(g):
		width = f[g].width
		if wider < width:
			wider = width
		
maxunits = wider / unit

print str(f.info.familyName) + ' ' + str(f.info.styleName)
# print "Fitted into a %d Units system (%d points per unit)" % (maxunits, round(unit))
print str(ngrid) + " n-units, " + str(unit) + " each"
print ""

for u in range(1, int(maxunits+2)):
	grupo = []
	for g in basic:
		if f.has_key(g):
			g_fitted = int(round(f[g].width / unit))
			if u == g_fitted:
				grupo.append(f[g].name)
	if grupo:
		print str(u) + " Units: %s" % ', '.join(map(str, grupo))
	else:
		print str(u) + " Units: "







