inp = input().split()
l = len(inp)
count = 0
for i in range(l):
    inp[i] = int(inp[i])
    count = 0
    for j in range(l):
        inp[j] = int(inp[j])
        if(inp[i]>=inp[j]):
            count = count+1
    if(count >= (l)):
        print(inp[i])
        break
