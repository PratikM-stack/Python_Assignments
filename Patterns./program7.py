num=1
rows=int(input())
for i in range(1,rows+1):
    for j in range(i):
        print(num,end="\t")
        num+=1
    if num > 2:
        num-=1
    print()
