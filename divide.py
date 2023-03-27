def safe_print_division(a, b):
    try:
        quetion = a / b
    except (ZeroDivisionError, TypeError):
        quetion = None
    finally:
        print("Inside result: {}".format(quetion))
    print()
    return (quetion)


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
