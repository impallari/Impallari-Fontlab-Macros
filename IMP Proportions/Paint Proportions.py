#FLM: Paint Narrower and Wider Glyphs

# Description:
# Paint Narrow Glyphs in Red and Wider Glyphs in Green

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont
from robofab.interface.all.dialogs import Message
f = CurrentFont()
glyphs = f.glyphs

tolerancia = 93;

# Se fija que haya 1 solo seleccionado y toma el ancho del mismo
if fl.count_selected != 1:
	Message("Select 1 Glyph")	
else:	
	source = f.selection[0]

ancho = f[source].width

# Limpia todos los colores
for g in glyphs:
	g.mark = 0

# pinta todos los glyphs
for g in glyphs:
	este = int(g.width)
	
	#Iguales
	if este == ancho:
		g.mark = 70
	
	#Narrower
	if ancho > este: 
		g.mark = 130
	
	#Wider
	if ancho < este:
		g.mark = 255		

	#Muy Narrower
	if ancho - tolerancia > este: 
		g.mark = 0
	
	#Muy Wider
	if ancho + tolerancia < este:
		g.mark = 0

f.update()
print "Done!"
