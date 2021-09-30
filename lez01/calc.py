#calculator.py

def sum(m, n):
	res = m
	step = 1 if n > 0 else -1
	for i in range (abs(n)):
		res+=step
	return res

def divide(m, n):
	if (n==0):
		return "inf"
	nmin = 1
	if (n<0):
		n = abs(n)
		nmin = -1
	mmin = 1
	if (m<0):
		m = abs(m)
		mmin = -1
	res = 0
	while m >= n:
		m = m - n
		res += 1 
	return nmin*mmin*res
