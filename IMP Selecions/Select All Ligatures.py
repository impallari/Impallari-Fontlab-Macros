#FLM: Select All Ligatures

# Description:
# Select al ligatures containing and underscore in its name

# Ej:
# /s_t will be selected
# /s_t.fina will be selected

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '_' in g):
		fl.Select( glyph.index )