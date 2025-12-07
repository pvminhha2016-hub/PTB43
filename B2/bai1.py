### tam giac vuong * voi n  dong (>1)
#input n
n = input("so dong > 1: ")
n = int(n) #int
if (n < 2):
    print("so dong phai lon hon 1" )
else:
# tao cam giac vuong
    for i in range(1, n+1):
        print(" * "*i)
#hoi thong tin
input("ho ten:  ")
input("ngay sinh: ")
input("que quan")
input("so thich")