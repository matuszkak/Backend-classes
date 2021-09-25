def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError('Nullával nem lehet osztani')
  return dividend / divisor


# divide(3, 0)

grades = []
# grades = [2, 4, 5]

try:
  avg = divide(sum(grades), len(grades))
  print(avg)
except ZeroDivisionError as e:
  print(e)
  print('there are no grades yet')
finally:
  print('thank you')

students = [{
    "name": "Bob",
    "grades": [2, 3, 4]
}, {
    "name": "Steve",
    "grades": []
}, {
    "name": "John",
    "grades": [3, 4]
}]

try:
  for student in students:
    grades = student['grades']
    name = student['name']
    avg = divide(sum(grades), len(grades))
except ZeroDivisionError:
  print(f'Error: {name} has no grades')
