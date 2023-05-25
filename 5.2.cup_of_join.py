from typing import List, Any


def join(*lists: List[Any], sep: str = '-') -> List[Any]:
    """
    Joins multiple lists together with an optional separator.

    Params:
        *lists: Variable number of lists to be joined.
        sep (str): Separator to be used between the items. Defaults to '-'.

    Returns:
        list: Joined list containing items from all input lists.
    """
    joined_list = []

    for lst in lists:
        joined_list += lst
        if lst is not lists[-1]:
            joined_list += sep

    return joined_list


def get_lists() -> List[List[int]]:
    """
    Retrieves a specified number of lists from the user.

    Returns:
        list: A list of lists, where each inner list contains integers.
    """
    num_lists = int(input("Enter number of lists to be joined: "))
    lists = []

    for i in range(num_lists):
        lst = input(f"Enter list {i + 1}: ").split()
        lst = [int(item) for item in lst]
        lists.append(lst)
    return lists


def main() -> None:
    """
    The main entry point of the program.

    Retrieves lists from the user, joins them together, and prints the result.
    """
    res = get_lists()

    answer = input("Do you want a custom separator? (y/n): ")
    if answer == 'y':
        custom_sep = input("Enter a custom separator: ")
        result = join(*res, sep=custom_sep)
    else:
        result = join(*res)

    print(result)


if __name__ == '__main__':
    main()
