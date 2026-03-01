import math
#ham rut gon phan so
def rut_gon_phan_so(tu:int, mau:int):
    ucln = math.gcd(tu, mau)
    tu_moi = tu// ucln
    mau_moi = mau// ucln
    return tu_moi, mau_moi

#goi lai ham de chay
if __name__ == "__main__":
    print(rut_gon_phan_so(6,21))
