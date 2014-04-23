#FLM: Compare Proportions Lowercase to Median Sans

# Description:
# Compare Lowercase Proportions to Median Sans Serif

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
n_base = f['n'].width

# Calculo el ancho que tendrian que tener las otras letras
a_median = round(93.5 * n_base / 100)
b_median = round(100.7 * n_base / 100)
c_median = round(85.0 * n_base / 100)
d_median = round(100.5 * n_base / 100)
e_median = round(93.7 * n_base / 100)
f_median = round(59.7 * n_base / 100)
g_median = round(98.2 * n_base / 100)
h_median = round(100.0 * n_base / 100)
i_median = round(46.5 * n_base / 100)
j_median = round(46.7 * n_base / 100)
k_median = round(91.9 * n_base / 100)
l_median = round(46.8 * n_base / 100)
m_median = round(151.0 * n_base / 100)
n_median = round(100.0 * n_base / 100)
o_median = round(99.1 * n_base / 100)
p_median = round(100.5 * n_base / 100)
q_median = round(100.5 * n_base / 100)
r_median = round(66.7 * n_base / 100)
s_median = round(80.6 * n_base / 100)
t_median = round(63.9 * n_base / 100)
u_median = round(100.0 * n_base / 100)
v_median = round(88.7 * n_base / 100)
w_median = round(133.5 * n_base / 100)
x_median = round(88.4 * n_base / 100)
y_median = round(89.6 * n_base / 100)
z_median = round(82.3 * n_base / 100)
space_median = round(41.1 * n_base / 100)

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
print space_median

# Comparo y pinto
compare_to_median (f['a'], a_median)
compare_to_median (f['b'], b_median)
compare_to_median (f['c'], c_median)
compare_to_median (f['d'], d_median)
compare_to_median (f['e'], e_median)
compare_to_median (f['f'], f_median)
compare_to_median (f['g'], g_median)
compare_to_median (f['h'], h_median)
compare_to_median (f['i'], i_median)
compare_to_median (f['j'], j_median)
compare_to_median (f['k'], k_median)
compare_to_median (f['l'], l_median)
compare_to_median (f['m'], m_median)
compare_to_median (f['n'], n_median)
compare_to_median (f['o'], o_median)
compare_to_median (f['p'], p_median)
compare_to_median (f['q'], q_median)
compare_to_median (f['r'], r_median)
compare_to_median (f['s'], s_median)
compare_to_median (f['t'], t_median)
compare_to_median (f['u'], u_median)
compare_to_median (f['v'], v_median)
compare_to_median (f['w'], w_median)
compare_to_median (f['x'], x_median)
compare_to_median (f['y'], y_median)
compare_to_median (f['z'], z_median)
compare_to_median (f['space'], space_median)

#Updateo mi fuente		
f.update()

# Listo el pollo
print '------ Done ------';