"""
**Генератори:**

1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
"""
def even_numbers(N):

    num = 0
    while num <= N:
        if num % 2 == 0:
            yield num
        num +=1




"""
2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""
def fibonacci(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b



"""

**Ітератори:**

1. Реалізуйте ітератор для зворотного виведення елементів списку.
"""

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self


    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.data[self.index]




"""
2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""


class EvenIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0


    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.N:
            num = self.current
            self.current +=1
            if num % 2 == 0:
                return num
        raise StopIteration


#Приклади
for n in even_numbers(10):
    print(n)

print("\n")

for n in fibonacci(50):
    print(n)

print("\n")

nums = [1,2,3,4,5]
rev_iter = ReverseIterator(nums)
for n in rev_iter:
    print(n)

print("\n")

evens =  EvenIterator(10)
for n in evens:
    print(n)