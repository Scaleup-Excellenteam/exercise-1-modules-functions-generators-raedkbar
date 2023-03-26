def get_recipe_price(prices, optionals=None, **ingredients):
    total_price = 0

    # If optionals is not provided, set it to an empty list
    if optionals is None:
        optionals = []

    # Iterate over each ingredient in the prices dictionary
    for ingredient, price in prices.items():
        weight = ingredients.get(ingredient)  # Get the weight of the current ingredient
        if ingredient not in optionals:
            total_price += price * weight / 100

    return int(total_price)


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))
