def manual_add(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result

# O(n)

# Why?
# When it's a loop that always executes a predetermined number of times
# that does not vary with its input.



def add_formula(number):
    return number * (number + 1) // 2

# O(1)

# Why?
# When it's a loop that always executes a predetermined number of times
# that does not vary with its input.


#¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
# Version 2. With one billion iterations, Version 1 would take several seconds to complete. Version 2 calculates the answer instantly with a single formula.

def pull_request():
	print("Hello, i needed to make a change to do a PR")