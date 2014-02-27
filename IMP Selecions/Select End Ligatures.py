#FLM: Select .end Ligatures

# Description:
# Select al .end glyphs that are ligatures

# Ej:
# /f_i will not be selected
# /f_i.end will be selected

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '_' in g):
		if ( '.end' in g): 
			fl.Select( glyph.index )