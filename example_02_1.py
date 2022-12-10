import random as rnd
n = 100
player = rnd.randint(1, 2)
player1 = "user"
player2 = "бот"
while n > 0:
    if player == 1:
        player = 2
    else:
        player = 1
    print("Осталось " + str(n) + " конфет")
    i = 0
    if player == 1:
        while i < 1 or i > 28:
            i = int(input("Игрок user сделайте ход: "))
            if i < 1 or i > 28:
                print("Можно ввести число в диапазоне от 1 до 28\nПопробуйте снова")
                i = 0
            elif n - i < 0:
                print("Введенное значение выходит за пределы")
                i = 0
            else:
                n = n - i
    if player == 2:
        if n > 28:
            k = 28
        else:
            k = n
        i = rnd.randint(1, k)
        print("Бот ввел значение: " + str(i))
        n = n - i
if player == 1:
    print("Попедитель: user")
else:
    print("Победитель: БОТ")