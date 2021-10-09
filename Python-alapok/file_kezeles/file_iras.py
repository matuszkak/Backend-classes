from os import path

# lekerdezzuk az aktualis mappat
current_path = path.dirname(__file__)
print(current_path)
file_name = 'your_file.txt'

my_list = ['elso sor', 'masodik sor', 'harmadik sor']
with open(path.join(current_path, file_name), 'w') as f:
  for item in my_list:
    f.write(f'{item}\n')
