inp = input()
x = len(inp)
count = 0
for i in inp:
    if(i == " "):
        count = count+1

print(x-count)
