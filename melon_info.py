"""Print out all the melons in our inventory."""


from melons import melon_dict

def print_melon(melon_dictionary):
    """Print each melon with corresponding attribute information."""

    for key, value in melon_dictionary.items():
        print(key.upper())
        for key, value in value.items():
            print(f"\t{key} : {value}")
        print('-' * 30)
            

print_melon(melon_dict)
