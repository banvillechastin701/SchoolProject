def get_unique_elements(my_list):
    seen = set()
    return [x for x in my_list if x not in seen and not seen.add(x)]

print(get_unique_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
