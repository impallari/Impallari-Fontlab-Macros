#FLM: 03 Add new Anchors

# Description:
# Adds new anchors

# Credits:
# Pablo Impallari
# http://www.impallari.com

print "Starting..."

# Get the Font
from robofab.world import CurrentFont
f = CurrentFont()

# Borrar Anchors Viejos
for glyph in f:
	glyph.clearAnchors()
	
f.update()

# Get Metrics
ascenderHeight = f.info.ascender
capHeight = f.info.capHeight
xHeight = f.info.xHeight
descenderHeight = f.info.descender
bboxTop = f.info.openTypeHheaAscender
bboxBottom = f.info.openTypeHheaDescender

# Set Anchors Y values
Y_top_LC = xHeight + ( ascenderHeight - xHeight ) / 2
Y_top_Cap = capHeight + ( bboxTop - capHeight ) / 2
Y_caronalt = Y_top_LC
Y_aphostrophe = Y_top_LC
Y_periodcentered = capHeight / 2
Y_bottom = descenderHeight / 2
Y_ogonek = xHeight / 10

# Create some Guidleines
f.clearHGuides()
f.appendHGuide(Y_top_LC)
f.appendHGuide(Y_top_Cap)
f.appendHGuide(Y_periodcentered)
f.appendHGuide(Y_bottom)
f.appendHGuide(Y_ogonek)
f.appendHGuide(bboxTop)
f.appendHGuide(bboxBottom)
f.update()


# Lets place the anchors on the Caps Base Glyphs
f['A'].appendAnchor( 'topUC', ( f['A'].width / 2 , Y_top_Cap ) )
f['A'].appendAnchor( 'ogonek', ( ( f['A'].width / 6 ) * 5 , Y_ogonek ) )
f['A'].mark = 100

f['AE'].appendAnchor( 'topUC', ( f['AE'].width / 2 , Y_top_Cap ) )
f['AE'].mark = 100

f['C'].appendAnchor( 'topUC', ( f['C'].width / 2 , Y_top_Cap ) )
f['C'].appendAnchor( 'bottom', ( f['C'].width / 2 , Y_bottom ) )
f['C'].mark = 100

f['D'].appendAnchor( 'topUC', ( f['D'].width / 2 , Y_top_Cap ) )
f['D'].appendAnchor( 'bottom', ( f['D'].width / 2 , Y_bottom ) )
f['D'].mark = 100

f['E'].appendAnchor( 'topUC', ( f['E'].width / 2 , Y_top_Cap ) )
f['E'].appendAnchor( 'bottom', ( f['E'].width / 2 , Y_bottom ) )
f['E'].appendAnchor( 'ogonek', ( ( f['E'].width / 6 ) * 5 , Y_ogonek ) )
f['E'].mark = 100

f['G'].appendAnchor( 'topUC', ( f['G'].width / 2 , Y_top_Cap ) )
f['G'].appendAnchor( 'bottom', ( f['G'].width / 2 , Y_bottom ) )
f['G'].mark = 100

f['H'].appendAnchor( 'topUC', ( f['H'].width / 2 , Y_top_Cap ) )
f['H'].appendAnchor( 'bottom', ( f['H'].width / 2 , Y_bottom ) )
f['H'].mark = 100

f['I'].appendAnchor( 'topUC', ( f['I'].width / 2 , Y_top_Cap ) )
f['I'].appendAnchor( 'bottom', ( f['I'].width / 2 , Y_bottom ) )
f['I'].appendAnchor( 'ogonek', ( f['I'].width / 2 , Y_ogonek ) )
f['I'].mark = 100

f['J'].appendAnchor( 'topUC', ( f['J'].width / 2 , Y_top_Cap ) )
f['J'].mark = 100

f['K'].appendAnchor( 'bottom', ( f['K'].width / 2 , Y_bottom ) )
f['K'].mark = 100

f['L'].appendAnchor( 'topUC', ( f['L'].width / 2 , Y_top_Cap ) )
f['L'].appendAnchor( 'bottom', ( f['L'].width / 2 , Y_bottom ) )
f['L'].appendAnchor( 'caronalt', ( ( f['L'].width / 6 ) * 5 , Y_caronalt ) )
f['L'].appendAnchor( 'periodcentered', ( ( f['L'].width / 6 ) * 5 , Y_periodcentered ) )
f['L'].mark = 100

