n = int(input("Nhap so nguyen duong n:"))
if n > 0:
	tong = 0
	i = 1
	while i <= n:
		tong += i
		i += 1
else:
	print('So ban nhap kh phai la so nguyen duong')
print ("tong cac so nguyen duong la:\n"+str(tong))
