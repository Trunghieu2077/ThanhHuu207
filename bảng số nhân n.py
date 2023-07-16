n = int(input("Nhap so nguyen duong n:"))
if n >= 1:
	for i in range (1,11):
		print (str(n)+ " Nhan "+str(i)+" Bang: "+ str(n*i))
else:
	print("So Ban Nhap Khong Phai La So Nguyen Duong")
