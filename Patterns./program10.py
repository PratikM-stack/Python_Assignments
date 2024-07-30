num=69
for i in range(1,6):
    for j in range(6-i):
        print(chr(num),end=" ")
        num+=1
    print()
    num=69
    num-=i
