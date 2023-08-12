# count the number 4 in a given list

count = 0

nums=[]

x=int(input("Enter number of Elements : "))

for i in range(0,x):
    num=int(input())
    nums.append(num)

for num in nums:
    if(num==4):
        count+=1


print("The number of occurrences = ",count)