f['N'].appendAnchor( 'topUC', ( f['N'].width / 2 , Y_top_Cap ) )
f['N'].appendAnchor( 'bottom', ( f['N'].width / 2 , Y_bottom ) )
f['N'].mark = 100

f['O'].appendAnchor( 'topUC', ( f['O'].width / 2 , Y_top_Cap ) )
f['O'].appendAnchor( 'bottom', ( f['O'].width / 2 , Y_bottom ) )
f['O'].appendAnchor( 'ogonek', ( f['O'].width / 2 , Y_ogonek ) )
f['O'].mark = 100

f['Oslash'].appendAnchor( 'topUC', ( f['Oslash'].width / 2 , Y_top_Cap ) )
f['Oslash'].mark = 100

f['R'].appendAnchor( 'topUC', ( f['R'].width / 2 , Y_top_Cap ) )
f['R'].appendAnchor( 'bottom', ( f['R'].width / 2 , Y_bottom ) )
f['R'].mark = 100

f['S'].appendAnchor( 'topUC', ( f['S'].width / 2 , Y_top_Cap ) )
f['S'].appendAnchor( 'bottom', ( f['S'].width / 2 , Y_bottom ) )
f['S'].mark = 100

f['T'].appendAnchor( 'topUC', ( f['T'].width / 2 , Y_top_Cap ) )
f['T'].appendAnchor( 'bottom', ( f['T'].width / 2 , Y_bottom ) )
f['T'].mark = 100

f['U'].appendAnchor( 'topUC', ( f['U'].width / 2 , Y_top_Cap ) )
f['U'].appendAnchor( 'bottom', ( f['U'].width / 2 , Y_bottom ) )
f['U'].appendAnchor( 'ogonek', ( f['U'].width / 2 , Y_ogonek ) )
f['U'].mark = 100

f['W'].appendAnchor( 'topUC', ( f['W'].width / 2 , Y_top_Cap ) )
f['W'].mark = 100

f['Y'].appendAnchor( 'topUC', ( f['Y'].width / 2 , Y_top_Cap ) )
f['Y'].mark = 100

f['Z'].appendAnchor( 'topUC', ( f['Z'].width / 2 , Y_top_Cap ) )
f['Z'].appendAnchor( 'bottom', ( f['Z'].width / 2 , Y_bottom ) )
f['Z'].mark = 100


# Lets place the anchors on the Lowercase Base Glyphs
f['a'].appendAnchor( 'top', ( f['a'].width / 2 , Y_top_LC ) )
f['a'].appendAnchor( 'ogonek', ( ( f['a'].width / 4 ) * 3 , Y_ogonek ) )
f['a'].mark = 100

f['ae'].appendAnchor( 'top', ( f['ae'].width / 2 , Y_top_LC ) )
f['ae'].mark = 100

f['c'].appendAnchor( 'top', ( f['c'].width / 2 , Y_top_LC ) )
f['c'].appendAnchor( 'bottom', ( f['c'].width / 2 , Y_bottom ) )
f['c'].mark = 100

f['d'].appendAnchor( 'bottom', ( f['d'].width / 2 , Y_bottom ) )
f['d'].appendAnchor( 'caronalt', ( f['d'].width - 10 , Y_caronalt ) )
f['d'].mark = 100

f['e'].appendAnchor( 'top', ( f['e'].width / 2 , Y_top_LC ) )
f['e'].appendAnchor( 'bottom', ( f['e'].width / 2 , Y_bottom ) )
f['e'].appendAnchor( 'ogonek', ( ( f['e'].width / 4 ) * 3 , Y_ogonek ) )
f['e'].mark = 100

f['g'].appendAnchor( 'top', ( f['g'].width / 2 , Y_top_LC ) )
f['g'].mark = 100

f['h'].appendAnchor( 'top', ( f['h'].width / 2 , Y_top_LC ) )
f['h'].appendAnchor( 'bottom', ( f['h'].width / 2 , Y_bottom ) )
f['h'].mark = 100

f['i'].appendAnchor( 'bottom', ( f['i'].width / 2 , Y_bottom ) )
f['i'].appendAnchor( 'ogonek', ( f['i'].width / 2 , Y_ogonek ) )
f['i'].mark = 100

f['dotlessi'].appendAnchor( 'top', ( f['dotlessi'].width / 2 , Y_top_LC ) )
f['dotlessi'].mark = 100

