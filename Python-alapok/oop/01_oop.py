class MyClass:
  pass


class Animal:
  # class attribute nem a példányhoz tartozik,, ha átállítjuk, az összes példány átállítja
  exists: True

  # constructior,a kkor fut le amikor példáényosítjuk az osztályt
  def __init__(self, age, max_age):
    self.age = age
    self.max_age = max_age
    print('Animal is created')

  def __str__(self):
    return f"This animal is {self.age} years old"

  def __repr__(self):
    return f"This animal is {self.age} years old"

  def eat(self):
    print('eating')

  def aging(self):
    self.age += 1
    print(self.age)
    if self.age >= self.max_age:
      self.alive = False


# my_animal = Animal(10, 50)
# my_animal2 = Animal(20, 100)

# print(my_animal.age)
# my_animal.eat()

# Animal.exists = False
# print(my_animal.exists)
# print(my_animal2.exists)

# # ha ki akarod íratni a classot akkor azt jeleníti meg ami az str-ben van definiálva
# print(my_animal)


class Dog(Animal):
  def __init__(self, age, max_age, fur_length):
    super().__init__(age, max_age)
    self.fur_length = fur_length

  def barking(self):
    print('vau vau!')


my_dog = Dog(10, 15, 'long')
print(f'{my_dog.age} éves vagyok')
my_dog.barking()
my_dog.aging()
