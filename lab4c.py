#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    new_dect = {}
    i = 0
    for key in keys:
        new_dect[key] = values[i]
        i += 1
    return new_dect
print(create_dictionary(list_keys, list_values))

def shared_values(dict1, dict2):
    set1 = set(dict1.values())  # Convert dictionary values into a set
    set2 = set(dict2.values())  # Convert dictionary values into a set
    
    return set1.intersection(set2)  # Find common values

if __name__ == "__main__":
    york = create_dictionary(list_keys, list_values)
    print('York:', york)  

    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)  
