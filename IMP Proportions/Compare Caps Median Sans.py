#FLM: Compare Proportions Caps to Median Sans

# Description:
# Compare Caps Proportions to Median Sans Serif

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont
from robofab.interface.all.dialogs import Message

def compare_to_median(g, new_width):
	g.clearVGuides()
	g.clearHGuides()
	g.appendVGuide(new_width)
	if g.width == new_width:
		g.mark = 70
	if g.width < new_width:
		g.mark = 130
	if g.width > new_width:
		g.mark = 255	


# La fuente seleccionada es la que se va a modificar
f = CurrentFont()

# Mido mi n
H_base = f['H'].width

# Calculo el ancho que tendrian que tener las otras letras
a_median = round(93.1 * H_base / 100)
b_median = round(91.5 * H_base / 100)
c_median = round(90.6 * H_base / 100)
d_median = round(98.3 * H_base / 100)
e_median = round(80.7 * H_base / 100)
f_median = round(77.1 * H_base / 100)
g_median = round(97.5 * H_base / 100)
h_median = round(100.0 * H_base / 100)
i_median = round(41.7 * H_base / 100)
j_median = round(66.8 * H_base / 100)
k_median = round(90.9 * H_base / 100)
l_median = round(74.2 * H_base / 100)
m_median = round(120.9 * H_base / 100)
n_median = round(100.3 * H_base / 100)
o_median = round(101.8 * H_base / 100)
p_median = round(87.7 * H_base / 100)
q_median = round(102.0 * H_base / 100)
r_median = round(91.7 * H_base / 100)
s_median = round(80.8 * H_base / 100)
t_median = round(79.8 * H_base / 100)
u_median = round(98.4 * H_base / 100)
v_median = round(91.2 * H_base / 100)
w_median = round(132.2 * H_base / 100)
x_median = round(90.3 * H_base / 100)
y_median = round(87.6 * H_base / 100)
z_median = round(82.9 * H_base / 100)

print  a_median
print  b_median
print  c_median
print  d_median
print  e_median
print  f_median
print  g_median
print  h_median
print  i_median
print  j_median
print  k_median
print  l_median
print  m_median
print  n_median
print  o_median
print  p_median
print  q_median
print  r_median
print  s_median
print  t_median
print  u_median
print  v_median
print  w_median
print  x_median
print  y_median
print z_median

# Comparo y pinto
compare_to_median (f['A'], a_median)
compare_to_median (f['B'], b_median)
compare_to_median (f['C'], c_median)
compare_to_median (f['D'], d_median)
compare_to_median (f['E'], e_median)
compare_to_median (f['F'], f_median)
compare_to_median (f['G'], g_median)
compare_to_median (f['H'], h_median)
compare_to_median (f['I'], i_median)
compare_to_median (f['J'], j_median)
compare_to_median (f['K'], k_median)
compare_to_median (f['L'], l_median)
compare_to_median (f['M'], m_median)
compare_to_median (f['N'], n_median)
compare_to_median (f['O'], o_median)
compare_to_median (f['P'], p_median)
compare_to_median (f['Q'], q_median)
compare_to_median (f['R'], r_median)
compare_to_median (f['S'], s_median)
compare_to_median (f['T'], t_median)
compare_to_median (f['U'], u_median)
compare_to_median (f['V'], v_median)
compare_to_median (f['W'], w_median)
compare_to_median (f['X'], x_median)
compare_to_median (f['Y'], y_median)
compare_to_median (f['Z'], z_median)

#Updateo mi fuente		
f.update()

# Listo el pollo
print '------ Done ------';