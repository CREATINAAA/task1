s = input()
s2 = input()
slovo = ''
while True:
    if len(slovo) < len(s2):
        for i in s:
            slovo += i
    elif slovo != s2:
        slovo = ''
        continue
    else:
        print(slovo)
        break
