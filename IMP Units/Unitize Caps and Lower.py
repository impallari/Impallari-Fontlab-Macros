#FLM: Unitize Caps and Lowercase

# Description:
# Suggest values to fit glyphs into units

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
# 54 Photo typesetting and later Linotype (18*4)
# 72 (18*4)
# 96 Later Monotype

#Always add .0 - Ej 18.0 instead of 18
units = 36.0

#scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
basic = lower + upper

f = CurrentFont()
anchos = {}
wider = 0

for n in basic:
	name = f[n].name
	width = f[n].width
	anchos[name] = width
	if wider < width:
		wider = width
		
unit = wider / units

print "%d Units of %d (%.2f) points each" % (units, round(unit), unit)

print ""
print "Unitized"
for key, value in sorted(anchos.iteritems(), key=lambda (k,v): (v,k)):
	unitized = value / unit
	print "%s: %s - %d units (%.2f)" % (key, value, round(unitized), unitized)