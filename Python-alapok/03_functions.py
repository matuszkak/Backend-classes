def my_func():
  pass


def add_user(users, new_user):
  users.append(new_user)


# local vs. global parameters

users = []
print(users)
add_user(users, 'John')
print(users)
new_users = users
print(users)
new_users.append('Kate')
print(users)
print(new_users)
new_users.append('Cab')
print(users)
print(new_users)
users.append('Mark')
print(users)
print(new_users)

vehicle = 'bus'


def drive():
  global vehicle
  vehicle = vehicle.capitalize()
  print(f'driving a {vehicle}')


drive()


# callback
def times2(num):
  return num * 2


seq = [3, 4, 5, 5]
times2_seq = list(map(times2, seq))
print(times2_seq)

# anonim function
times2_seq = list(map(lambda x: x * 2, seq))
print(times2_seq)

# a seq változóban megkeressük a 2-vel osztható számokat
filtered_list = list(filter(lambda num: num % 2 == 0, seq))
print(filtered_list)

# pont annyi paramétert kell megadni amennyit a func vár (JB-ben nem így van)
print(times2(7))

# keyword argument - func definícióban létrehopzott változókra hivatkozunk, a nevükkel együtt
# ilyenkor nem számít, milyen sorrendben adjuk meg


def set_namme(namme, new_namme):
  namme = new_namme
  return namme


set_namme(new_namme='Kate', namme='Peter')


def multiply(*args):
  print(args)
  total = 1
  for arg in args:
    total = total * arg
  return total


val = multiply(2, 3, 4, 5, 6)
print(val)
