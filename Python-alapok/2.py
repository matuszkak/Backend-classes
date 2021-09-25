def is_narcistic(value):
  value = str(value)
  numbers = []
  for c in value:
    numbers.append(int(c))
  print(numbers)
  power = len(numbers)
  summ = 0
  for number in numbers:
    summ = summ + number**power
  if summ == int(value):
    return True
  return False


print(is_narcistic(153))
print(is_narcistic(128))
