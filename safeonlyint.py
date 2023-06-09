def safe_print_list_integers(my_list=[], x=0):
    num_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_print += 1
        except IndexError:
            break
        except (TypeError, ValueError):
            continue
    print()
    return num_print


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))