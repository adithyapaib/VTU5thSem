def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

number = int(input("Enter a number: "))
while number != 1:
    print(number)
    number = collatz(number)

def slength(s):
    l = 0
    for i in s:
        l += 1
    return l

slength("Hello") # 5

>>> print(min('Adithya'))
A
