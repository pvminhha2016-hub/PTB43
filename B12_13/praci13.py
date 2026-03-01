#def inthong_tin(ten, giolam, luongtheogio, tonhluong):
    #print(" thong tin cua nhan vien")
#ten = input("ten nhan vien")
#giolam = input("so gio lam viec")
#luongtheogio = input("so luong lam dc tronh gio")
#tonhluong = print(giolam * luongtheogio)
def tinhluong(giolam,luongtheogio):
    return giolam*luongtheogio
def inthong_tin(ten, giolam, luongtheogio, tonhluong):
    print("Ten:", ten)
    print("giolam:", giolam)
    print("luonggio:",luongtheogio)
    print("tongluong:", tonhluong)

tongluong = tinhluong(12, 150)
inthong_tin(" ten ", 12, 150, tongluong)