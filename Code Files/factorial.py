def factorial(a):
	fact = 1
	for i in range(1, a+1):
		fact = fact*i
	return(fact)


n = int(input("Please enter the number: \n"))
print(f"Factorial of {n} is {factorial(n)}")


print("===========================")
print("Finding factorial using recursion")


def rec_fact(b):
	if b == 1:
		return b
	else:
		return b*rec_fact(b-1)


c = int(input(f"Please enter the number: \n"))
print(f"Factorial of {c} using recurssion is {rec_fact(c)}")