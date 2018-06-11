def func(hi,lo,div):
    lo_m = (lo // div) + 1
    hi_m = hi // div
    sum = (hi_m-lo_m+1)*(hi_m+lo_m)*7//2
    return sum

func(50, 0, 7)
