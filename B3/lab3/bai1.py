#
cau_kiem_tra = input("nhap so cau kiem tra")
so_hoc_sinh = input("nhap so hoc sinh ")

#chuyển số học sinh
cau_kiem_tra = int(cau_kiem_tra)
so_hoc_sinh = int(so_hoc_sinh)

#kết luận 
print(f"""mỗi học sinh sẽ dc lam {cau_kiem_tra//so_hoc_sinh}câu kiểm tra còn dư {cau_kiem_tra%so_hoc_sinh}câu kiểm tra""")