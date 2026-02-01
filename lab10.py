danh_sach_diem = []
#them diem 
so_bai_kiem_tra = int(input("nhap so bai kiem tra"))
while so_bai_kiem_tra:
    so_bai_kiem_tra = int(input("nhap  lai so bai kiem tra:"))
for i in range( so_bai_kiem_tra):
    diem = float(int(f"nhap bai kiem  {i + 1} "))
    while diem < 0:
        diem =float(int(f"nhap lai bai kiem tra {i + 1} "))
        #them vao danh sach
        danh_sach_diem.append(diem)


print("danh sach diem: ", danh_sach_diem)
# 1. Sắp xếp danh sách điểm số theo chiều tăng dần 
danh_sach_diem.sort(reverse=False)
#.2Xoá số điểm nhỏ nhất (Nếu có hai số điểm nhỏ nhất thì xoá cả hai)
if  (so_bai_kiem_tra == 1) : print("ko the xoa do  danh sach 1 phan tu ")
else:
    diem_nn = min(danh_sach_diem)
    #lap lai cho toi khi xo Het diem nho nnhat
    while diem_nn in danh_sach_diem:
        danh_sach_diem.remove(diem_nn)
        print("da xOa diem nho nhat",diem_nn)
        print("danh sach sau khi bi xoa ", danh_sach_diem)
#3. Xuất danh sách điểm sau khi đã xử lý yêu cầu 1 và 2
#4. Đếm số lượng điểm lớn hơn hoặc bằng 8 và xuất ra màn hình
cuonter = 0
for value in danh_sach_diem:
    if value >= 8 : cuonter += 1
print("so loung diem >=  8", cuonter)

danh_sach_diem_lon_hon8 = [value for value in danh_sach_diem if value >= 8]
print(len(danh_sach_diem_lon_hon8))