from os import path

# lekerdezzuk az aktualis mappat
current_path = path.dirname(__file__)
print(current_path)
file_name = 'your_file.txt'

my_list = []
with open(path.join(current_path, file_name), 'r') as f:
  for line in f:
    #leszedjük a sorvége jeleket - whitespace-t szedi le elöl és hátul is
    line = line.strip()
    my_list.append(line)
print(my_list)