f['dotlessj'].appendAnchor( 'top', ( f['dotlessj'].width / 2 , Y_top_LC ) )
f['dotlessj'].mark = 100

f['k'].appendAnchor( 'bottom', ( f['h'].width / 2 , Y_bottom ) )
f['k'].mark = 100

f['l'].appendAnchor( 'top', ( f['l'].width / 2 , Y_top_LC ) )
f['l'].appendAnchor( 'bottom', ( f['l'].width / 2 , Y_bottom ) )
f['l'].appendAnchor( 'caronalt', ( f['l'].width -10 , Y_caronalt ) )
f['l'].appendAnchor( 'periodcentered', ( f['l'].width -10 , Y_periodcentered ) )
f['l'].mark = 100

f['n'].appendAnchor( 'top', ( f['n'].width / 2 , Y_top_LC ) )
f['n'].appendAnchor( 'bottom', ( f['n'].width / 2 , Y_bottom ) )
f['n'].appendAnchor( 'apostrophe', ( 10 , Y_aphostrophe ) )
f['n'].mark = 100

f['o'].appendAnchor( 'top', ( f['o'].width / 2 , Y_top_LC ) )
f['o'].appendAnchor( 'bottom', ( f['o'].width / 2 , Y_bottom ) )
f['o'].appendAnchor( 'ogonek', ( f['o'].width / 2 , Y_ogonek ) )
f['o'].mark = 100

f['oslash'].appendAnchor( 'top', ( f['oslash'].width / 2 , Y_top_LC ) )
f['oslash'].mark = 100

f['r'].appendAnchor( 'top', ( f['r'].width / 2 , Y_top_LC ) )
f['r'].appendAnchor( 'bottom', ( f['r'].width / 2 , Y_bottom ) )
f['r'].mark = 100

f['s'].appendAnchor( 'top', ( f['s'].width / 2 , Y_top_LC ) )
f['s'].appendAnchor( 'bottom', ( f['s'].width / 2 , Y_bottom ) )
f['s'].mark = 100

f['t'].appendAnchor( 'bottom', ( f['t'].width / 2 , Y_bottom ) )
f['t'].appendAnchor( 'caronalt', ( f['t'].width - 10 , Y_caronalt ) )
f['t'].mark = 100

f['u'].appendAnchor( 'top', ( f['u'].width / 2 , Y_top_LC ) )
f['u'].appendAnchor( 'bottom', ( f['u'].width / 2 , Y_bottom ) )
f['u'].appendAnchor( 'ogonek', ( ( f['u'].width / 4 ) * 3 , Y_ogonek ) )
f['u'].mark = 100

f['w'].appendAnchor( 'top', ( f['w'].width / 2 , Y_top_LC ) )
f['w'].mark = 100

f['y'].appendAnchor( 'top', ( f['y'].width / 2 , Y_top_LC ) )
f['y'].mark = 100

f['z'].appendAnchor( 'top', ( f['z'].width / 2 , Y_top_LC ) )
f['z'].appendAnchor( 'bottom', ( f['z'].width / 2 , Y_bottom ) )
f['z'].mark = 100


# Lets place the anchors on the Lowercase Components

f['acute'].appendAnchor( '_top', ( f['acute'].width / 2 , Y_top_LC ) )
f['acute'].mark = 130

f['apostrophe'].appendAnchor( '_apostrophe', ( f['apostrophe'].width / 2 , Y_aphostrophe ) )
f['apostrophe'].mark = 130

f['breve'].appendAnchor( '_top', ( f['breve'].width / 2 , Y_top_LC ) )
f['breve'].mark = 130

f['caron'].appendAnchor( '_top', ( f['caron'].width / 2 , Y_top_LC ) )
f['caron'].mark = 130

f['caron.alt'].appendAnchor( '_caronalt', ( f['caron.alt'].width / 2 , Y_caronalt ) )
f['caron.alt'].mark = 130

f['cedilla'].appendAnchor( '_bottom', ( f['cedilla'].width / 2 , Y_bottom ) )
f['cedilla'].mark = 130

f['circumflex'].appendAnchor( '_top', ( f['circumflex'].width / 2 , Y_top_LC ) )
f['circumflex'].mark = 130

f['commaaccent'].appendAnchor( '_bottom', ( f['commaaccent'].width / 2 , Y_bottom ) )
f['commaaccent'].mark = 130

