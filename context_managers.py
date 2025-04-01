# The code uses a context manager to open a file and automatically close it after reading
with open("hello.txt", "r") as open_file:
    print(open_file.read())

class ContextManager:
  def __init__(self):
    print('Initializing class...')
 
  def __enter__(self):
    print('Entering context...')
 
  def __exit__(self, *exc):
    print('Exiting context...')

with ContextManager() as cm:
  print('Code inside with statement')
