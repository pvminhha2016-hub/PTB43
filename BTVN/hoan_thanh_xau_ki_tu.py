def tao_xau(s, i=1):
    if i > len(s):
        return
    print(s[:i])
    tao_xau(s, i + 1)

# Test
tao_xau("MindX")
