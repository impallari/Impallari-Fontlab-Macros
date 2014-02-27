#FLM: Mediciones: Medir Informacion Base

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
text.append( 'Font, UPM, x-height, stem, n_counter, o_counter, space, c_right, e_right, f_left, f_right, i_left, l_left, n_left, n_right, o_both, r_right, s_left, s_right, t_left, t_right, u_left' )
	

for f in AllFonts():
	
	x_height = f.info.xHeight
	half_x_height = x_height / 2
	s1_x_height = x_height * 72 / 100
	s2_x_height = x_height * 29 / 100	
	
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

	space = int(f['space'].width)
	
	c_right = int(f['c'].rightMargin)
	
	e_right = int(f['e'].rightMargin)

	f_margins = getMargins(f["f"], half_x_height)
	f_left = int(f_margins[0])
	f_right = int(f_margins[1])
		
	i_left = int(i_margins[0])

	l_margins = getMargins(f["l"], half_x_height)
	l_left = int(l_margins[0])
	
	r_right = int(f['r'].rightMargin)
	
	s_margins_1 = getMargins(f["s"], s1_x_height)
	s_left = int(s_margins_1[0])	
	s_margins_2 = getMargins(f["s"], s2_x_height)
	s_right = int(s_margins_2[1])
	
	t_left = int(f['t'].leftMargin)
	t_right = int(f['t'].rightMargin)

	u_margins = getMargins(f["u"], half_x_height)
	u_left = int(u_margins[0])		
	
	# Armar Texto
	text.append( 
		str(f.info.familyName) + ' ' + str(f.info.styleName) + ', ' + 
		str(f.info.unitsPerEm) + ', ' + 
		str(x_height) + ', ' + 
		str(stem) + ', ' + 		
		str(n_counter) + ', ' + 
		str(o_counter) + ', ' + 
		str(space) + ', ' + 	
		str(c_right) + ', ' +
		str(e_right) + ', ' +
		str(f_left) + ', ' +
		str(f_right) + ', ' +
		str(i_left) + ', ' +
		str(l_left) + ', ' +
		str(n_left) + ', ' +	
		str(n_right) + ', ' +
		str(o_both) + ', ' +
		str(r_right) + ', ' +
		str(s_left) + ', ' +
		str(s_right) + ', ' +
		str(t_left) + ', ' +
		str(t_right) + ', ' +
		str(u_left)
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
