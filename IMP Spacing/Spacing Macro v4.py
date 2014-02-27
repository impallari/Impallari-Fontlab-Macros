#FLM: Space Explorer v4.0

#
#    Description:
#    Auto-Spacing for Lowercase Glyphs
#
#    Goals:
#    - Minimize rivers in body text settings
#    - Minimize the need for kernig pairs
#
#    Credits:
#    Pablo Impallari
#    http://www.impallari.com
#

# --- Configuration ----

style = 1 # 1 for sans, 2 for serif
aConstruction = 1 # 1 for roman, 2 for italic construction
gConstruction = 1 # 1 for roman, 2 for italic construction

global_spacing = 80
compensate_rounds = 100

# --- End of Configuration, now run the macro ----

# --------------------------------------------------
# --------- Do not edit bellow this line -----------
# ------ unless you know what you are doing --------
# --------------------------------------------------

# Refinar serif g_roman
# Refinar serif-only Parameters	

print "-------------------------------------------"
print "Starting..."
print "-------------------------------------------"

# --- Dependencies ---
from robofab.world import CurrentFont,CurrentGlyph
from robofab.pens.marginPen import MarginPen

# --- Functions ---
def getMargins(g, y):
	pen = MarginPen(g.getParent(), y, True)
	g.draw(pen)
	crossings = pen.getMargins()
	try:
		margins = (round(crossings[0]), g.width - round(crossings[1]))
	except:
		margins = (None, None)
	return margins
	
def setMargins(g, y, l=None, r=None):
    margins = getMargins(g, y)
    if l is not None and margins[0] is not None:
        difference = margins[0] - g.leftMargin
        g.leftMargin = l - difference
    if r is not None and margins[1] is not None:
        difference = margins[1] - g.rightMargin
        g.rightMargin = r - difference


# --- Grab some info about the font ---
print "Analizing font..."
print "-------------------------------------------"

f = CurrentFont()

x_height = f.info.xHeight
half_x_height = x_height / 2

i_width = f['i'].width
i_margins = getMargins(f["i"], half_x_height)
stem = i_width - i_margins[0] - i_margins[1]

x_height_optical_compensation = x_height * 100 / ( stem * 5 )

n_width = f['n'].width
n_margins = getMargins(f["n"], half_x_height)
n_counter = n_width - n_margins[0] - n_margins[1] - stem - stem

o_width = f['o'].width
o_margins = getMargins(f["o"], half_x_height)
o_counter = o_width - o_margins[0] - o_margins[1] - stem - stem

a_x_height = x_height * 25 / 100
k_x_height = x_height * 20 / 100
s1_x_height = x_height * 72 / 100
s2_x_height = x_height * 29 / 100
v_x_height = x_height * 68 / 100
w_x_height = x_height * 65 / 100
y_x_height = x_height * 70 / 100

# --- Parameters ----
if style == 1:
	factor_space = 78.2455243881 # Advance
	factor_c_right = 673.037037037037 # SB
	factor_e_right = 478.210526315789 # SB
	factor_f_left = 193.59793814433 # Stem half_x_height
	factor_f_right = 148.259541984733 # Stem half_x_height
	factor_groman_left = 598.4 # SB
	factor_groman_right = 1102.36363636364 # SB
	factor_i_left = 259.388235294118 # Stem half_x_height
	factor_l_left = 259.388235294118 # Stem half_x_height	
	factor_n_left = 273.0455246914 # Stem half_x_height
	factor_n_right = 292.8897435897 # Stem half_x_height
	factor_o_both = 591.1903846154 # Stem half_x_height
	factor_r_right = 1215.5 # SB
	factor_s_left = 420.315789473684 # Stem s1_x_height
	factor_s_right = 528.883720930233 # Stem s2_x_height
	factor_t_left = 982.133333333333 # SB
	factor_t_right = 792.111888111888 # SB
	factor_u_left = 295.432600732601 # Stem half_x_height

