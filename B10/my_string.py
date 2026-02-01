#--------------------------------------------------------
#khai bao sau ki tu
chuoi_rong = " "
full_name = "duy"
#--------------------------------------------------------
#duyet xau
#try cap phan tu
print(len(chuoi_rong))
print(len(full_name))
#--------------------------------------------------------
#noi xau ki tu
for chart in full_name:
    print(chart, end="")

for index in range(len(full_name)):
    #truy cap phan tu
    print(f"{index}: {full_name[index]}")    
    #xau ki tu
sentence = "my full name is " + full_name + "."
print(sentence)
#--------------------------------------------------------
# xau con
firsNAME = "duy"
lastNAME = "duc"
#--------------------------------------------------------
#tim xau con trong danh sach
print(firsNAME in full_name)
print(lastNAME in full_name)
#chinh kieu cho str
print(full_name.lower())
print(full_name.upper())
print(full_name.capitalize())
#--------------------------------------------------------
#tim vi tri xau con
d_index = full_name.find("d")
print(d_index)
#NOTE
k_index = full_name.find("k", 4)
print(k_index)
#--------------------------------------------------------
#str -> list 
name_list = full_name.split(" ")
print(name_list)
#--------------------------------------------------------
#thay doi phan tu
newNAME = full_name.replace("ky", "duy", 1)
print(newNAME)





