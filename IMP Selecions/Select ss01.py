#FLM: Select .ss01 glyphs

# Description:
# Select all .ss01 glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.ss01' in g) : fl.Select( glyph.index )