f['dieresis'].appendAnchor( '_top', ( f['dieresis'].width / 2 , Y_top_LC ) )
f['dieresis'].mark = 130

f['dotaccent'].appendAnchor( '_top', ( f['dotaccent'].width / 2 , Y_top_LC ) )
f['dotaccent'].mark = 130

f['dotbelow'].appendAnchor( '_bottom', ( f['dotbelow'].width / 2 , Y_bottom ) )
f['dotbelow'].mark = 130

f['grave'].appendAnchor( '_top', ( f['grave'].width / 2 , Y_top_LC ) )
f['grave'].mark = 130

f['hungarumlaut'].appendAnchor( '_top', ( f['hungarumlaut'].width / 2 , Y_top_LC ) )
f['hungarumlaut'].mark = 130

f['macron'].appendAnchor( '_top', ( f['macron'].width / 2 , Y_top_LC ) )
f['macron'].mark = 130

f['ogonek'].appendAnchor( '_ogonek', ( f['ogonek'].width / 2 , Y_ogonek ) )
f['ogonek'].mark = 130

f['ring'].appendAnchor( '_top', ( f['ring'].width / 2 , Y_top_LC ) )
f['ring'].mark = 130

f['tilde'].appendAnchor( '_top', ( f['tilde'].width / 2 , Y_top_LC ) )
f['tilde'].mark = 130

f['uni030F'].appendAnchor( '_top', ( f['uni030F'].width / 2 , Y_top_LC ) )
f['uni030F'].mark = 130

f['uni0311'].appendAnchor( '_top', ( f['uni0311'].width / 2 , Y_top_LC ) )
f['uni0311'].mark = 130

f['periodcentered'].appendAnchor( '_periodcentered', ( f['periodcentered'].width / 2 , Y_periodcentered ) )
f['periodcentered'].mark = 130

# Lets place the anchors on the Caps Components
f['acute.cap'].appendAnchor( '_topUC', ( f['acute.cap'].width / 2 , Y_top_Cap ) )
f['acute.cap'].mark = 160

f['breve.cap'].appendAnchor( '_topUC', ( f['breve.cap'].width / 2 , Y_top_Cap ) )
f['breve.cap'].mark = 160

f['caron.cap'].appendAnchor( '_topUC', ( f['caron.cap'].width / 2 , Y_top_Cap ) )
f['caron.cap'].mark = 160

f['circumflex.cap'].appendAnchor( '_topUC', ( f['circumflex.cap'].width / 2 , Y_top_Cap ) )
f['circumflex.cap'].mark = 160

f['dieresis.cap'].appendAnchor( '_topUC', ( f['dieresis.cap'].width / 2 , Y_top_Cap ) )
f['dieresis.cap'].mark = 160

f['dotaccent.cap'].appendAnchor( '_topUC', ( f['dotaccent.cap'].width / 2 , Y_top_Cap ) )
f['dotaccent.cap'].mark = 160

f['grave.cap'].appendAnchor( '_topUC', ( f['grave.cap'].width / 2 , Y_top_Cap ) )
f['grave.cap'].mark = 160

f['hungarumlaut.cap'].appendAnchor( '_topUC', ( f['hungarumlaut.cap'].width / 2 , Y_top_Cap ) )
f['hungarumlaut.cap'].mark = 160

f['macron.cap'].appendAnchor( '_topUC', ( f['macron.cap'].width / 2 , Y_top_Cap ) )
f['macron.cap'].mark = 160

f['ring.cap'].appendAnchor( '_topUC', ( f['ring.cap'].width / 2 , Y_top_Cap ) )
f['ring.cap'].mark = 160

f['tilde.cap'].appendAnchor( '_topUC', ( f['tilde.cap'].width / 2 , Y_top_Cap ) )
f['tilde.cap'].mark = 160

f['uni030F.cap'].appendAnchor( '_topUC', ( f['uni030F.cap'].width / 2 , Y_top_Cap ) )
f['uni030F.cap'].mark = 160

f['uni0311.cap'].appendAnchor( '_topUC', ( f['uni0311.cap'].width / 2 , Y_top_Cap ) )
f['uni0311.cap'].mark = 160

f.update()

print "Done!"
print "Keep in mind that the anchors placement are aproximate, tweek as needed."




