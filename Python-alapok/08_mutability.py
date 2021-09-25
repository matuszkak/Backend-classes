a = []
b = a
print(id(a))
print(id(b))

a.append(34)
print(b)

# a-hoz fűzök hozzá de b is módosul

# ha tényéges másolat kell a listáról akkor a .copy metódust kell használni
b = a.copy()
print(id(a))
print(id(b))

a = 1995
b = 1995
print(id(a))
print(id(b))

# immutable: bool, int, foloat, tuple, string, frozenset
# mutable: list, set, dict
