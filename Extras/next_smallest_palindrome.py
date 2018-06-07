def pal(num):
    n = str(num)
    X = len(n)//2
    Y = X+(len(n)&1)
    first = n[:X][::-1] 
    second = n[Y:] 
    Z = n[:Y]
    if int(first) > int(second):
        return Z+first
    else:
        temp = str(int(Z)+1)
        return int(temp+temp[:X][::-1])
