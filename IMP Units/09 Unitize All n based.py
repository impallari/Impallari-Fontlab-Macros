#FLM: Calculate n-based units for All Fonts

# Description:
# Unitize a font based on the n width

# Credits:
# Pablo Impallari
# http://www.impallari.com

# In how many units do you want to divide your lowercase n
ngrid = 32.0

#scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
punct = ["space", "period", "hyphen"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
basic = lower + upper + punct + numbers

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
text.append( 'Font, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space, period, hyphen, zero, one, two, three, four, five, six, seven, eight, nine' )

# Go
mycount = 1
for f in AllFonts():

	# Calculate Unit Value
	print str(mycount) + ' ' + str(f.info.familyName)
	unit = f['n'].width / ngrid
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
		str(int(round(f['Z'].width/unit))) + ', ' + 
		str(int(round(f['a'].width/unit))) + ', ' + 
		str(int(round(f['b'].width/unit))) + ', ' + 
		str(int(round(f['c'].width/unit))) + ', ' + 
		str(int(round(f['d'].width/unit))) + ', ' + 
		str(int(round(f['e'].width/unit))) + ', ' + 
		str(int(round(f['f'].width/unit))) + ', ' + 
		str(int(round(f['g'].width/unit))) + ', ' + 
		str(int(round(f['h'].width/unit))) + ', ' + 
		str(int(round(f['i'].width/unit))) + ', ' + 
		str(int(round(f['j'].width/unit))) + ', ' + 
		str(int(round(f['k'].width/unit))) + ', ' + 
		str(int(round(f['l'].width/unit))) + ', ' + 
		str(int(round(f['m'].width/unit))) + ', ' + 
		str(int(round(f['n'].width/unit))) + ', ' + 
		str(int(round(f['o'].width/unit))) + ', ' + 
		str(int(round(f['p'].width/unit))) + ', ' + 
		str(int(round(f['q'].width/unit))) + ', ' + 
		str(int(round(f['r'].width/unit))) + ', ' + 
		str(int(round(f['s'].width/unit))) + ', ' + 
		str(int(round(f['t'].width/unit))) + ', ' + 
		str(int(round(f['u'].width/unit))) + ', ' + 
		str(int(round(f['v'].width/unit))) + ', ' + 
		str(int(round(f['w'].width/unit))) + ', ' + 
		str(int(round(f['x'].width/unit))) + ', ' + 
		str(int(round(f['y'].width/unit))) + ', ' + 
		str(int(round(f['z'].width/unit))) + ', ' +
		str(int(round(f['space'].width/unit))) + ', ' +
		str(int(round(f['period'].width/unit))) + ', ' +
		str(int(round(f['hyphen'].width/unit))) + ', ' +
		str(int(round(f['one'].width/unit))) + ', ' +
		str(int(round(f['two'].width/unit))) + ', ' +
		str(int(round(f['three'].width/unit))) + ', ' +
		str(int(round(f['four'].width/unit))) + ', ' +
		str(int(round(f['five'].width/unit))) + ', ' +
		str(int(round(f['six'].width/unit))) + ', ' +
		str(int(round(f['seven'].width/unit))) + ', ' +
		str(int(round(f['eight'].width/unit))) + ', ' +
		str(int(round(f['nine'].width/unit))) + ', ' +
		str(int(round(f['zero'].width/unit)))
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