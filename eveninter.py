n,k = input().split()
n = int(n)
k = int(k)
for i in range(n,(k-1),1):
    n = n+1
    if(n%2 == 0):
        print(n , end = ' ')
    
