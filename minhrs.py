mins = int(input())
temp = mins
hrs = (1/60)*mins
if hrs >= 1:
    hrs = int(hrs)
    mins =int(temp%60)
    print(hrs,end = " ")
    print(mins)
else:
    print(0,end = " ")
    print(mins)

    
