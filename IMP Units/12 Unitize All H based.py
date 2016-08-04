#FLM: Calculate H-based units for All Fonts

# Description:
# Unitize a font based on the H width

# Credits:
# Pablo Impallari
# http://www.impallari.com

# In how many units do you want to divide your lowercase n
ngrid = 40.0

#scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
punct = ["space", "period", "hyphen"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#basic = lower + upper + punct + numbers
basic = upper

# Clear Output windows
from FL import *
fl.output=""

# Dependencies
import operator
import os.path
from robofab.world import AllFonts
from robofab.interface.all.dialogs import PutFile

# Campos
text = []
text.append( 'Font, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z' )

# Go
mycount = 1
for f in AllFonts():

	# Calculate Unit Value
	print str(mycount) + ' ' + str(f.info.familyName)
	unit = f['H'].width / ngrid
	mycount = mycount + 1

	# Armar Texto
	text.append( 
		str(f.info.familyName) + ' ' + str(f.info.styleName) + ', ' + 
		str(int(round(f['A'].width/unit))) + ', ' + 
		str(int(round(f['B'].width/unit))) + ', ' + 
		str(int(round(f['C'].width/unit))) + ', ' + 
		str(int(round(f['D'].width/unit))) + ', ' + 
		str(int(round(f['E'].width/unit))) + ', ' + 
		str(int(round(f['F'].width/unit))) + ', ' + 
		str(int(round(f['G'].width/unit))) + ', ' + 
		str(int(round(f['H'].width/unit))) + ', ' + 
		str(int(round(f['I'].width/unit))) + ', ' + 
		str(int(round(f['J'].width/unit))) + ', ' + 
		str(int(round(f['K'].width/unit))) + ', ' + 
		str(int(round(f['L'].width/unit))) + ', ' + 
		str(int(round(f['M'].width/unit))) + ', ' + 
		str(int(round(f['N'].width/unit))) + ', ' + 
		str(int(round(f['O'].width/unit))) + ', ' + 
		str(int(round(f['P'].width/unit))) + ', ' + 
		str(int(round(f['Q'].width/unit))) + ', ' + 
		str(int(round(f['R'].width/unit))) + ', ' + 
		str(int(round(f['S'].width/unit))) + ', ' + 
		str(int(round(f['T'].width/unit))) + ', ' + 
		str(int(round(f['U'].width/unit))) + ', ' + 
		str(int(round(f['V'].width/unit))) + ', ' + 
		str(int(round(f['W'].width/unit))) + ', ' + 
		str(int(round(f['X'].width/unit))) + ', ' + 
		str(int(round(f['Y'].width/unit))) + ', ' + 
		str(int(round(f['Z'].width/unit))) 
	)

# Save File
text = '\n'.join(text)
path = PutFile('Save file as:')
if path:
    file = open(path, 'w')
    file.write(text)
    file.close()
    
# Done!
print "Done!"