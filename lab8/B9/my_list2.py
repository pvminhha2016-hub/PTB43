danh_sach1 = [1, "a", "abcd123456", 12.3, False
              ]
#----------------------------------------------------------------------------------------------------------------------------------
#duyet danh sach
for i in range(len(danh_sach1)):
    print(danh_sach1[i])

#dung khi ko can index
for value in danh_sach1:
    print(value)

#----------------------------
#them phan tu
#append(value): them vao cuoi phan tu
danh_sach1.append(100)
print(danh_sach1)
#index : them vao vi tri index
danh_sach1.insert(len(danh_sach1)-1, "new")
print(danh_sach1)
#-----------
# sua phan tu
danh_sach1[4] = "updataed item"
print(danh_sach1)
#xoa phan tu
#pop(): xoa o vi tri cuoi cung cua danh sach -> tra ve phan tu bi xoa
del_item = danh_sach1.pop()
print(f"{del_item} da dc xoa khoi danh sach{danh_sach1}")
#pop index : xoa o vii tri index -> tra ve phan tu bi xoa
del_item = danh_sach1.pop(-1)
print(f"{del_item} da dc xoa khoi danh sach{danh_sach1}")
#NOTE   : remove tra ve loi neu ko co phan tu nay
del_item_2 = danh_sach1.remove(-1)
print(danh_sach1)
#clear():  xoa het danh sach
print(danh_sach1.clear())
#sap xep danh sach
#sort : neu ? la  Fale : trang dan | 
#NOTE:neu muon sap xep -> cung kieu du lieu
danh_sach2 = ["a", "m", "A", "x", "-"]
danh_sach2.sort(reverse=True)
print(danh_sach2)#giam
danh_sach2.sort(reverse=False)
print(danh_sach2)#tang

