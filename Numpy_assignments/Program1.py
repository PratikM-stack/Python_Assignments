import numpy as np
def altSum(arr):
    sumEle=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i+j)% 2==0:
                sumEle+=arr[i][j]
    return sumEle
row=int(input("enter row:"))
column=int(input("enter columns:"))
arr=np.zeros((row,column),int)
print("enter elements row wise:")
for i in range(row):
    for j in range(column):
        arr[i][j]=int(input())
        
sumEle=altSum(arr)
print("alternate sum: ", sumEle)
