from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        yield file
    finally:
        file.close()

with open_file("hello.txt", "r") as file:
    print(file.read())

print(file.closed)