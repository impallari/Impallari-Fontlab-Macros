#FLM: Paint Same Width as selected

# Description:
# Paint all glyph of the same width

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont
from robofab.interface.all.dialogs import Message
f = CurrentFont()
glyphs = f.glyphs

# Se fija que haya 1 solo seleccionado y toma el ancho del mismo
if fl.count_selected != 1:
	Message("Select 1 Glyph")	
else:	
	source = f.selection[0]

ancho = f[source].width

# Limpia todos los colores
for g in glyphs:
	g.mark = 0

# pinta todos los glyphs del mismo ancho
for g in glyphs:
	este = g.width
	if este == ancho:
		g.mark = 240

f.update()
print "Done!"
