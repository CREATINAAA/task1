lst = [2, 4, 3]
lst2 = [5, 6, 4]
lst_new = []
for i in range(len(lst)):
    count = 0
    count += lst[i] + lst2[i]
    count = str(count)
    if i + 1 < len(lst) and len(count) > 1:
        count = count[len(count) - 1]
        lst[i + 1] = int(lst[i + 1]) + int(count[0])
    lst_new.append(count)
print(lst_new)
