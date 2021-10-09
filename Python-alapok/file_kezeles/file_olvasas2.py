from os import path

# lekerdezzuk az aktualis mappat
current_path = path.dirname(__file__)
print(current_path)
file_name = 'temp.txt'

my_list = []
f = open(path.join(current_path, file_name), 'r')

for line in f:
  my_list.append(int(line))

f.close()

print(my_list)