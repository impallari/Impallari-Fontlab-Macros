#FLM: Measure Font Darkness in all open fonts

# Description:
# Measure some key data for sorting fonts by darkness, in all open fonts
# The macro save a csv file for later sorting and analisis

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

# Clear Output windows
from FL import *
fl.output=""

# CSV file Headers
text = []
# text.append( 'Font, darkness, UPM, x-height, stem, n_width, n_left, n_right, n_counter' )
text.append( 'Font, darkness' )
	
# Measure
for f in AllFonts():

	# Do not trust font data for x-heigth
	# x_height = f.info.xHeight
	
	# Calculate it based on /n bbox instead
	bbox = f['n'].box
	x_height = bbox[3]
	
	half_x_height = x_height / 2
	
	i_width = f['i'].width
	i_margins = getMargins(f["i"], half_x_height)
	stem = int(i_width - i_margins[0] - i_margins[1])

	n_width = f['n'].width
	n_margins = getMargins(f["n"], half_x_height)	
	n_counter = int(n_width - n_margins[0] - n_margins[1]- stem - stem)
	n_left = int(n_margins[0])
	n_right = int(n_margins[1])
	
	upm = f.info.unitsPerEm
	if upm != 1000:
		normalizer = upm / 1000
		upm = 1000
		x_height = x_height / normalizer
		stem = stem / normalizer
		n_width = n_width / normalizer
		n_left = n_left / normalizer
		n_right = n_right / normalizer
		n_counter = n_counter / normalizer
		
	darkness = x_height*stem*n_counter
	
	fontfilename = f.fileName[1]
	
	print 'processing' + str(f.info.familyName) + ' ' + str(f.info.styleName)

	# Armar Texto
	text.append( 
		str(fontfilename) + ', ' +
		str(darkness)
		#str(f.info.familyName) + ' ' + str(f.info.styleName) + ', ' + 
		#str(darkness) + ', ' + 
		#str(upm) + ', ' + 
		#str(x_height) + ', ' + 
		#str(stem) + ', ' + 	
		#str(n_width) + ', ' +
		#str(n_left) + ', ' +
		#str(n_right) + ', ' +	
		#str(n_counter)
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