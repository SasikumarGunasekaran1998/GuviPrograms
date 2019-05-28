inp = input()
count = 0
for i in inp:
    if( i.isalpha() or i.isnumeric()):
        x = 0
    else:
        count = count+1
print(count)
