#FLM: Select .ss06 glyphs

# Description:
# Select all .ss06 glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.ss06' in g) : fl.Select( glyph.index )