hrs,mins = input().split()
hrs = int(hrs)
mins = int(mins)
hr,mi = input().split()
hr = int(hr)
mi = int(mi)
if(hrs>hr):
    print((hrs-hr),end = " ")
else:
    print((hr-hrs),end = " ")
if(mins>mi):
    print((mins-mi))
else:
    print((mi-mins))
    
