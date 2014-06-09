def tableChange(dat):
	v = op("settings")["variation"]
	s1 = 1 + remap(tdu.rand(me.time.absFrame), 0, 1, -v, v)
	s2 = 1 + remap(tdu.rand(me.time.absFrame * 137), 0, 1, -v, v)
	op("fifo1").appendRow(dat.row(0) + [s1, s2])
	return

def remap(old_value, old_min, old_max, new_min, new_max):
	return ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min