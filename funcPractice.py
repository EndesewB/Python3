def add_numbers(n1, n2):
	result = n1+n2
	return result


def multiply_numbers(n1, n2):
	result = n1 * n2
	return result


num1 = float(input("enter first num:"))
num2 = float(input("enter second num:"))
summ = add_numbers(num1, num2)
product = multiply_numbers(num1, num2)

print("the sum of the two numbers is:", summ, " and its product is:", product)
