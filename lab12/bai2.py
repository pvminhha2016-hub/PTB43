# tinh diem trung binh

def tinh_diem_tb(ds_diem_str):
    #chuyen string -> list
    ds_diem = ds_diem_str.split(" ")
    #chuyen het phan tu sang float
    for i in range(len(ds_diem)):
        ds_diem[i] = float(ds_diem[i])
        if ( not (0 <= ds_diem[i] <= 10 )):
            print("danh sach co diem ko hop le") 
            return #ket thuc

    #tinh diem tb
    result = sum (ds_diem, ds_diem[len(ds_diem) - 1])/(len(ds_diem) + 1)
    return round(result, 1)

print(tinh_diem_tb(input()))



