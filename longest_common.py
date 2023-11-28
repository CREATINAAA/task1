lst = ["flower", "flow", "flight"]
n = len(lst)
if (n < 2):
    print(lst[0])

commonPrefix = []

for charIndex, char in enumerate(lst[0]):
    needToTerminate = False
    for i in range(1, n):
        if ((charIndex == len(lst[i])) or (char != lst[i][charIndex])):
            needToTerminate = True
            break
    if (needToTerminate):
        break
    commonPrefix.append(char)

print(commonPrefix)
