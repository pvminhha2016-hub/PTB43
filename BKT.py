
tien_dien = int(input("nhap so dien tu 0 den 50: " ))

if (tien_dien <= 50 ):
    print(tien_dien * 1700)
elif tien_dien <= 100:
    print(tien_dien * 1900)
elif tien_dien <= 200:
    print(tien_dien * 2100)
else:
    print(tien_dien * 3000)

