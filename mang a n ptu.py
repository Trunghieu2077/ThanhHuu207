a = int(input("Nhap danh sach gom cac Phan Tu:"))
b = []
Tong = 0
for i in range (a):
    b = int(input("Nhap so thu "+str(i+1) +":"))
    for k in [b]:
        Tong += k
print (("Tong cua cac phan tu da nhap:")+str(Tong))
