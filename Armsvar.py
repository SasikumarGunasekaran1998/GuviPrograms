n,k = input().split() #Getting the input
n = int(n)
k = int(k)
for i in range (n,(k),1):
   sum = 0
   temp = i
   check = i
   use = i
   while(temp>0):
      use = use % 10
      t = use**3
      sum = sum + t
      temp = temp//10
      use = temp
   if(sum == check):
      print(sum)
   
      
      
      
      
   
   
   
