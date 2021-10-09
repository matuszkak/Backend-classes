import pickle
from os import path

persons = [{
    "name": "Fred",
    "age": 32,
    "married": True
}, {
    "name": "John",
    "age": 12,
    "married": False
}]

current_path = path.dirname(__file__)

with open(path.join(current_path, 'persons.pickle'), 'wb') as file:
  pickle.dump(persons, file)
