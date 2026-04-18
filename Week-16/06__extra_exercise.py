def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

# O(n)

# Why?
# When it's a loop that always executes a predetermined number of times
# that does not vary with its input.


def binary_search(my_list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

#O(log n)
#Why?

# When it's a loop that decreases its number of iterations
# the larger the input is.


# ¿En qué condiciones conviene usar cada uno?
#linear_search — use it when the list is unsorted

#binary_search — use it when the list is sorted



# ¿Qué pasa si la lista no está ordenada?
#Binary search assumes the list is sorted. If it's not, it will skip elements incorrectly and could miss the target even if it's there.


def pull_request():
	print("Hello, i needed to make a change to do a PR")