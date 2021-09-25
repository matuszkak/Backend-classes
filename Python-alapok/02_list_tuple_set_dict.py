# lista típusok

my_list = [2, 3, 56, 6]

print(my_list[0])
# -1. elem a lista utolasó eleme
print(my_list[-1])

# tól-ig határ, első inclusive, második exclusive
print(my_list[1:3])

print(my_list[2:])
print(my_list[:3])

# második lista első elemét szedi ki
my_nested_list = [[3, 4], [5, 6], [7, 8]]
print(my_nested_list[1][0])

my_list.append(5)
print(my_list)

# megnézi h a listában van-e egy adott érték
print(6 in my_list)

# tuple típusok
# immutable - does not support item assignment - nem lehet elem egyik értékét módosítani

my_tuple = (3, 'Peter', 8)

# set, nem tartalmazhat azonos elemeket a halmaz - egyedieket
my_set = {2, 3, 4, 5, 3, 3}
print(type(my_set))
print(my_set)

my_ownlist = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
unique = list(set(my_ownlist))
print(unique)

# dictionary

my_dict = {"name": "Peter", "age": 4, "alive": True}
print(my_dict['name'])
print(my_dict.keys())
print(my_dict.values())

for index, key in enumerate(my_dict):
  print(key, my_dict[key])

if 'alive' in my_dict:
  print('benne van')
