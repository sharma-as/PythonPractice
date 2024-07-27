def linear_search(lst, target):
    """Returns the index position of the target if found, else returns -1"""

    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return -1

a = linear_search([1,5,6,7,3],6)
print(a)

def linear_search2(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

b = linear_search2([1,5,6,7,3],5)
print(b)
