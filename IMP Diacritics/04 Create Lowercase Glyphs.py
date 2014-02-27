#FLM: 04 Create Lowercase Glyphs

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