if style == 2:
	factor_space = 89.6316060398 # Advance
	factor_c_right = 778.1732026144 # SB
	factor_e_right = 596.2612612613 # SB
	factor_f_left = 201.9302890043 # Stem half_x_height
	factor_f_right = 154.0411261542 # Stem half_x_height
	factor_groman_left = 598.4 # ---------------------------- Trucho (Medir desde SB)
	factor_groman_right = 1102.36363636364 # ---------------- Trucho (Medir desde SB)
	factor_i_left = 203.9733115468 # Stem half_x_height
	factor_l_left = 216.5680560078 # Stem half_x_height	
	factor_n_left = 207.4526121128 # Stem half_x_height
	factor_n_right = 235.5974683544 # Stem half_x_height
	factor_o_both = 708.4428571429 # Stem half_x_height
	factor_r_right = 1350.0714285714 # SB
	factor_s_left = 399.8301886792 # Stem s1_x_height
	factor_s_right = 563.4800853485 # Stem s3_x_height
	factor_t_left = 817.28 # SB
	factor_t_right = 1424.6666666667 # SB
	factor_u_left = 237.9158680283 # Stem half_x_height

	# Serif only Parameters	
	factor_serif_a_right = 226.975051975052 # Old was 227.027027027027
	factor_serif_b_left = 247.441860465116  # Old was -------------------- Trucho (Medir desde Stem)
	factor_serif_h_left = 218.587084148728 # Old was 218.602739726027
	factor_serif_j_right = 261.67803030303 # Old was 261.659090909091
	factor_serif_l_right = 224.357142857143 # Old was 224.714285714286
	factor_serif_p_left = 226.945053439298 # Old was 227.317073170732
	factor_serif_q_right = 252.174423893269 # Old was 251.46835443038
	

# --- Calculate Initial New Values ---
print "Calculating New Values..."
print "-------------------------------------------"

space = stem * n_counter / factor_space
n_left = stem * n_counter / factor_n_left
n_right = stem * n_counter / factor_n_right
o_both = stem * n_counter / factor_o_both 
f_left = stem * n_counter / factor_f_left
f_right = stem * n_counter / factor_f_right
r_right = stem * n_counter / factor_r_right
s_left = stem * n_counter / factor_s_left
s_right = stem * n_counter / factor_s_right
t_left = stem * n_counter / factor_t_left
t_right = stem * n_counter / factor_t_right
u_left = stem * n_counter / factor_u_left
i_left = stem * n_counter / factor_i_left
l_left = stem * n_counter / factor_l_left
c_right = stem * n_counter / factor_c_right
e_right = stem * n_counter / factor_e_right
groman_left = stem * n_counter / factor_groman_left
groman_right = stem * n_counter / factor_groman_right	

if style == 2:
	a_right = stem * n_counter / factor_serif_a_right
	b_left = stem * n_counter / factor_serif_b_left
	h_left = stem * n_counter / factor_serif_h_left
	j_right = stem * n_counter / factor_serif_j_right
	l_right = stem * n_counter / factor_serif_l_right
	p_left = stem * n_counter / factor_serif_p_left
	q_right = stem * n_counter / factor_serif_q_right

# --- Apply x-height optical compensation ---
n_left = n_left * x_height_optical_compensation / 100
n_right = n_right * x_height_optical_compensation / 100
o_both = o_both * x_height_optical_compensation / 100
space = space * x_height_optical_compensation / 100
u_left = u_left * x_height_optical_compensation / 100
f_left = f_left * x_height_optical_compensation / 100
f_right = f_right * x_height_optical_compensation / 100
r_right = r_right * x_height_optical_compensation / 100
s_left = s_left * x_height_optical_compensation / 100
s_right = s_right * x_height_optical_compensation / 100
t_left = t_left * x_height_optical_compensation / 100
t_right = t_right * x_height_optical_compensation / 100
i_left = i_left * x_height_optical_compensation / 100
l_left = l_left * x_height_optical_compensation / 100
c_right = c_right * x_height_optical_compensation / 100
e_right = e_right * x_height_optical_compensation / 100
groman_left = groman_left * x_height_optical_compensation / 100
groman_right = groman_right * x_height_optical_compensation / 100	

if style == 2:
	a_right = a_right * x_height_optical_compensation / 100
	b_left = b_left * x_height_optical_compensation / 100
	h_left = h_left * x_height_optical_compensation / 100
	j_right = j_right * x_height_optical_compensation / 100
	l_right = l_right * x_height_optical_compensation / 100
	p_left = p_left * x_height_optical_compensation / 100
	q_right = q_right * x_height_optical_compensation / 100
	
