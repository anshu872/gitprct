def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)
a=10
factorial(a)