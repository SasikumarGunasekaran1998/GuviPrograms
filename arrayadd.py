num = list()
n,k = input().split()
k = int(k)
n = int(n)
sum = 0
for count in range (0,n):
    n = int(input())
    num.append(int (n)) 
for count in range(0,k):
    sum = sum + num[count]
print (sum)
    
