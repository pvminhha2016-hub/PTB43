
tong_so_nt = 0
print("Các số nguyên tố bé hơn 100 là:")
for so_canxet in range(2, 101):
    la_so_nt = True
    for  so_chia in range(2, (so_canxet//2 + 1)):
        if so_canxet % so_chia == 0:
            la_so_nt = False
            break

    if la_so_nt == True:   # chỉ chia hết cho 1 và chính nó
        
        tong_so_nt += so_canxet
        print(i, end=" ")
print("\nTổng các số nguyên tố là:", tong_so_nt)



















    


#dem dùng để kiểm tra xem một số có phải là số nguyên tố hay không.