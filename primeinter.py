n,k = input().split() #Getting the input
n = int(n)
k = int(k)
for i in range(n,k + 1):
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i)
            
