#------------------------------------------------------
def print_str(s):
    for i in range(len(s)):
        for j in range(i + 1):
            print(s[j], end ="")
        print()

print_str(input("nhap choi"))
