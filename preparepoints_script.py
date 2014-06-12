def cook(scriptOP):
	scriptOP.clear()
	indat = scriptOP.inputs[0]
	scriptOP.appendRow(('P(0)', 'P(1)', 'P(2)', 'Cd(0)', 'Cd(1)', 'Cd(2)', 'Cd(3)'))
	if indat.numRows == 0:
		return
	for i in range(1, indat.numRows):
		a = indat[i, 'a'].val
		scriptOP.appendRow((indat[i, 'tx'], indat[i, 'ty'], indat[i, 'tz'], a, a, a, a))
