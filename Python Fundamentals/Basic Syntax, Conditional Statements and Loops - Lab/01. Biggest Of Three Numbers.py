fnum = int(input())
snum = int(input())
tnum = int(input())

if fnum > snum and fnum > tnum:
	print(fnum)
elif snum > fnum and snum > tnum:
	print(snum)
else:
	print(tnum)