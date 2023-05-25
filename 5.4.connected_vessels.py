from typing import Any, List


def interleave(*lists: Any) -> List[Any]:
    """
    Interleaves the elements from multiple sequences.

    Params:
        *lists: Variable number of sequences.

    Returns:
        A list containing the interleaved elements from the input sequences.
    """
    max_len = max(len(param) for param in lists)
    res = []
    for elem in range(max_len):
        for lst in lists:
            if elem < len(lst):
                res.append(lst[elem])
    return res


def main() -> None:
    """
    Main entry point of the program.
    """
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))


if __name__ == '__main__':
    main()
