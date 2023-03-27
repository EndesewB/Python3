try:
    result = 10 * (2/0)
    print("the result is ", result)
except ZeroDivisionError:
    print("division by zero is not possible")


try:
    x = int(input("enter integer number "))
except ValueError:
    print("you inserted non integer, please enter integer")





