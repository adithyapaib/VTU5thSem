#1 Reverse a string 

from multiprocessing import Condition


def rev(string):
    return string[::-1]

# Reverse a string using a list
def rev2(string):
    l = list(string)
    l.reverse()
    return ''.join(l)

print(rev2('hello')) # olleh
print(rev('hello')) # olleh



#2. Check if a string is a palindrome

def palindrome(string):
    return string == string[::-1]

print(palindrome('hello')) # False
print(palindrome('racecar')) # True 


#3 Check if a number is odd or even

def oddEven(num):
    if num % 2 == 0:
        return 'Even'
    return 'Odd'

print(oddEven(5)) # Odd
print(oddEven(6)) # Even


#4. Check if a number is prime

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(isPrime(5)) # True
print(isPrime(6)) # False


#5 Print fibonacci series using recursion

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5)) # 5
print(fib(6)) # 8




# 6. Print the first n fibonacci numbers using a list

def fib3(n):
    a, b = 0, 1
    l = []
    for i in range(n):
        a, b = b, a + b
        l.append(a)
    return l


print(fib3(5)) # [0, 1, 1, 2, 3]

# 7. factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# 7. factorial using loop

def  factorial2(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial2(5)) # 120




    



if Condition:
    "Statements if condition is true"
elif Condition2:
        """ Statements to be executed if the previous if condition is False """

        #.....
elif ConditionN:
        """ Statements to be executed if the previous if condition is False """
else:
        """ Statements to be executed if the condition is False """


if(a>b):
    print("a is greater than b")
elif(a<b):
    print("a is less than b")
else:
    print("a is equal to b")



while ConditionIsTrue:
    "Statements to be executed while the condition is true"
    #.....  #.....


for variable in sequence:
    "Statements to be executed for each item in the sequence"
    #.....  #.....

for i in range(10):
    print(i)

from  random import randint
A = randint(0,100)


def functionName(arg1, arg2, arg3):
        "function definition"