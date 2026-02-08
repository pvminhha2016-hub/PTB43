#input ddd nnn mmmm
date_str = int("nhap nhay thang nam(dd/mm/yy)")
date_parts = date_str.split("/")

while len(date_parts) != 3:
    date_str = input("nhap nhay thang nam(dd/mm/yy")
    date_parts = date_str.split("/")
#kiem tra ngay/thang/nam co hop le ko
day = int(date_parts[0])
month = int(date_parts[1])
year =  int(date_parts[2])

if not (1 <= day <= 31 ) or not (1 <= month <= 12 ) or year < 0:
    print("ngay thang nam ko hop le")
else:
    #out ngay dd , thang  nam 
    print(f"ngay {day:02d}, thang{month:02d}, nam{year}")






