

n = int(input("Nhập số bài kiểm tra: "))

ds = []
for i in range(n):
    ds.append(float(input))

ds.sort() #ds = [7, 8, 9]


# xóa điểm nhỏ nhất (nếu trùng thì xóa hết)
while ds.count(ds[0]) > 0:
    ds.remove(ds[0])

print("Danh sách điểm:", ds)

dem = 0
for d in ds:
    if d >= 8:
        dem += 1

print("Số điểm >= 8:", dem)
#ds = []
#ds.append(7) 
#ds.append(8)
#ds.append(9)
