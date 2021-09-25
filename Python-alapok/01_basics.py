kapcsolo = True

if kapcsolo == True:
  print('a kapcsoló fel van kacsolva')

print('ez mindig lefut')

age = 5
name = 'Peter'
print(f'hello {name}')  # Python 3.6 felett
print('hello {} your age is {}'.format(name, age))

szam = 10
while szam > 0:
  print(f'a szambol levontunk egyet: {szam}')
  szam -= 1

mylist = [3, 4, 5, 5]

for num in mylist:
  print(num)

for i in range(5):
  print(i)

for index, item in enumerate(mylist):
  print(f'{index}: {item}')
