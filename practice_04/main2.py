# Задание 1. Область видимости

x = 12

def show():
    x = 2
    print(x)

show()
print(x)

#Сначала вызывается функция show(), внутри которой объявлена локальная переменная x = 2. Поэтому первой выводится цифра 2.
#После завершения функции выполняется print(x). Здесь используется внешняя переменная x = 12, поэтому выводится 12.

# Задание 2. Args

def total(*args):
    return sum(args)

print(total(2, 3, 4))


# Задание 3. Kwargs

def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Иван", age=18))


# Задание 4. Функция как параметр

def increase(x):
    return x + 2

def apply(func, value):
    return func(value)

print(apply(increase, 3))


# Задание 5. Рекурсия

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(3)