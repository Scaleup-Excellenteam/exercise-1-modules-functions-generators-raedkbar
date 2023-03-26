def join(*param, sep='-'):
    # use a list comprehension to flatten the lists
    joined_list = []

    # add the separator between the items
    for lst in param:
        joined_list += lst
        if lst is not param[-1]:
            joined_list += sep

    return joined_list


# get input from user
def get_lists():
    num_lists = int(input("Enter number of lists to be joined: "))
    lists = []

    for i in range(num_lists):
        lst = input(f"Enter list {i + 1}: ").split()
        lst = [int(item) for item in lst]
        lists.append(lst)
    return lists


res = get_lists()

answer = input("Do you want a custom separator? (y/n): ")
if answer == 'y':
    custom_sep = input("Enter a custom separator: ")
    result = join(*res, sep=custom_sep)
else:
    result = join(*res)

print(result)
