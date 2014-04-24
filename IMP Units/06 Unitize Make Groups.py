#FLM: Make Units Groups

# Description:
# Suggest values to fit glyphs into units, and present them into groups

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import operator
from robofab.world import CurrentFont

# Clear Output windows
from FL import *
fl.output=""

# Typical Units
# 11 and 12 IBM Executive Typewriter
# 18 Monotype
# 36 Lumitype
# 48 Berthold
# 54 Photo typesetting and later Linotype (18*3)
# 72 (18*4)
# 96 Later Monotype

#Always add .0 - Ej 18.0 instead of 18
units = 36.0

#scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
punct = ["space", "period", "hyphen"]
basic = punct + lower + upper + numbers

f = CurrentFont()
wider = 0

for n in basic:
	width = f[n].width
	if wider < width:
		wider = width
		
unit = wider / units

print str(f.info.familyName) + ' ' + str(f.info.styleName)
print "Fitted into a %d Units system (%d points per unit)" % (units, round(unit))
print ""

for u in range(1, int(units+1)):
	grupo = []
	for g in basic:
		g_fitted = int(round(f[g].width / unit))
		if u == g_fitted:
			grupo.append(f[g].name)
	if grupo:
		print str(u) + " Units: %s" % ', '.join(map(str, grupo))
