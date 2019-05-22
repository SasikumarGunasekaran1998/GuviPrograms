n = int(input())
num = input().split()
l = len(num)
if(l!= n):
   print("Please enter the specfied value")
else:
   for i in range (n):
      for j in range(i,n):
         if(num[i] > num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
      print(num[i],end=' ')
    
         
      
