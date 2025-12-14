# nhap s, h, p
hour = 0
minute = 0
second = input("nhap so giay")

#chuyển kiểu dữ liệu
second = int(second)

#tinh toan
hour = second // 3600
minute =    (second % 3600 ) // 60
# pham le cu phut -> giay/S
second = (second% 3600 ) % 60

print(f"{hour}:{minute}:{second}")
