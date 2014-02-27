#FLM: Sincronize Numerals Sideberings

# Description:
# Copia los sidebearings de los superiores, en los otros 3 amigos

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()

# g.leftMargin = 35
# g.rightMargin = 35

#Left
f['oneinferior'].leftMargin = f['onesuperior'].leftMargin
f['twoinferior'].leftMargin = f['twosuperior'].leftMargin
f['threeinferior'].leftMargin = f['threesuperior'].leftMargin
f['fourinferior'].leftMargin = f['foursuperior'].leftMargin
f['fiveinferior'].leftMargin = f['fivesuperior'].leftMargin
f['sixinferior'].leftMargin = f['sixsuperior'].leftMargin
f['seveninferior'].leftMargin = f['sevensuperior'].leftMargin
f['eightinferior'].leftMargin = f['eightsuperior'].leftMargin
f['nineinferior'].leftMargin = f['ninesuperior'].leftMargin
f['zeroinferior'].leftMargin = f['zerosuperior'].leftMargin

f['one.denominator'].leftMargin = f['onesuperior'].leftMargin
f['two.denominator'].leftMargin = f['twosuperior'].leftMargin
f['three.denominator'].leftMargin = f['threesuperior'].leftMargin
f['four.denominator'].leftMargin = f['foursuperior'].leftMargin
f['five.denominator'].leftMargin = f['fivesuperior'].leftMargin
f['six.denominator'].leftMargin = f['sixsuperior'].leftMargin
f['seven.denominator'].leftMargin = f['sevensuperior'].leftMargin
f['eight.denominator'].leftMargin = f['eightsuperior'].leftMargin
f['nine.denominator'].leftMargin = f['ninesuperior'].leftMargin
f['zero.denominator'].leftMargin = f['zerosuperior'].leftMargin

f['one.numerator'].leftMargin = f['onesuperior'].leftMargin
f['two.numerator'].leftMargin = f['twosuperior'].leftMargin
f['three.numerator'].leftMargin = f['threesuperior'].leftMargin
f['four.numerator'].leftMargin = f['foursuperior'].leftMargin
f['five.numerator'].leftMargin = f['fivesuperior'].leftMargin
f['six.numerator'].leftMargin = f['sixsuperior'].leftMargin
f['seven.numerator'].leftMargin = f['sevensuperior'].leftMargin
f['eight.numerator'].leftMargin = f['eightsuperior'].leftMargin
f['nine.numerator'].leftMargin = f['ninesuperior'].leftMargin
f['zero.numerator'].leftMargin = f['zerosuperior'].leftMargin

#Right
f['oneinferior'].rightMargin = f['onesuperior'].rightMargin
f['twoinferior'].rightMargin = f['twosuperior'].rightMargin
f['threeinferior'].rightMargin = f['threesuperior'].rightMargin
f['fourinferior'].rightMargin = f['foursuperior'].rightMargin
f['fiveinferior'].rightMargin = f['fivesuperior'].rightMargin
f['sixinferior'].rightMargin = f['sixsuperior'].rightMargin
f['seveninferior'].rightMargin = f['sevensuperior'].rightMargin
f['eightinferior'].rightMargin = f['eightsuperior'].rightMargin
f['nineinferior'].rightMargin = f['ninesuperior'].rightMargin
f['zeroinferior'].rightMargin = f['zerosuperior'].rightMargin

f['one.denominator'].rightMargin = f['onesuperior'].rightMargin
f['two.denominator'].rightMargin = f['twosuperior'].rightMargin
f['three.denominator'].rightMargin = f['threesuperior'].rightMargin
f['four.denominator'].rightMargin = f['foursuperior'].rightMargin
f['five.denominator'].rightMargin = f['fivesuperior'].rightMargin
f['six.denominator'].rightMargin = f['sixsuperior'].rightMargin
f['seven.denominator'].rightMargin = f['sevensuperior'].rightMargin
f['eight.denominator'].rightMargin = f['eightsuperior'].rightMargin
f['nine.denominator'].rightMargin = f['ninesuperior'].rightMargin
f['zero.denominator'].rightMargin = f['zerosuperior'].rightMargin

f['one.numerator'].rightMargin = f['onesuperior'].rightMargin
f['two.numerator'].rightMargin = f['twosuperior'].rightMargin
f['three.numerator'].rightMargin = f['threesuperior'].rightMargin
f['four.numerator'].rightMargin = f['foursuperior'].rightMargin
f['five.numerator'].rightMargin = f['fivesuperior'].rightMargin
f['six.numerator'].rightMargin = f['sixsuperior'].rightMargin
f['seven.numerator'].rightMargin = f['sevensuperior'].rightMargin
f['eight.numerator'].rightMargin = f['eightsuperior'].rightMargin
f['nine.numerator'].rightMargin = f['ninesuperior'].rightMargin
f['zero.numerator'].rightMargin = f['zerosuperior'].rightMargin

f.update()

print 'done';