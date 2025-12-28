##lặp lịa hữu hạn
## ragen(start, stop, step)
#lap lai trong khoang tu <start> -> <stop - 1>, bước nhảy là <step> đơn vị
#---------------
#lap lại từ 0 đén stop
#rangen(start, stop): lặp lịa từ start -> stop -> 1 mặc định nhảy la 1
## ragen(start, stop, step)

#countdown 10s happy new year
import time

for giay in range(10, 0, -1):
    print(giay)
    time.step(1)
    print("hapyyy new year")

# ve tam giac
canh = 5    
for dong in range(1, canh):
    print("* "*dong)
for cach in range(cach, 0, -1):
    print(" " * (cach-dong) + "0 " * dong)

    print("merry christams")

