#FLM: 05 Create Uppercase Glyphs

# Description:
# Create new composite glyphs, using anchors and components

# Credits:
# Pablo Impallari
# http://www.impallari.com

print "Starting..."

# Get the Font
from robofab.world import CurrentFont
f = CurrentFont()

# Definimos la funcion que crea los glyphs nuevos
def generarGlyph (nuevo, base, ascento, anchor) :
	f.compileGlyph(nuevo, base, [ ( ascento, anchor ) ] )
	f[nuevo].mark = 80
	f[nuevo].autoUnicodes()
	f[nuevo].update()

# Generate Uppercase Glyphs
generarGlyph ('AEacute', 'AE','acute.cap', 'topUC')

generarGlyph ('Aacute', 'A', 'acute.cap', 'topUC')
generarGlyph ('Abreve', 'A', 'breve.cap', 'topUC')
generarGlyph ('Acircumflex', 'A', 'circumflex.cap', 'topUC')
generarGlyph ('Adblgrave', 'A', 'uni030F.cap', 'topUC')
generarGlyph ('Adieresis', 'A', 'dieresis.cap', 'topUC')
generarGlyph ('Agrave', 'A', 'grave.cap', 'topUC')
generarGlyph ('Ainvertedbreve', 'A', 'uni0311.cap', 'topUC')
generarGlyph ('Amacron', 'A', 'macron.cap', 'topUC')
generarGlyph ('Aring', 'A', 'ring.cap', 'topUC')
generarGlyph ('Atilde', 'A', 'tilde.cap', 'topUC')
generarGlyph ('Aogonek', 'A', 'ogonek', 'ogonek')

generarGlyph ('Cacute', 'C', 'acute.cap', 'topUC')
generarGlyph ('Ccaron', 'C', 'caron.cap', 'topUC')
generarGlyph ('Ccircumflex', 'C', 'circumflex.cap', 'topUC')
generarGlyph ('Cdotaccent', 'C', 'dotaccent.cap', 'topUC')
generarGlyph ('Ccedilla', 'C', 'cedilla', 'bottom')

generarGlyph ('Dcaron', 'D', 'caron.cap', 'topUC')
generarGlyph ('Ddotbelow', 'D', 'dotbelow', 'bottom')

generarGlyph ('Eacute', 'E', 'acute.cap', 'topUC')
generarGlyph ('Ebreve', 'E', 'breve.cap', 'topUC')
generarGlyph ('Ecaron', 'E', 'caron.cap', 'topUC')
generarGlyph ('Ecircumflex', 'E', 'circumflex.cap', 'topUC')
generarGlyph ('Edblgrave', 'E', 'uni030F.cap', 'topUC')
generarGlyph ('Edieresis', 'E', 'dieresis.cap', 'topUC')
generarGlyph ('Edotaccent', 'E', 'dotaccent.cap', 'topUC')
generarGlyph ('Egrave', 'E', 'grave.cap', 'topUC')
generarGlyph ('Einvertedbreve', 'E', 'uni0311.cap', 'topUC')
generarGlyph ('Emacron', 'E', 'macron.cap', 'topUC')
generarGlyph ('Etilde', 'E', 'tilde.cap', 'topUC')
generarGlyph ('Eogonek', 'E', 'ogonek', 'ogonek')
generarGlyph ('Edotbelow', 'E', 'dotbelow', 'bottom')

generarGlyph ('Gacute', 'G', 'acute.cap', 'topUC')
generarGlyph ('Gbreve', 'G', 'breve.cap', 'topUC')
generarGlyph ('Gcircumflex', 'G', 'circumflex.cap', 'topUC')
generarGlyph ('Gdotaccent', 'G', 'dotaccent.cap', 'topUC')
generarGlyph ('Gcommaaccent', 'G', 'commaaccent', 'bottom')

generarGlyph ('Hcircumflex', 'H', 'circumflex.cap', 'topUC')
generarGlyph ('Hdotbelow', 'H', 'dotbelow', 'bottom')

generarGlyph ('Iacute', 'I', 'acute.cap', 'topUC')
generarGlyph ('Ibreve', 'I', 'breve.cap', 'topUC')
generarGlyph ('Icircumflex', 'I', 'circumflex.cap', 'topUC')
generarGlyph ('Idblgrave', 'I', 'uni030F.cap', 'topUC')
generarGlyph ('Idieresis', 'I', 'dieresis.cap', 'topUC')
generarGlyph ('Igrave', 'I', 'grave.cap', 'topUC')
generarGlyph ('Iinvertedbreve', 'I', 'uni0311.cap', 'topUC')
generarGlyph ('Imacron', 'I', 'macron.cap', 'topUC')
generarGlyph ('Itilde', 'I', 'tilde.cap', 'topUC')
generarGlyph ('Idotaccent', 'I', 'dotaccent.cap', 'topUC')
generarGlyph ('Iogonek', 'I', 'ogonek', 'ogonek')
generarGlyph ('Idotbelow', 'I', 'dotbelow', 'bottom')

generarGlyph ('Jcircumflex', 'J', 'circumflex.cap', 'topUC')

generarGlyph ('Kcommaaccent', 'K', 'commaaccent', 'bottom')

generarGlyph ('Lacute', 'L', 'acute.cap', 'topUC')
generarGlyph ('Ldot', 'L', 'periodcentered', 'periodcentered')
generarGlyph ('Lcaron', 'L', 'caron.alt', 'caronalt')
generarGlyph ('Lcommaaccent', 'L', 'commaaccent', 'bottom')

