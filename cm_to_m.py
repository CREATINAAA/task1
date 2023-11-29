a = str(input())
b = str(input())

def summa(numb, chto):
    s = 0
    if chto == '+':
        for i in numb:
            s += int(i)
        return s
    elif chto == '*':
        s = 1
        for i in numb:
            s *= int(i)
        return s

print(summa(a, '+'))
print(summa(a, '*'))