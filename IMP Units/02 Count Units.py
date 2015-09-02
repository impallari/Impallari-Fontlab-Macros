#FLM: Count Units in selected glyph

# Description:
# Count Units in selected glyph

# Credits:
# Pablo Impallari
# http://www.impallari.com

unit = 20.0 # Change this value to your desired unit size

# Clear Output windows
from FL import *
fl.output=""

from robofab.world import CurrentFont

f = CurrentFont()
list = f.selection
# list.sort()

biggest = 0
sumatoria = 0

for g in list:	
	
	glyph = f[g].name
	ancho = f[g].width
	units = ancho / unit
	print "%s units - %s" % (units, glyph)
	
	if units > biggest:
		biggest = units
	
	sumatoria = sumatoria + units

promedio = sumatoria / len(list)	

print ""
print "Average is %s units" % (promedio)		
print "Wider is %s units" % (biggest)








