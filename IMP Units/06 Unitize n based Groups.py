#FLM: Make n-based Groups

# Description:
# Suggest values to fit glyphs into n-based units, and present them into groups

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import operator
from robofab.world import CurrentFont

# Clear Output windows
from FL import *
fl.output=""

#Always add .0 - Ej: 18.0 instead of 18
units = 32.0

#scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
punct = ["space", "period", "hyphen"]
# basic = lower + upper + punct + numbers
basic = lower

f = CurrentFont()

unit = f['n'].width / units

wider = 0

for n in basic:
	if f.has_key(n):
		width = f[n].width
		if wider < width:
			wider = width
			
total = wider / unit

print str(f.info.familyName) + ' ' + str(f.info.styleName)
#print "Fitted into a %d Units system (%d points per unit)" % (total, round(unit))
print str(units) + " n-units, " + str(unit) + " each"
print ""

for u in range(1, int(total+2)):
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
