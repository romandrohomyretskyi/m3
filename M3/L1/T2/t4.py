'''
Давай намалюємо будинок! 
Яку площу він займе?

Користувач вводить чотири числа: 
a і b - сторони прямокутника, 
c і d - висота і основа трикутника.
Визначте функцію home_area, 
яка поверне площу будинку 
(тобто суму площ прямокутника і трикутника).

'''

def home_area(a, b, c, d):
    subtriangle_area_two=c*(d/2)
    triangle_area=(c*d)-subtriangle_area_two
    return (a*b)+triangle_area

a = int(input("Введіть першу сторону прямокутника: "))
b = int(input("Введіть другу сторону прямокутника: "))
c = int(input("Введіть першу сторону трикутника: "))
d = int(input("Введіть другу сторону трикутника: "))
print(home_area(a, b, c, d))
