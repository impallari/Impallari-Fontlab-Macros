#FLM: 06 Create All Glyphs

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

# Generate Lowecase Glyphs

generarGlyph ('aacute', 'a', 'acute', 'top')
generarGlyph ('abreve', 'a', 'breve', 'top')
generarGlyph ('acircumflex', 'a', 'circumflex', 'top')
generarGlyph ('adblgrave', 'a', 'uni030F', 'top')
generarGlyph ('adieresis', 'a', 'dieresis', 'top')
generarGlyph ('agrave', 'a', 'grave', 'top')
generarGlyph ('ainvertedbreve', 'a', 'uni0311', 'top')
generarGlyph ('amacron', 'a', 'macron', 'top')
generarGlyph ('aring', 'a', 'ring', 'top')
generarGlyph ('atilde', 'a', 'tilde', 'top')
generarGlyph ('aogonek', 'a', 'ogonek', 'ogonek')

generarGlyph ('aeacute', 'ae', 'acute', 'top')

generarGlyph ('cacute', 'c', 'acute', 'top')
generarGlyph ('ccaron', 'c', 'caron', 'top')
generarGlyph ('ccircumflex', 'c', 'circumflex', 'top')
generarGlyph ('cdotaccent', 'c', 'dotaccent', 'top')
generarGlyph ('ccedilla', 'c', 'cedilla', 'bottom')

generarGlyph ('dcaron', 'd', 'caron.alt', 'caronalt')
generarGlyph ('ddotbelow', 'd', 'dotbelow', 'bottom')

generarGlyph ('eacute', 'e', 'acute', 'top')
generarGlyph ('ebreve', 'e', 'breve', 'top')
generarGlyph ('ecaron', 'e', 'caron', 'top')
generarGlyph ('ecircumflex', 'e', 'circumflex', 'top')
generarGlyph ('edblgrave', 'e', 'uni030F', 'top')
generarGlyph ('edieresis', 'e', 'dieresis', 'top')
generarGlyph ('edotaccent', 'e', 'dotaccent', 'top')
generarGlyph ('egrave', 'e', 'grave', 'top')
generarGlyph ('einvertedbreve', 'e', 'uni0311', 'top')
generarGlyph ('emacron', 'e', 'macron', 'top')
generarGlyph ('etilde', 'e', 'tilde', 'top')
generarGlyph ('eogonek', 'e', 'ogonek', 'ogonek')
generarGlyph ('edotbelow', 'e', 'dotbelow', 'bottom')

generarGlyph ('gacute', 'g', 'acute', 'top')
generarGlyph ('gbreve', 'g', 'breve', 'top')
generarGlyph ('gcircumflex', 'g', 'circumflex', 'top')
generarGlyph ('gdotaccent', 'g', 'dotaccent', 'top')

generarGlyph ('hcircumflex', 'h', 'circumflex', 'top')
generarGlyph ('hdotbelow', 'h', 'dotbelow', 'bottom')

generarGlyph ('iacute', 'dotlessi', 'acute', 'top')
generarGlyph ('ibreve', 'dotlessi', 'breve', 'top')
generarGlyph ('icircumflex', 'dotlessi', 'circumflex', 'top')
generarGlyph ('idblgrave', 'dotlessi', 'uni030F', 'top')
generarGlyph ('idieresis', 'dotlessi', 'dieresis', 'top')
generarGlyph ('igrave', 'dotlessi', 'grave', 'top')
generarGlyph ('iinvertedbreve', 'dotlessi', 'uni0311', 'top')
generarGlyph ('imacron', 'dotlessi', 'macron', 'top')
generarGlyph ('itilde', 'dotlessi', 'tilde', 'top')

generarGlyph ('iogonek', 'i', 'ogonek', 'ogonek')
generarGlyph ('idotbelow', 'i', 'dotbelow', 'bottom')

generarGlyph ('jcircumflex', 'dotlessj', 'circumflex', 'top')

generarGlyph ('kcommaaccent', 'k', 'commaaccent', 'bottom')

generarGlyph ('lacute', 'l', 'acute', 'top')
generarGlyph ('lcaron', 'l', 'caron.alt', 'caronalt')
generarGlyph ('ldot', 'l', 'periodcentered', 'periodcentered')
generarGlyph ('lcommaaccent', 'l', 'commaaccent', 'bottom')

