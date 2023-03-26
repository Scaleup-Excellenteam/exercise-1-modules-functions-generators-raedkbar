import os


def get_files(p):
    return [file_name for file_name in os.listdir(path) if file_name.lower().startswith("deep")]


path = input("Please enter a path:")
files = get_files(path)
print(files)
