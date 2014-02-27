#FLM: Select .end glyphs

# Description:
# Select al .end glyphs that are not ligatures

# Ej:
# /f_i will be selected
# /f_i.end will not be selected

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.end' in g):
		if ( '_' not in g): 
			fl.Select( glyph.index )