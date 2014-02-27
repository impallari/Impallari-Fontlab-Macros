#FLM: Select .end glyphs and ligatures

# Description:
# Select al .end glyphs

# Ej:
# /a will not be selected
# /a.end will not be selected

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.end' in g):
		fl.Select( glyph.index )