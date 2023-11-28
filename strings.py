stroka = str(input())
integer = ''
numbers = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '-': '-'
}
for key in stroka:
    if key in numbers:
        integer += numbers[key]
    elif key == ' ':
        integer = 0
        break

print(int(integer))
