a = " "
for i in range(1,101):
	if i %2 != 0 and i not in [5,7,93]:
		a += str(i) + "     "
print (a)
