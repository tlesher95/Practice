import random
def list_to_set(x):
     return set(x)

def set_to_list(y):
    return list(y)

def combine_lists(L1, L2):
    return L1 + L2

a = random.sample(range(1,20), 5)
k = random.sample(range(1,20), 5)
combo = combine_lists(a, k)
b = list_to_set(combo)
c = set_to_list(b)
print("Randomly generated list:", combo)
print("Converted to set:", list_to_set(combo))
print("Converted back to list:", set_to_list(b))


# Just for practice comprehension
d = [digit**2 for digit in c if digit > 8]
print("List squared if greater than 8:", d)