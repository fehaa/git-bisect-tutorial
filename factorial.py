number = input("Factorial \nEnter a number:")

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)
print(factorial(int(number)))