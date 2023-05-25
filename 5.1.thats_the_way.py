import os
from typing import List


def get_files(path: str) -> List[str]:
    """
    Get a list of files in the specified directory that start with "deep".

    Params:
        path (str): The path of the directory.

    Returns:
        list: A list of file names that start with "deep".
    """
    # Use list comprehension to filter file names that start with "deep"
    return [file_name for file_name in os.listdir(path) if file_name.lower().startswith("deep")]


def main() -> None:
    """
    Main function to get a path from the user and display files starting with "deep".
    """
    path = input("Please enter a path:")
    print(get_files(path))


if __name__ == '__main__':
    main()
