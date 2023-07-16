n = int(input("Nhap so nguyen duong n:"))
TongGiaiThua = 1
if n >= 1:
	for i in range (1,n+1):
		TongGiaiThua *= i
else:
	print ("Khong the tinh giai thua cua so am")
print ('Giai thua cua so ban da nhap la: \n'+str(TongGiaiThua))
