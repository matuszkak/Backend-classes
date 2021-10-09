import time
from threading import Thread


def do_work():
  print('starting work')
  time.sleep(3)
  print('finished work')


for i in range(5):
  t = Thread(target=do_work, args=())
  t.start()
#   do_work()

# párhuzamosan fut le, shared memory - mindegyik szál ua memoria területtel dolgozik, no isolation, változók sem különülnek el, elérhető minden szálnak (vs. process, ahol van izoláció)
