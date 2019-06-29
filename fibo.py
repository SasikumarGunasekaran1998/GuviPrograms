num = int(input())
n1 = 1
n2 = 1
for i in range(num):
    print(n1,end = ' ')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    

