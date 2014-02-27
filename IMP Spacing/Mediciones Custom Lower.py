#FLM: Mediciones: Medir Informacion Custom

# Description:
# Abrir todas las fuentes de una familia y ejecutar el macro
# En resultado es un txt con los anchos de los stems de cada miembro

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import os.path
from robofab.world import AllFonts
from robofab.pens.marginPen import MarginPen
from robofab.interface.all.dialogs import PutFile

# Functions
def getMargins(g, y):
	pen = MarginPen(g.getParent(), y, True)
	g.draw(pen)
	# get crossing values
	crossings = pen.getMargins()
	try:
		margins = (round(crossings[0]), g.width - round(crossings[1]))
	except:
		margins = (None, None)
	return margins

# Macro
text = []
text.append( 'Font, x-height, stem, n_counter, a_right, h_left, j_right, l_right, p_left, q_right' )

print "Starting..."

for f in AllFonts():
	
	x_height = f.info.xHeight
	half_x_height = x_height / 2

	a_x_height = x_height * 25 / 100
	k_x_height = x_height * 20 / 100
	s1_x_height = x_height * 72 / 100
	s2_x_height = x_height * 29 / 100
	v_x_height = x_height * 68 / 100
	w_x_height = x_height * 65 / 100
	y_x_height = x_height * 70 / 100
	
	i_width = f['i'].width
	i_margins = getMargins(f["i"], half_x_height)
	stem = int(i_width - i_margins[0] - i_margins[1])

	n_width = f['n'].width
	n_margins = getMargins(f["n"], half_x_height)	
	n_counter = int(n_width - n_margins[0] - n_margins[1]- stem - stem)
	n_left = int(n_margins[0])
	n_right = int(n_margins[1])

	o_width = f['o'].width
	o_margins = getMargins(f["o"], half_x_height)	
	o_counter = int(o_width - o_margins[0] - o_margins[1]- stem - stem)
	o_both = int(o_margins[0])


	a_margins = getMargins(f["a"], half_x_height)	
	a_right = int(a_margins[1])
	
	h_margins = getMargins(f["h"], half_x_height)	
	h_left = int(h_margins[0])
	
	j_margins = getMargins(f["j"], half_x_height)	
	j_right = int(j_margins[1])
	
	l_margins = getMargins(f["l"], half_x_height)	
	l_right = int(l_margins[1])
	
	p_margins = getMargins(f["p"], half_x_height)	
	p_left = int(p_margins[0])
	
	q_margins = getMargins(f["q"], half_x_height)	
	q_right = int(q_margins[1])
	
	# Armar Texto
	text.append( 
		str(f.info.familyName) + ' ' + str(f.info.styleName) + ', ' + 
		str(x_height) + ', ' + 
		str(stem) + ', ' + 		
		str(n_counter) + ', ' + 
		str(a_right) + ', ' +
		str(h_left) + ', ' +
		str(j_right) + ', ' +
		str(l_right) + ', ' +
		str(p_left) + ', ' +
		str(q_right)
	)

# Save File
text = '\n'.join(text)
path = PutFile('Save file as:')
if path:
    file = open(path, 'w')
    file.write(text)
    file.close()
    
# Done!
print "Donde!"
