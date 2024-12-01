from random import randint

n_min = 1
n_max = 20
n = randint(n_min, n_max)
popitok = 10

print('Я загадал число от 1 до 100! Попробуй отгадать его за', popitok ,'попыток.')

for i in range(popitok):
    try:
        wopr = int(input('Какое число я загадал?(1 - 100):'))
        if wopr == n:
            print('Вы отгадали с', (i + 1),'попытки!')
            break
    except:
        print('Вы ввели не число.')

    print('У вас осталось', popitok - (i + 1), 'попыток.')

#python programa_rdm.py



















#a = randint(1, 10)
#b = 10

#def qestions():
#    wopr = input('Какое число?')
#    if a == wopr:
#        print('Правильно!')
#    else:
#        b = b - 1
#        print('')