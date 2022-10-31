def sq_num(l):
    for i in l:
        print(i**2,end=" ")

n=[int(e) for e in range(1,31)]
print(sq_num(n))