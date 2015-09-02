#FLM: Unitize all open fonts

# Description:
# Suggest values to fit glyphs into units for all open fonts
# Exports as csv file

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import operator
import os.path
from robofab.world import AllFonts
from robofab.interface.all.dialogs import PutFile

# Clear Output windows
from FL import *
fl.output=""

# Typical Units
# 11 and 12 IBM Executive Typewriter
# 18 Monotype
# 36 Lumitype (18*2)
# 48 Berthold
# 54 Photo typesetting and later Linotype (18*3)
# 72 (18*4)
# 96 Later Monotype (48*2)

#Always add .0 - Ej 18.0 instead of 18
units = 36.0

#scope
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["space", "period", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
#scope = numbers + lower + upper
scope = upper + lower + numbers

# Campos
text = []
text.append( 'Font, units, unit, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space, period, one, two, three, four, five, six, seven, eight, nine, zero' )

for f in AllFonts():
	
	anchos = {}
	wider = 0
	
	for n in scope:
		width = f[n].width
		if wider < width:
			wider = width
			
	unit = wider / units

	# Armar Texto
	text.append( 
		str(f.info.familyName) + ' ' + str(f.info.styleName) + ', ' + 
		str(int(units)) + ', ' + 
		str(int(round(unit))) + ', ' + 
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