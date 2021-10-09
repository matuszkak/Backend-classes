import pickle
from os import path

current_path = path.dirname(__file__)

with open(path.join(current_path, 'persons.pickle'), 'rb') as file:
  persons = pickle.load(file)

print(persons)