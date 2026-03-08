ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tìm số ngày của tháng
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
elif thang == 2:
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        so_ngay = 29
    else:
        so_ngay = 28
else:
    so_ngay = 0

# Kiểm tra ngày hợp lệ
if so_ngay == 29:
    print("YES")
else :
    print("NO")

   