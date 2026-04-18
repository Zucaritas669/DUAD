def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

# O(n^2)
# why?
# "The exponent will increase depending on the number of nested loops."

def pull_request():
	print("Hello, i needed to make a change to do a PR")