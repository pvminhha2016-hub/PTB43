#inputday diem
day_diem = input("nhap day diem (o -> 10, cach = ' '):")
diem_parts = day_diem.split(' ')
# nhap sai format ( ko phai so hoac ngoai khoang 0-10)
while True:
    valid = True
    for diem in diem_parts:
        diem = float(diem)
        if not (0 <= diem <= 10):
            valid = False
            break

    if not valid:
        day_die = input("nhap lai  day diem (0 -> 10, cach = '' ):")
        day_diem= day_diem.split()
        diem_parts = day_diem.splid(' ')
    else:
        count_10 = 0
        #out diem = 10
        for diem in diem_parts:
            diem = format(diem)
            if diem == 10:
                count_10 += 1 

        print(f"so diem 10 la : {count_10}") if count_10 > 0 else print("ko co diem 10")
        break
                















