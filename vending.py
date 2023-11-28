count_bottle = {
    'kvas': 2,
    'coca-cola': 4,
    'dushes': 10
}

menu_drinks = {
    'kvas': (2 * (10 ** 6) + 50),
    'coca-cola': (5 * (10 ** 6) + 20),
    'dushes': (3 * (10 ** 6) + 10)
}

banknots_vending = 10
cents_vending = 100
z = ((10 ** 6) * banknots_vending) + cents_vending
value = int(input()) * (10 ** 6)
bottles = int(input())
value2 = 0
x = True
while x:
    print('Что желаете?')
    key = str(input())
    if len(key) > 0:
        while count_bottle[key] == 0:
            print('Напиток закончился, выберите другой')
            key = str(input())
            if len(key) == 0:
                break
        while key not in count_bottle:
            print('Такого напитка нет, выберите другой')
            key = str(input())
            if len(key) == 0:
                break
        if key in count_bottle:
            while bottles > count_bottle[key]:
                print('У нас столько нет, выберите меньше')
                bottles = int(input())
                if bottles == 0:
                    break
            else:
                print(f'У нас есть такой напиток, он стоит {menu_drinks[key] * bottles}')
                while value < (menu_drinks[key] * bottles):
                    print('Внесите еще денег')
                    value2 = int(input()) * (10 ** 6)
                    value += value2
                else:
                    print('Ваш напиток в пути')
                    count_bottle[key] -= bottles
                    banknots_vending += value / (10 ** 6)
                    if value > (menu_drinks[key] * bottles):
                        print('Мы должны Вам сдачу, подождите')
                        print(f'Ваша сдача {value - (menu_drinks[key] * bottles)}')
                        
        else:
            None
    else:
        print('Всего доброго!')
        x = False
