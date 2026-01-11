#input = n
#output = day so tu 1 -> (sum > n)
n = -1
while n < 0:
    # neu n < 0 thi yeu cau pham lai
    n = int(input("nhap n (n > 0):"))

sum = 0
i = 0
print(" day so tu 1 den khi tong vuot qua n: " , end= '')
while sum <= n:
    sum += i
    print(i, end= ' ')
    i += 1