generarGlyph ('Nacute', 'N', 'acute.cap', 'topUC')
generarGlyph ('Ncaron', 'N', 'caron.cap', 'topUC')
generarGlyph ('Ndotaccent', 'N', 'dotaccent.cap', 'topUC')
generarGlyph ('Ntilde', 'N', 'tilde.cap', 'topUC')
generarGlyph ('Ncommaaccent', 'N', 'commaaccent', 'bottom')

generarGlyph ('Oacute', 'O', 'acute.cap', 'topUC')
generarGlyph ('Obreve', 'O', 'breve.cap', 'topUC')
generarGlyph ('Ocircumflex', 'O', 'circumflex.cap', 'topUC')
generarGlyph ('Odblgrave', 'O', 'uni030F.cap', 'topUC')
generarGlyph ('Odieresis', 'O', 'dieresis.cap', 'topUC')
generarGlyph ('Ograve', 'O', 'grave.cap', 'topUC')
generarGlyph ('Ohungarumlaut', 'O', 'hungarumlaut.cap', 'topUC')
generarGlyph ('Oinvertedbreve', 'O', 'uni0311.cap', 'topUC')
generarGlyph ('Omacron', 'O', 'macron.cap', 'topUC')
generarGlyph ('Otilde', 'O', 'tilde.cap', 'topUC')
generarGlyph ('Oogonek', 'O', 'ogonek', 'ogonek')
generarGlyph ('Odotbelow', 'O', 'dotbelow', 'bottom')

generarGlyph ('Oslashacute', 'Oslash', 'acute.cap', 'topUC')

generarGlyph ('Racute', 'R', 'acute.cap', 'topUC')
generarGlyph ('Rcaron', 'R', 'caron.cap', 'topUC')
generarGlyph ('Rdblgrave', 'R', 'uni030F.cap', 'topUC')
generarGlyph ('Rinvertedbreve', 'R', 'uni0311.cap', 'topUC')
generarGlyph ('Rcommaaccent', 'R', 'commaaccent', 'bottom')
generarGlyph ('Rdotbelow', 'R', 'dotbelow', 'bottom')

generarGlyph ('Sacute', 'S', 'acute.cap', 'topUC')
generarGlyph ('Scaron', 'S', 'caron.cap', 'topUC')
generarGlyph ('Scircumflex', 'S', 'circumflex.cap', 'topUC')
generarGlyph ('Sdotbelow', 'S', 'dotbelow', 'bottom')
generarGlyph ('uni015E', 'S', 'cedilla', 'bottom')
generarGlyph ('uni0218', 'S', 'commaaccent', 'bottom')

generarGlyph ('Tcaron', 'T', 'caron.cap', 'topUC')
generarGlyph ('Tdotbelow', 'T', 'dotbelow', 'bottom')
generarGlyph ('uni0162', 'T', 'cedilla', 'bottom')
generarGlyph ('uni021A', 'T', 'commaaccent', 'bottom')

generarGlyph ('Uacute', 'U', 'acute.cap', 'topUC')
generarGlyph ('Ubreve', 'U', 'breve.cap', 'topUC')
generarGlyph ('Ucircumflex', 'U', 'circumflex.cap', 'topUC')
generarGlyph ('Udblgrave', 'U', 'uni030F.cap', 'topUC')
generarGlyph ('Udieresis', 'U', 'dieresis.cap', 'topUC')
generarGlyph ('Ugrave', 'U', 'grave.cap', 'topUC')
generarGlyph ('Uhungarumlaut', 'U', 'hungarumlaut.cap', 'topUC')
generarGlyph ('Uinvertedbreve', 'U', 'uni0311.cap', 'topUC')
generarGlyph ('Umacron', 'U', 'macron.cap', 'topUC')
generarGlyph ('Uring', 'U', 'ring.cap', 'topUC')
generarGlyph ('Utilde', 'U', 'tilde.cap', 'topUC')
generarGlyph ('Uogonek', 'U', 'ogonek', 'ogonek')
generarGlyph ('Udotbelow', 'U', 'dotbelow', 'bottom')

generarGlyph ('Wacute', 'W', 'acute.cap', 'topUC')
generarGlyph ('Wcircumflex', 'W', 'circumflex.cap', 'topUC')
generarGlyph ('Wdieresis', 'W', 'dieresis.cap', 'topUC')
generarGlyph ('Wgrave', 'W', 'grave.cap', 'topUC')

generarGlyph ('Yacute', 'Y', 'acute.cap', 'topUC')
generarGlyph ('Ycircumflex', 'Y', 'circumflex.cap', 'topUC')
generarGlyph ('Ydieresis', 'Y', 'dieresis.cap', 'topUC')
generarGlyph ('Ygrave', 'Y', 'grave.cap', 'topUC')
generarGlyph ('Ytilde', 'Y', 'tilde.cap', 'topUC')

generarGlyph ('Zacute', 'Z', 'acute.cap', 'topUC')
generarGlyph ('Zcaron', 'Z', 'caron.cap', 'topUC')
generarGlyph ('Zdotaccent', 'Z', 'dotaccent.cap', 'topUC')
generarGlyph ('Zdotbelow', 'Z', 'dotbelow', 'bottom')

f.update()

print "Done!"
print "Please review the glyphs one by one"