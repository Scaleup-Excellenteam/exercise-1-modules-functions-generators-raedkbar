from typing import Dict, List


def get_recipe_price(prices: Dict[str, int], optionals: List[str] = None, **ingredients: int) -> int:
    """
    Calculates the total price of a recipe based on ingredient prices and weights.

    Params:
        prices: A dictionary containing ingredient prices in currency units per 100 grams.
        optionals: A list of optional ingredients. Defaults to an empty list if not provided.
        ingredients: Keyword arguments representing the ingredient weights in grams.

    Returns:
        The total price of the recipe as an integer value.
    """
    total_price = 0

    # If optionals is not provided, set it to an empty list
    if optionals is None:
        optionals = []

    # Iterate over each ingredient in the prices dictionary
    for ingredient, price in prices.items():
        weight = ingredients.get(ingredient)
        if ingredient not in optionals:
            total_price += price * weight / 100

    return int(total_price)


def main() -> None:
    """
    Entry point of the program. Calls the `get_recipe_price` function with different test cases.
    """
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    # Expected output: 44

    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    # Expected output: 54

    print(get_recipe_price({}))
    # Expected output: 0


if __name__ == '__main__':
    main()