# --- Apply User Preferences ---
n_left = ( n_left * global_spacing / 100 )
n_right = ( n_right * global_spacing / 100 )
o_both = ( o_both * global_spacing / 100 ) * compensate_rounds / 100
space = ( space * global_spacing / 100 ) 
u_left = ( u_left * global_spacing / 100 )
f_left = ( f_left * global_spacing / 100 )
f_right = ( f_right * global_spacing / 100 )
r_right = ( r_right * global_spacing / 100 )
s_left = ( s_left * global_spacing / 100 )
s_right = ( s_right * global_spacing / 100 )
t_left = ( t_left * global_spacing / 100 )
t_right = ( t_right * global_spacing / 100 )
i_left = ( i_left * global_spacing / 100 )
l_left = ( l_left * global_spacing / 100 )
c_right = ( c_right * global_spacing / 100 )
e_right = ( e_right * global_spacing / 100 )
groman_left = ( groman_left * global_spacing / 100 )
groman_right = ( groman_right * global_spacing / 100 )

if style == 2:
	a_right = ( a_right * global_spacing / 100 )
	b_left = ( b_left * global_spacing / 100 )
	h_left = ( h_left * global_spacing / 100 )
	j_right = ( j_right * global_spacing / 100 )
	l_right = ( l_right * global_spacing / 100 )
	p_left = ( p_left * global_spacing / 100 )
	q_right = ( q_right * global_spacing / 100 )

# --- Unmark all glyphs ---
glyphs = f.glyphs
for g in glyphs:
	g.mark = 0
f.update()

# --- Apply Spacing ---
print "Applying new spacing to the Lowercase..."
print "-------------------------------------------"

if f.has_key('space'):
	f['space'].width = space
	f['a'].mark = 80

if f.has_key('a'):
	if style == 1:
		if aConstruction == 1:
			setMargins(f['a'], a_x_height, n_right * 0.57 , None ) #------ Hardcoded, mejorable
			setMargins(f['a'], half_x_height, None, n_right)
			f['a'].mark = 80
		if aConstruction == 2:
			setMargins(f['a'], half_x_height, o_both, n_right)
			f['a'].mark = 80
	if style == 2:
		if aConstruction == 1:
			setMargins(f['a'], a_x_height, n_right * 0.57 , None ) #------ Hardcoded, mejorable
			setMargins(f['a'], half_x_height, None, a_right)
			f['a'].mark = 80
		if aConstruction == 2:
			setMargins(f['a'], half_x_height, o_both, n_right)
			f['a'].mark = 80
				
if f.has_key('b'):
	if style == 1:
		setMargins(f['b'], half_x_height, n_left, o_both)
		f['b'].mark = 80
	if style == 2:
		setMargins(f['b'], half_x_height, b_left, o_both)
		f['b'].mark = 80
			
if f.has_key('c'):
	if style == 1:
		setMargins(f['c'], half_x_height, o_both * 1.05 , None ) #------ Hardcoded, mejorable
		f['c'].rightMargin = c_right
		f['c'].mark = 80
	if style == 2:
		setMargins(f['c'], half_x_height, o_both * 1.05 , None ) #------ Hardcoded, mejorable
		f['c'].rightMargin = c_right
		f['c'].mark = 80
		
if f.has_key('d'):
	setMargins(f['d'], half_x_height, o_both, n_left)
	f['d'].mark = 80

if f.has_key('e'):
	if style == 1:
		setMargins(f['e'], half_x_height, o_both, None )
		f['e'].rightMargin = e_right
		f['e'].mark = 80
	if style == 2:
		setMargins(f['e'], half_x_height, o_both, None )
		f['e'].rightMargin = e_right
		f['e'].mark = 80
			
if f.has_key('f'):
	setMargins(f['f'], half_x_height, f_left, f_right)
	f['f'].mark = 80	
	
if f.has_key('g'):
	if gConstruction == 1: 
		f['g'].leftMargin = groman_left
		f['g'].rightMargin = groman_right
		f['g'].mark = 80
	if gConstruction == 2:
		setMargins(f['g'], half_x_height, o_both, n_right)
		f['g'].mark = 80	
	
