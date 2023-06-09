def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            # print(f"{my_list[i]}", end="")
            print("{:d}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
        except ValueError:
            continue
    print()
    return total


my_list = [1, 2, 3, "school", 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
