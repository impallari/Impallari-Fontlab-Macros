#FLM: Measure glyphs widths

# Description:
# Measure glyphs widths in all open fonts

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import os.path
from robofab.world import AllFonts
from robofab.interface.all.dialogs import PutFile

# Campos
text = []
text.append( 'Font, UPM, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space, period, one, two, three, four, five, six, seven, eight, nine, zero' )
	
# Measure
for f in AllFonts():

	# Armar Texto
	text.append( 
		str(f.info.familyName) + ' ' + str(f.info.styleName) + ', ' + 
		str(f.info.unitsPerEm) + ', ' + 
		str(f['A'].width) + ', ' + 
		str(f['B'].width) + ', ' + 
		str(f['C'].width) + ', ' + 
		str(f['D'].width) + ', ' + 
		str(f['E'].width) + ', ' + 
		str(f['F'].width) + ', ' + 
		str(f['G'].width) + ', ' + 
		str(f['H'].width) + ', ' + 
		str(f['I'].width) + ', ' + 
		str(f['J'].width) + ', ' + 
		str(f['K'].width) + ', ' + 
		str(f['L'].width) + ', ' + 
		str(f['M'].width) + ', ' + 
		str(f['N'].width) + ', ' + 
		str(f['O'].width) + ', ' + 
		str(f['P'].width) + ', ' + 
		str(f['Q'].width) + ', ' + 
		str(f['R'].width) + ', ' + 
		str(f['S'].width) + ', ' + 
		str(f['T'].width) + ', ' + 
		str(f['U'].width) + ', ' + 
		str(f['V'].width) + ', ' + 
		str(f['W'].width) + ', ' + 
		str(f['X'].width) + ', ' + 
		str(f['Y'].width) + ', ' + 
		str(f['Z'].width) + ', ' + 
		str(f['a'].width) + ', ' + 
		str(f['b'].width) + ', ' + 
		str(f['c'].width) + ', ' + 
		str(f['d'].width) + ', ' + 
		str(f['e'].width) + ', ' + 
		str(f['f'].width) + ', ' + 
		str(f['g'].width) + ', ' + 
		str(f['h'].width) + ', ' + 
		str(f['i'].width) + ', ' + 
		str(f['j'].width) + ', ' + 
		str(f['k'].width) + ', ' + 
		str(f['l'].width) + ', ' + 
		str(f['m'].width) + ', ' + 
		str(f['n'].width) + ', ' + 
		str(f['o'].width) + ', ' + 
		str(f['p'].width) + ', ' + 
		str(f['q'].width) + ', ' + 
		str(f['r'].width) + ', ' + 
		str(f['s'].width) + ', ' + 
		str(f['t'].width) + ', ' + 
		str(f['u'].width) + ', ' + 
		str(f['v'].width) + ', ' + 
		str(f['w'].width) + ', ' + 
		str(f['x'].width) + ', ' + 
		str(f['y'].width) + ', ' + 
		str(f['z'].width) + ', ' +
		str(f['space'].width) + ', ' +
		str(f['period'].width) + ', ' +
		str(f['one'].width) + ', ' +
		str(f['two'].width) + ', ' +
		str(f['three'].width) + ', ' +
		str(f['four'].width) + ', ' +
		str(f['five'].width) + ', ' +
		str(f['six'].width) + ', ' +
		str(f['seven'].width) + ', ' +
		str(f['eight'].width) + ', ' +
		str(f['nine'].width) + ', ' +
		str(f['zero'].width)
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