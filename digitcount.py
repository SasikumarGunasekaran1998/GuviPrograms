num = int(input()) #Get the input
digit = 0
while(num > 0):
    num = num // 10 #integer value of the quotient
    digit = digit + 1
print(digit)
