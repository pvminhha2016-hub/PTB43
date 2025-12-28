# ứng dụng tạo
# cách chơi
#1 start
#2.neit
#3.skip (countnue)
#3.nhập số câu hỏi
#$ nếu trả lời sai
#-----------------------
import random

#bắt đầu chơi
while True:
    choice = input("nhập 'start' để chơi,   'neit' để thoát: ")
    choice = choice.lower().strip()
    if choice == 'neit':
        print("chương trình kết thúc byeeeeeeee")
        break
    if choice != 'start':
        print("lựa chọn ko hợp lệ")
        continue
#số lượng câu hỏi
# input : n 
n = int(input("nhặp ssos lượng câu hỏi"))
while n <= 0:
    print("số lượng câu hỏi lớn hon 0")
    n = int(input("nhập lại số luownhj câu hỏi:"))
    # tạo tạo câu hỏi dựa trên số lượng câu
for so_lan in range(1, n + 1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    correct = a + b
    # in câu hỏi
    question = f"{a} + {b} = "
    # kien tra cau hoi
    while(ans == ""):
        ans = input(question)
        if ans.lower().strip() == "skip":
            print("bỏ qua câu hỏi này")
            break
        if int(ans) == correct:
            print("đúng")
            break
        else:
            print("sai xx")
            ans = " "