generarGlyph ('nacute', 'n', 'acute', 'top')
generarGlyph ('ncaron', 'n', 'caron', 'top')
generarGlyph ('ndotaccent', 'n', 'dotaccent', 'top')
generarGlyph ('ntilde', 'n', 'tilde', 'top')
generarGlyph ('napostrophe', 'n', 'apostrophe', 'apostrophe')
generarGlyph ('ncommaaccent', 'n', 'commaaccent', 'bottom')

generarGlyph ('oacute', 'o', 'acute', 'top')
generarGlyph ('obreve', 'o', 'breve', 'top')
generarGlyph ('ocircumflex', 'o', 'circumflex', 'top')
generarGlyph ('odblgrave', 'o', 'uni030F', 'top')
generarGlyph ('odieresis', 'o', 'dieresis', 'top')
generarGlyph ('ograve', 'o', 'grave', 'top')
generarGlyph ('ohungarumlaut', 'o', 'hungarumlaut', 'top')
generarGlyph ('oinvertedbreve', 'o', 'uni0311', 'top')
generarGlyph ('omacron', 'o', 'macron', 'top')
generarGlyph ('otilde', 'o', 'tilde', 'top')
generarGlyph ('oogonek', 'o', 'ogonek', 'ogonek')
generarGlyph ('odotbelow', 'o', 'dotbelow', 'bottom')

generarGlyph ('oslashacute', 'oslash', 'acute', 'top')

generarGlyph ('racute', 'r', 'acute', 'top')
generarGlyph ('rcaron', 'r', 'caron', 'top')
generarGlyph ('rdblgrave', 'r', 'uni030F', 'top')
generarGlyph ('rinvertedbreve', 'r', 'uni0311', 'top')
generarGlyph ('rdotbelow', 'r', 'dotbelow', 'bottom')
generarGlyph ('rcommaaccent', 'r', 'commaaccent', 'bottom')

generarGlyph ('sacute', 's', 'acute', 'top')
generarGlyph ('scaron', 's', 'caron', 'top')
generarGlyph ('scircumflex', 's', 'circumflex', 'top')
generarGlyph ('sdotbelow', 's', 'dotbelow', 'bottom')
generarGlyph ('uni015F', 's', 'cedilla', 'bottom')
generarGlyph ('uni0219', 's', 'commaaccent', 'bottom')

generarGlyph ('tcaron', 't', 'caron.alt', 'caronalt')
generarGlyph ('tdotbelow', 't', 'dotbelow', 'bottom')
generarGlyph ('uni0163', 't', 'cedilla', 'bottom')
generarGlyph ('uni021B', 't', 'commaaccent', 'bottom')

generarGlyph ('uacute', 'u', 'acute', 'top')
generarGlyph ('ubreve', 'u', 'breve', 'top')
generarGlyph ('ucircumflex', 'u', 'circumflex', 'top')
generarGlyph ('udblgrave', 'u', 'uni030F', 'top')
generarGlyph ('udieresis', 'u', 'dieresis', 'top')
generarGlyph ('ugrave', 'u', 'grave', 'top')
generarGlyph ('uhungarumlaut', 'u', 'hungarumlaut', 'top')
generarGlyph ('uinvertedbreve', 'u', 'uni0311', 'top')
generarGlyph ('umacron', 'u', 'macron', 'top')
generarGlyph ('utilde', 'u', 'tilde', 'top')
generarGlyph ('uring', 'u', 'ring', 'top')
generarGlyph ('uogonek', 'u', 'ogonek', 'ogonek')
generarGlyph ('udotbelow', 'u', 'dotbelow', 'bottom')

generarGlyph ('wacute', 'w', 'acute', 'top')
generarGlyph ('wcircumflex', 'w', 'circumflex', 'top')
generarGlyph ('wdieresis', 'w', 'dieresis', 'top')
generarGlyph ('wgrave', 'w', 'grave', 'top')

generarGlyph ('yacute', 'y', 'acute', 'top')
generarGlyph ('ycircumflex', 'y', 'circumflex', 'top')
generarGlyph ('ydieresis', 'y', 'dieresis', 'top')
generarGlyph ('ygrave', 'y', 'grave', 'top')
generarGlyph ('ytilde', 'y', 'tilde', 'top')

generarGlyph ('zacute', 'z', 'acute', 'top')
generarGlyph ('zcaron', 'z', 'caron', 'top')
generarGlyph ('zdotaccent', 'z', 'dotaccent', 'top')
generarGlyph ('zdotbelow', 'z', 'dotbelow', 'bottom')

f.update()

print "Done!"
print "Please review the glyphs one by one"