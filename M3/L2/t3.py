'''
Потрібно порахувати добуток чисел від a до b. 
Програма запитує числа і виводить результат.
Програма запитує у людини спочатку перше число, потім друге. 
Після цього програма повинна перемножити всі числа від a до b 
(припускаючи, що a < b) і надрукувати результат. 
Приклад: Введено числа 5 і 7. 
Програма надрукує "210" (5 * 6 * 7 = 210).
'''

a=int(input("number1:"))
b=int(input("number2:"))

step=1 if a<=b else -1

result=1
for number in range(a,b+step,step):
    result*=number

print(result)

