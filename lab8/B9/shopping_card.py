cart = []
funcs = [
    "0. in gio hang"
    "1.them vao gio",
    "2. chinh sua mon hang",
    "3. xoa mon hang",
    "4. sap xep theo ten ",
    "5. thoat chuong trinh"
         ]

#bat dau chuong trinh
print("----------------shopping----------------")
while True:
    # in danh sach tinh nang
    for value in funcs:
        print(value)
    #chon 1 chuc nang
    choice = int(input("chon 1 chuc nang:"))
    # neu ko chon dung -> bao loi
    while (choice > 5 or choice < 0):
        choice = int(input(" chon 1 chuc nang (0 -> 5):"))

    # funcs 5 :
    if choice == 5:
        print("bye")
        break

 # funcs 0 :
    if choice == 0:
        if len(cart) == 0:
            print("gio hang rong ")
        continue
        for i in range(len(cart)):
            print(f"{i}: {cart[i]}")
#funcs1:
    elif choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass

