from my_module import say_hi, multiply
from lib.mylib import say_hello

say_hi()
print(multiply(3, 4))
#itt a name változó már nem main!

say_hello()

import sys

#innen importálhasz be modulokat
print(sys.path)
