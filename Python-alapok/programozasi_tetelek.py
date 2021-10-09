t = [3, 4, 5, 6, 1]

# összeg
osszeg = 0
for num in t:
  osszeg = osszeg + num

print(f'összeg: {osszeg}')

# lineáris keresés (eldöntésre épül - van-e benne?)
n = len(t)
keresett_elem = 5

i = 0
while i < n and t[i] != keresett_elem:
  i = i + 1
if (i < n):
  print(f'van benne {keresett_elem}-ös')
  print(f'a(z) {keresett_elem} a(z) {i+1}. helyen található')
else:
  print('nincs ilyen elem')

# max kiválasztás
max_index = 0
for i, elem in enumerate(t):
  if elem > t[max_index]:
    max_index = i

print(f'a maximum: {t[max_index]}')

# buborékrendezés
n = len(t)
for i in range(n - 1):
  for j in range(0, n - i - 1):
    if t[j] > t[j + 1]:
      t[j], t[j + 1] = t[j + 1], t[j]
print(t)

# faktorilális, rekurzív
r = 10


def fakt(n):
  if n == 0:
    return 1
  else:
    return (n * fakt(n - 1))


print(fakt(r))
