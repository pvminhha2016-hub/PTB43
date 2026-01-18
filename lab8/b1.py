#xac dinh tam giac
#input nhap do dai 3 canh
a = -1
b = -1
c = -1
while (a and b and c) <= 0:
   print("----------------------------")
   print("  nhap do dai a,b,c < 0")
   a = int(input(" nhap do dai canh a (a > 0):   "))
   b = int(input(" nhap do dai canh a (b > 0):   "))
   b = int(input(" nhap do dai canh a (c > 0):   "))
if a + b > c and a + c > b and b + c > a:
   print(" la hinh tam giac")
else:
   print("ko phai hinh tam giac")