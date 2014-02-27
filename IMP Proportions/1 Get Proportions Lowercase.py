#FLM: Get Proportions Lowercase

# Description:
# Compare Uppercase Proportions to other fonts

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import OpenFont, CurrentFont
from robofab.interface.all.dialogs import Message

# La fuente seleccionada es la que se va a modificar
myfont = CurrentFont()


# Pregunta de que fuente quiero copiar las proporciones
orignalFont = OpenFont(None, "Which font's Proportions do you want?")
original = {}

# Rango de Glyphs que voy a medir
uppercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Leo las n y obtengo el Ratio
original_n = orignalFont['n'].width
myfont_n = myfont['n'].width

# Leo la fuente de origen
for item in uppercase:
	if myfont.has_key(item):
		
		# Calculo Anchos
		ancho_original = orignalFont[item].width
		ancho_myfont = myfont[item].width
		ratio = ancho_original * 100.00 / original_n
		ancho_nuevo = int( myfont_n * ratio / 100 )
		
		# Calculo Diferencia
		if ancho_myfont > ancho_nuevo :
			diferencia = ancho_nuevo - ancho_myfont
		if ancho_myfont < ancho_nuevo :
			diferencia = "+" + str(ancho_nuevo - ancho_myfont)
		if ancho_myfont == ancho_nuevo:
			diferencia = " - "

		# Imprimo
		print item + " " + str(ancho_nuevo) + " (" + str(diferencia) + ")"
		
		# Borro Lineas Guia Locales
		myfont[item].clearVGuides()
		myfont[item].clearHGuides()
		
		# Agrego Linea Guia en el nuevo Ancho
		myfont[item].appendVGuide(ancho_nuevo)
		
		# Pinto
		if ancho_myfont == ancho_nuevo:
			myfont[item].mark = 70
		if ancho_myfont < ancho_nuevo:
			myfont[item].mark = 130
		if ancho_myfont > ancho_nuevo:
			myfont[item].mark = 255					

# Cierro la fuente Original	
orignalFont.close()

#Updateo mi fuente		
myfont.update()

# Listo el pollo
print '------ Done ------';