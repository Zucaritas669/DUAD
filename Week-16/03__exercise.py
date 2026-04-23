def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
		
# O(1)

# Why?
# When it's a loop that always executes a predetermined number of times
# that does not vary with its input.

def pull_request():
	print("Hello, i needed to make a change to do a PR")