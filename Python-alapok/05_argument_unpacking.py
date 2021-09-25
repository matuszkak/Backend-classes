
# positional arguments
def named1(*args):
  print(args)


named1(3, 4, 5, 5)


# keyword arguments
def named2(**kwargs):
  print(kwargs)


named2(name="Bob", age=4, alive=True)

details = {'name": Bob', "age": 4, "alive": True}

named2(**details)


