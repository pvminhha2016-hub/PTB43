# 1. Tính trung bình cộng
def trung_binh(ds):
    return sum(ds) / len(ds)

# 2. Tìm điểm lớn thứ hai
# nhập số lượng điểm
n = int(input("Nhập số lượng điểm: "))

ds = []

# nhập từng điểm
for i in range(n):
    diem = int(input("Nhập điểm: "))
    ds.append(diem)

# 1. tính trung bình
def trung_binh(ds):
    return sum(ds) / len(ds)

# 2. tìm điểm lớn thứ hai
def lon_thu_hai(ds):
    ds.sort()
    return ds[-2]

# 3. đổi điểm <=5 thành 9
def cai_thien(ds):
    for i in range(len(ds)):
        if ds[i] <= 5:
            ds[i] = 9
    return ds

print("Trung bình:", trung_binh(ds))
print("Điểm lớn thứ hai:", lon_thu_hai(ds))
print("Danh sách sau khi cải thiện:", cai_thien(ds))