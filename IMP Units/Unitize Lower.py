#FLM: Unitize Lowercase

# Description:
# Suggest values to fit glyphs into units

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import operator
from FL import *
from robofab.world import CurrentFont

# Clear Output windows
fl.output=""

# Typical Units
# 3 Jenson
# 6
# 9 (DB)
# 10 (JvK)
# 12 (MC) 
# 15 (MC)
# 18 (MC)
# 36 (FB)

#Always add .0 - Ej 18.0 instead of 18
units = 36.0

#scope
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
basic = lower

f = CurrentFont()
anchos = {}
wider = 0

for n in basic:
	if f.has_key(n):
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