#FLM: Measure Lower as percent on n

# Description:
# Measure lowercase widths as a percent of n
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
text.append( 'Font; UPM; a; b; c; d; e; f; g; h; i; j; k; l; m; n; o; p; q; r; s; t; u; v; w; x; y; z; space' )
	
# Measure
for f in AllFonts():

	base = f['n'].width
	a_percent = '%.1f' %(f['a'].width * 100.0 / base)
	b_percent = '%.1f' %(f['b'].width * 100.0 / base)
	c_percent = '%.1f' %(f['c'].width * 100.0 / base)
	d_percent = '%.1f' %(f['d'].width * 100.0 / base)
	e_percent = '%.1f' %(f['e'].width * 100.0 / base)	
	f_percent = '%.1f' %(f['f'].width * 100.0 / base)
	g_percent = '%.1f' %(f['g'].width * 100.0 / base)
	h_percent = '%.1f' %(f['h'].width * 100.0 / base)
	i_percent = '%.1f' %(f['i'].width * 100.0 / base)
	j_percent = '%.1f' %(f['j'].width * 100.0 / base)
	k_percent = '%.1f' %(f['k'].width * 100.0 / base)
	l_percent = '%.1f' %(f['l'].width * 100.0 / base)
	m_percent = '%.1f' %(f['m'].width * 100.0 / base)
	n_percent = 100
	o_percent = '%.1f' %(f['o'].width * 100.0 / base)
	p_percent = '%.1f' %(f['p'].width * 100.0 / base)
	q_percent = '%.1f' %(f['q'].width * 100.0 / base)
	r_percent = '%.1f' %(f['r'].width * 100.0 / base)
	s_percent = '%.1f' %(f['s'].width * 100.0 / base)
	t_percent = '%.1f' %(f['t'].width * 100.0 / base)
	u_percent = '%.1f' %(f['u'].width * 100.0 / base)
	v_percent = '%.1f' %(f['v'].width * 100.0 / base)
	w_percent = '%.1f' %(f['w'].width * 100.0 / base)
	x_percent = '%.1f' %(f['x'].width * 100.0 / base)
	y_percent = '%.1f' %(f['y'].width * 100.0 / base)
	z_percent = '%.1f' %(f['z'].width * 100.0 / base)
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