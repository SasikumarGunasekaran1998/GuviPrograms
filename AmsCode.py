n = int(input()) #Getting the input
temp = n
count = 0
sums = 0
ren = n
check = n
while(temp>0): #counting number of digits
   temp = temp//10
   count = count + 1
for i in range ((count)):#Finding the armstrong number
   n = n % 10
   temp = n**3
   sums = sums + temp
   ren = ren//10
   n = ren
if(sums == check):
   print("yes")
else:
   print("no")
   
   
