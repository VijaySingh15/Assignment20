def unique_ilst(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_ilst([1,2,3,3,3,4,5]))