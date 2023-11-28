numb = int(input())
numb = str(numb)
revers_numb = ''
if numb[0] == '-':
    revers_numb += '-'
    for i in numb[::-1]:
        if i == '-':
            pass
        else:
            revers_numb += i
else:
    for i in numb[::-1]:
        revers_numb += i
revers_numb = int(revers_numb)
print(revers_numb)
