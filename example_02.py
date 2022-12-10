import random as rnd
n = 2021
player = rnd.randint(1, 2)

while n > 0:
    if player == 1:
        player = 2
    else:
        player = 1
    print("Осталось " + str(n) + " конфет")
    i = 0    
    while i < 1 or i > 28:
        i = int(input("Игрок " + str(player) + " сделайте ход: "))
        if i < 1 or i > 28:
            print("Можно ввести число в диапазоне от 1 до 28\nПопробуйте снова")
            i = 0
        elif n - i < 0:
            print("Введенное значение выходит за пределы")
            i = 0
        else:
            n = n - i
    

print("Попедитель игрок " + str(player))