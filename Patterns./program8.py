num=1
var=1
for i in range(1,5):
    var+=1
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()
    num=i+num+var
