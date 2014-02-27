#FLM: Select Basic Ligatures

# Description:
# Select al basic ligatures
# containing and underscore in its name
# that does not have a prefix

# Ej:
# /s_t will be selected
# /s_t.ss01 will not be selected

# Credits:
# Pablo Impallari
# http://www.impallari.com
	
for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '_' in g):
		if ( '.' not in g): 
			fl.Select( glyph.index )