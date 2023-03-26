import re


def open_file(file_path, mode):
    f = open(file_path, mode)
    return f


def extract_content(f):
    # Read the file in chunks of 1024 bytes
    while True:
        chunk = f.read(1024)
        if not chunk:
            # End of file reached
            break
        # Search for secret messages in the chunk
        matches = re.findall(b'[a-z]{5,}!', chunk)
        for match in matches:
            # Decode the match from bytes to string
            msg = match.decode('utf-8')
            # Yield the secret message
            yield msg


path = input("Please enter a path: ")
file = open_file(path, 'rb')
generator = extract_content(file)

for message in generator:
    print(message)

file.close()
