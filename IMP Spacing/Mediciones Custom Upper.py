#FLM: Mediciones: Medir Informacion Custom Caps

# Description:
# Abrir todas las fuentes a medir y ejecutar el macro
# En resultado es un txt con la informacion de cada fuente

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
text.append( 'Font, Cap-height, Cap Stem, H_counter, H_left, H_right, O_left, O_right' )

print "Starting..."

for f in AllFonts():
	
	x_height = f.info.xHeight
	half_x_height = x_height / 2
	
	cap_height = f.info.capHeight
	half_cap_height = cap_height / 2

	# Calculo el Stem
	I_width = f['I'].width
	I_margins = getMargins(f["I"], half_cap_height)
	caps_stem = int(I_width - I_margins[0] - I_margins[1])

	# Calculo la /H
	H_margins = getMargins(f["H"], half_cap_height)	
	H_left  = int(H_margins[0])
	H_right = int(H_margins[1])
	H_counter = int(f["H"].width - H_margins[0] - H_margins[1]- caps_stem - caps_stem)
	
	# Calculo la /O
	O_margins = getMargins(f["O"], half_cap_height)	
	O_left  = int(O_margins[0])
	O_right = int(O_margins[1])

	
	# Armar Texto
	text.append( 
		str(f.info.familyName) + ' ' + str(f.info.styleName) + ', ' + 
		str(cap_height) + ', ' + 
		str(caps_stem) + ', ' + 
		str(H_counter) + ', ' + 		
		str(H_left) + ', ' +
		str(H_right) + ', ' +
		str(O_left) + ', ' +
		str(O_right)
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
