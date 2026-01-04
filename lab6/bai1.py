## tinh tong cac so tu 1 den n  la so nguyen (0<n)  va (int)
n = -1
while n <= 0:
    n = int(input("nhap so nguyen n  > 0: "))

tong = 0
## muon chay chan -> start: so chan + chay chan2
for i in range(2, n + 1,2):
    tong += i 

print(f" tong cac so chan tu 1 den {n} la: {tong}")