#__________________________________________________________________________
##ham ko co tra ve ko
def hello():
    name = input("nhap ten cua ban")
    print(f"Hi {name}")
#__________________________________________________________________________
#ham co tra ve
def sum_two_num():
    a = int(input("nhap so thu nhat:"))
    b = int(input("nhap so thu hai:"))
    return a + b
#__________________________________________________________________________
#ham co tham so/parameters
def duplicate_str(s:str, n:int):
    return s * n
#__________________________________________________________________________
#global
global_count = 0
def cuonter_to_n(n: int):#khai bao de su dung
    print(global_count) #in ra ngoai
    for i in range(n+1):
        global_count += 1
    print(global_count)
#__________________________________________________________________________
#goi ham de chay
if __name__=="___main___":   
    #hello()
    #######print(sum_two_num())
    print(duplicate_str("a", 3))   