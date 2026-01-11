import math
#input: a,b
a = 0
b = 0
while(a and b ) == 0:
    a = int(input("nhap tu so"))
    b = int(input("nhap mau so"))

# tinh BCNN
bcnn = math.lcm(a. b)
print(f"BCNN cua  {a} va {b} la: {bcnn}")

#rut gon 
print(f"phan so ban dau: {a} va {b}")
ucln = math.gcd(a,b)
a == a//ucln
b == b//ucln
print(f"phan so rut gon {a}/{b}")