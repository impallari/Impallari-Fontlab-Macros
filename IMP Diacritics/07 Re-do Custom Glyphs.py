#FLM: 07 Re-do Custom Glyphs

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

# Recreate Needed Glysph
# Copy and paste the glyphs you need from Macro 06

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


generarGlyph ('racute', 'r', 'acute', 'top')
generarGlyph ('rcaron', 'r', 'caron', 'top')
generarGlyph ('rdblgrave', 'r', 'uni030F', 'top')
generarGlyph ('rinvertedbreve', 'r', 'uni0311', 'top')

f.update()

print "Done!"
print "Please review the glyphs one by one"