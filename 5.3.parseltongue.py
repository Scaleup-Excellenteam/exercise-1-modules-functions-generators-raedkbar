import re
from typing import Iterator, IO


MSG_PATTERN = '[a-z]{5,}'


def open_file(file_path: str, mode: str):
    """
    Opens a file and returns a file object.

    Params:
        file_path (str): The path to the file.
        mode (str): The mode in which to open the file ('r', 'w', etc.).

    Returns:
        file object: The opened file object.
    """
    return open(file_path, mode)


def extract_content(file: IO) -> Iterator[str]:
    """
    Extracts secret messages from a file.

    Params:
        file (file object): The file object to extract messages from.

    Yields:
        str: A secret message found in the file.
    """
    while True:
        # Read the file in chunks of 1024 bytes
        chunk = file.read(1024)
        if not chunk:
            break

        matches = re.findall(MSG_PATTERN, chunk)
        for match in matches:
            msg = match.decode('utf-8')  # Decode the match from bytes to string
            yield msg


def main() -> None:
    """
    The main entry point of the program.
    """
    path = input("Please enter a path: ")
    file = open_file(path, 'rb')
    generator = extract_content(file)

    for message in generator:
        print(message)

    file.close()


if __name__ == '__main__':
    main()
