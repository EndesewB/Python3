def safe_print_integer(value):
    try:
        print("{:d} is an integer".format(value))
        return True
    except ValueError:
        return False


value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = '45'
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
