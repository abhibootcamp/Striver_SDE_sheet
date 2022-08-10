def printPascal(n:int):
    res = []
    if n > 0:
        res.append([1])
    n -= 1
    if n > 0:
        res.append([1,1])
    n -= 1
    cnt = 2
    while n > 0:
        sub_list = []
        sub_list.append(1)
        for i in range(1, cnt):
            sumi = res[cnt-1][i-1] + res[cnt-1][i]
            sub_list.append(sumi)
        sub_list.append(1)
        res.append(sub_list)
        cnt += 1
        n -= 1
    return res
