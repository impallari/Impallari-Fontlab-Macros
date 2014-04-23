#FLM: Measure Caps as percent on H

# Description:
# Measure uppercase widths as a percent of H
# all open fonts

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import os.path
from robofab.world import AllFonts
from robofab.interface.all.dialogs import PutFile

# Campos
text = []
text.append( 'Font; UPM; A; B; C; D; E; F; G; H; I; J; K; L; M; N; O; P; Q; R; S; T; U; V; W; X; Y; Z; space' )
	
# Measure
for f in AllFonts():

	base = f['H'].width
	a_percent = '%.1f' %(f['A'].width * 100.0 / base)
	b_percent = '%.1f' %(f['B'].width * 100.0 / base)
	c_percent = '%.1f' %(f['C'].width * 100.0 / base)
	d_percent = '%.1f' %(f['D'].width * 100.0 / base)
	e_percent = '%.1f' %(f['E'].width * 100.0 / base)	
	f_percent = '%.1f' %(f['F'].width * 100.0 / base)
	g_percent = '%.1f' %(f['G'].width * 100.0 / base)
	h_percent = 100
	i_percent = '%.1f' %(f['I'].width * 100.0 / base)
	j_percent = '%.1f' %(f['J'].width * 100.0 / base)
	k_percent = '%.1f' %(f['K'].width * 100.0 / base)
	l_percent = '%.1f' %(f['L'].width * 100.0 / base)
	m_percent = '%.1f' %(f['M'].width * 100.0 / base)
	n_percent = '%.1f' %(f['N'].width * 100.0 / base)
	o_percent = '%.1f' %(f['O'].width * 100.0 / base)
	p_percent = '%.1f' %(f['P'].width * 100.0 / base)
	q_percent = '%.1f' %(f['Q'].width * 100.0 / base)
	r_percent = '%.1f' %(f['R'].width * 100.0 / base)
	s_percent = '%.1f' %(f['S'].width * 100.0 / base)
	t_percent = '%.1f' %(f['T'].width * 100.0 / base)
	u_percent = '%.1f' %(f['U'].width * 100.0 / base)
	v_percent = '%.1f' %(f['V'].width * 100.0 / base)
	w_percent = '%.1f' %(f['W'].width * 100.0 / base)
	x_percent = '%.1f' %(f['X'].width * 100.0 / base)
	y_percent = '%.1f' %(f['Y'].width * 100.0 / base)
	z_percent = '%.1f' %(f['Z'].width * 100.0 / base)
	space_percent = '%.1f' %(f['space'].width * 100.0 / base)

	#Armar Texto
	text.append( 
		str(f.info.familyName) + ' ' + str(f.info.styleName) + '; ' + 
		str(f.info.unitsPerEm) + '; ' + 
		str(a_percent) + '; ' + 
		str(b_percent) + '; ' + 
		str(c_percent) + '; ' + 
		str(d_percent) + '; ' + 
		str(e_percent) + '; ' + 
		str(f_percent) + '; ' + 
		str(g_percent) + '; ' + 
		str(h_percent) + '; ' + 
		str(i_percent) + '; ' + 
		str(j_percent) + '; ' + 
		str(k_percent) + '; ' + 
		str(l_percent) + '; ' + 
		str(m_percent) + '; ' + 
		str(n_percent) + '; ' + 
		str(o_percent) + '; ' + 
		str(p_percent) + '; ' + 
		str(q_percent) + '; ' + 
		str(r_percent) + '; ' + 
		str(s_percent) + '; ' + 
		str(t_percent) + '; ' + 
		str(u_percent) + '; ' + 
		str(v_percent) + '; ' + 
		str(w_percent) + '; ' + 
		str(x_percent) + '; ' + 
		str(y_percent) + '; ' + 
		str(z_percent) + '; ' + 
		str(space_percent)
	)

# Save File
text = '\n'.join(text)
path = PutFile('Save file as:')
if path:
    file = open(path, 'w')
    file.write(text)
    file.close()
    
# Done!
print "Done!"