

melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}


melon_name = list(melon_names.values())
melon_price = list(melon_prices.values())
melon_seedlessness = list(melon_seedlessness.values())
melon_weight = [None] * 5
flesh_color = [None] * 5
rind_color = [None] * 5

# a list of dictionaries each contain the set of attributes of a melon
list_attr = [{'name' : name, 'price' : price, 'seedlessness' : seed, 'weight' : weight, 'rind_color' : rind_col, 'flesh_color' : flesh_col } for name, price, seed, weight, rind_col, flesh_col in zip(melon_name, melon_price, melon_seedlessness, melon_weight, rind_color, flesh_color)]

# a dictionary using name as the key and the items in the list_attr as the value
melon_dict = {name : value for name, value in zip(melon_name, list_attr) }
