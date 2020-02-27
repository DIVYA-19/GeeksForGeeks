array = list(map(int, input().split()))

stack = []
res = []

for i in range(len(array)):
    while len(stack)>0 and stack[-1] > array[i]:
        del stack[-1]

    if len(stack) == 0:
        res.append(None)

    elif stack[-1] < array[i]:
        res.append(stack[-1])
    
    stack.append(array[i])

print(res)
