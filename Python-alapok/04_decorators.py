import time


def timing_function(callback):
  def wrapper():
    t1 = time.time()
    callback()
    t2 = time.time()
    print(f'A függvényt ennyi időbe telt lefuttatni: {t2-t1}')

  return wrapper


@timing_function
def my_function():
  num_list = []
  for num in range(0, 10000):
    num_list.append(num)
  print(f'sum all of numbers: {sum(num_list)}')


wrapped_function = timing_function(my_function)

wrapped_function()

my_function()
