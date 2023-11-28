dic = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}
lst = []
numb = '234'
our_combination = ''
count = 0
for key in range(0, len(numb)):
    for v in dic[int(numb[key])]:
        our_combination = v
        if key + 1 < len(numb):
            for i in range(0, len(numb)):
                if i + 1 < len(numb):
                    for c in dic[int(numb[i + 1])]:
                        our_combination += c
                        if our_combination not in lst:
                            lst.append(our_combination)

print(lst)
