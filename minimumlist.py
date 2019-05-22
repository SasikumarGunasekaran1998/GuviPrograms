n = int(input())
num = input().split()
l = len(num)
if(l!= n):
   print("Please enter the specfied value")
else:
   for i in range (n):
         count = 0
         for j in range(n):
            if(int(num[i])>0):
               if(num[i] < num[j]):
                  count = count+1
               if(count>=n-1):
                  print(num[i])
                  break
            else:
               if(num[i] > num[j]):
                  count = count+1
               if(count>=n-1):
                  print(num[i])
                  
               