if f.has_key('h'):
	if style == 1:
		setMargins(f['h'], half_x_height, n_left, n_right)
		f['h'].mark = 80
	if style == 2:
		setMargins(f['h'], half_x_height, h_left, n_right)
		f['h'].mark = 80
					
if f.has_key('i'):
	if style == 1:
		setMargins(f['i'], half_x_height, i_left, i_left)
		f['i'].mark = 80
	if style == 2:
		setMargins(f['i'], half_x_height, i_left, i_left)
		f['i'].mark = 80
		
if f.has_key('j'):
	if style == 1:
		setMargins(f['j'], half_x_height, i_left, i_left)
		f['j'].mark = 80
	if style == 2:
		setMargins(f['j'], half_x_height, i_left, j_right)
		f['j'].mark = 80
		
if f.has_key('k'):
	if style == 1:
		setMargins(f['k'], half_x_height, n_left, None)
		setMargins(f['k'], k_x_height, None, n_left )
		f['k'].mark = 80
	if style == 2:
		setMargins(f['k'], half_x_height, h_left, None)
		setMargins(f['k'], k_x_height, None, n_left )
		f['k'].mark = 80
		
if f.has_key('l'):
	if style == 1:
		setMargins(f['l'], half_x_height, l_left, l_left)
		f['l'].mark = 80
	if style == 2:
		setMargins(f['l'], half_x_height, h_left, l_right)
		f['l'].mark = 80

if f.has_key('m'):
	setMargins(f['m'], half_x_height, n_left, n_right)
	f['m'].mark = 80

if f.has_key('n'):
	setMargins(f['n'], half_x_height, n_left, n_right)
	f['n'].mark = 80

if f.has_key('o'):
	setMargins(f['o'], half_x_height, o_both, o_both)
	f['o'].mark = 80

if f.has_key('p'):
	if style == 1:
		setMargins(f['p'], half_x_height, n_left, o_both)
		f['p'].mark = 80
	if style == 2:
		setMargins(f['p'], half_x_height, p_left, o_both)
		f['p'].mark = 80
 
if f.has_key('q'):
	if style == 1:
		setMargins(f['q'], half_x_height, o_both, n_left)
		f['q'].mark = 80
	if style == 2:
		setMargins(f['q'], half_x_height, o_both, q_right)
		f['q'].mark = 80

if f.has_key('r'):
	setMargins(f['r'], half_x_height, n_left, None)
	f['r'].rightMargin = r_right
	f['r'].mark = 80

if f.has_key('s'):
	setMargins(f['s'], s1_x_height, s_left, None )
	setMargins(f['s'], s2_x_height, None, s_right )
	f['s'].mark = 80

if f.has_key('t'):
	f['t'].leftMargin = t_left
	f['t'].rightMargin = t_right
	f['t'].mark = 80	
	
if f.has_key('u'):
	setMargins(f['u'], half_x_height, u_left, n_left) #------ mejorable
	f['u'].mark = 80
		
if f.has_key('v'):
	setMargins(f['v'], v_x_height, n_right, n_left * 1.13) #------ Hardcoded, mejorable
	f['v'].mark = 80

if f.has_key('w'):
	setMargins(f['w'], w_x_height, n_right, n_left * 1.13) #------ Hardcoded, mejorable
	f['w'].mark = 80

if f.has_key('x'):
	f['x'].leftMargin = o_both * 0.66 #------ Hardcoded, mejorable
	f['x'].rightMargin = o_both * 0.71 #------ Hardcoded, mejorable
	f['x'].mark = 80

if f.has_key('y'):
	setMargins(f['y'], y_x_height, n_right, n_left * 0.99) #------ Hardcoded, mejorable
	f['y'].mark = 80
	
if f.has_key('z'):
	f['z'].leftMargin = o_both * 0.86 #------ Hardcoded, mejorable
	f['z'].rightMargin = o_both * 0.91 #------ Hardcoded, mejorable
	f['z'].mark = 80

# --- Done! ---
f.update()
print "Donde. Enjoy!"
print "Please review and tweek as needed"
print "-------------------------------------------"