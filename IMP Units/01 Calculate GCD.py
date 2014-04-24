#FLM: Calculate GCD of selected glyphs

# Description:
# Calculate the Greatest Common Denominator of selected glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import fractions
from robofab.world import CurrentFont

# Clear Output windows
from FL import *
fl.output=""

# Function
def gcd(L):
    return reduce(fractions.gcd, L)

f = CurrentFont()
widths = [] 
rounded = []

list = f.selection
items = len(list)

for a in list:	
	currentWidth = int(f[a].width)
	widths.append( currentWidth )	
	if currentWidth % 2 != 0:
		currentWidth = currentWidth + 1
	rounded.append( currentWidth )

widths.sort()
rounded.sort()

print "Original widths:"
print widths	
print gcd( widths )

print ""

print "Rounded Up widths:"
print rounded	
print gcd( rounded ) 

print ""  
print "Done!"
