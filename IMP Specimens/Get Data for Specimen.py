#FLM: Get Data for the Specimen Tool

# Description:
# Get Advance Width and Kerning Pairs data
# Saves two TXT files
# Contents of those filess can be copy-pasted into the specimens tool

# To-do:
# It only report main pairs, not fully expanded if the font uses classes
# Better to run it in a copy of your font, having your kerning manually expanded

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Clear Output windows
from FL import *
fl.output=""

# Dependencies
import os.path
from robofab.world import CurrentFont

# Get Current font
f = CurrentFont()
kerning = f.kerning
path = f.path
dir, fileName = os.path.split(path)

# Scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list = lower + upper

# Get Advance Widths
print "Getting Advance Widths..."
output = open(dir+'/measures-for-specimen-tool.txt', 'w')

for n in list:
	if f.has_key(n):
		output.write( n +',' +str(f[n].width) )
		output.write( '\n')		

output.close()

# Get Kerning Values
print "Getting Kerning..."
output = open(dir+'/kerning-for-specimen-tool.txt', 'w')

for n in list:
	if f.has_key(n):

		currentLeft = kerning.getLeft(f[n].name)
		for pair in currentLeft:
		  if pair[0][1] in list:
		  	output.write( str(pair[0][0]) + ',' + str(pair[0][1]) + ',' + str(pair[1]) )
		  	output.write( '\n')
		
		currentRight = kerning.getRight(f[n].name)
		for pair in currentRight:
		  if pair[0][0] in list:
		  	output.write( str(pair[0][0]) + ',' + str(pair[0][1]) + ',' + str(pair[1]) )
		  	output.write( '\n')
		  	
output.close()

print "Done!"









