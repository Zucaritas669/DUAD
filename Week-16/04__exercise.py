def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

# O(n^3)
# why?
# "The exponent will increase depending on the number of nested loops."


def pull_request():
	print("Hello, i needed to make a change to do a PR")