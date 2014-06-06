#FLM: Draw Pseudo Ogee

# Description:
# Create an Pseudo Ogee shape

# Credits:
# Pablo Impallari1
# http://www.impallari.com

# Dependencies
from robofab.world import CurrentFont
f = CurrentFont()

# Creo un Glyphs Nuevo
newGlyph = f.newGlyph('ogee', clear=True)
 
# Creo un nuevo Pen
pen = newGlyph.getPen()

# Defino Medidas
alto = 500
ancho = 100

# Calculo
inicio_x = 100
inicio_y = 0
angulo = alto / 10 * 4.666666
curva = alto / 3.333333
 
# Lo mando a donde tiene que ir

#ida
pen.moveTo( ( inicio_x, inicio_y ) )
pen.curveTo( (inicio_x + curva * -1, inicio_y + angulo ), (inicio_x + curva, alto - angulo), (inicio_x, alto) )

# ancho
pen.lineTo( ( inicio_x + ancho, inicio_y + alto ) )

# vuelta
pen.curveTo( (inicio_x + curva + ancho, alto - angulo), (inicio_x + curva * -1 + ancho, inicio_y + angulo ), (inicio_x + ancho, inicio_y) )

# cierra
pen.lineTo( ( inicio_x, inicio_y ) )
pen.closePath()

# Margenes
newGlyph.leftMargin = 100
newGlyph.rightMargin = 100
 
# Update 
newGlyph.update()
f.update()

print "Done!"
