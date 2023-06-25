my_lst = [1, 2, 3, 2, 4, 3, 5, 5, 6]

def find_duplicates(lst):
    d = {}
    duplicates = []
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    for key, value in d.items():
        if value > 1:
            duplicates.append(key)
    return duplicates

print(find_duplicates(my_lst))