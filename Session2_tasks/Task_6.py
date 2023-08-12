# find the largest num in a list

nums=[]

x=int(input("Enter number of Elements : "))

for i in range(0,x):
    num=int(input())
    nums.append(num)

nums.sort()
print("The max num is ",nums[-1])