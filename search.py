text = input()
word = input()
i = text.find(word)
count = ''
if i != -1:
    i = 0
    while True:
        i = text.find(word, i)
        if i == -1:
            print(count)
            break
        count += str(i) + ' '
        i += 1
else:
    print(i)
# def counting(text, word):
#     i = -1
#     count = ''
#     while True:
#         i = text.find(word, i + 1)
#         if i == -1:
#             return count
#         count += str(i) + ' '


# print(counting(text, word))
