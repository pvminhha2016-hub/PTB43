#@pvminhha2016
# ---------------------------------
# Kiểm tra tam giác
#a = int(input())
#b = int(input())
#c = int(input())

#if a + b <= c or a + c <= b or b + c <= a:
    #print("Khong phai tam giac")

#elif a == b and b == c:
    ##print("Tam giac deu")

#elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    #print("Tam giac vuong")

#elif a == b or a == c or b == c:
    #print("Tam giac can")

#else:
    #print("Tam giac thuong")

# ---------------------------------
# tìm giá trị lớn nhất, bé nhất

#s = input().split()

#ds = []
#for i in s:
    #ds.append(int(i))

#lon = ds[0]
#be = ds[0]

#for i in ds:
    #if i > lon:
        #lon = i
    #if i < be:
        #be = i

#print(lon)
#print(be)




# ---------------------------------
# Họ và tên
#s = input()
#ds = s.split()

#if len(ds) == 2:
    #print('Ho:',ds[0])   
    #print('Ten:', ds[1])
#else:
    #print('Ho:', ds[0])
    #print("Ten dem:"," ".join(ds[1:-1]))
    #print('Ten:', ds[-1])
#ds[0] : ho
#ds[1:-1]: ten dem
#ds[-1] : ten
#ds[1:-1] → ten dem
#ds[-1] → ten
# ---------------------------------
# ngày tháng năm
ngay = int(input())
thang = int(input())
nam = int(input())

if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
elif thang == 2:
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        so_ngay = 29
    else:
        so_ngay = 28
else:
    so_ngay = 0




