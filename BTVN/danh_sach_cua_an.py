#len(ds) + 1 → vì điểm cuối tính 2 lần nên tổng hệ số tăng thêm 1
#ds[-1] → lấy điểm cuối
#ds[:-1] → lấy tất cả điểm trừ điểm cuối

def tinh_trung_binh(ds):
    tong = 0
    for i in range(len(ds) - 1):
        tong += ds[i]
    tong += ds[-1] * 2
    trung_binh = tong / (len(ds) + 1)
    print("Trung bình điểm là:", trung_binh)


