import time
from multiprocessing import Process, set_start_method


def do_work():
  print('starting work')
  time.sleep(3)
  print('finished work')


if __name__ == '__main__':

  set_start_method('spawn')
  for i in range(5):
    # separate memory, resource heavy, isolation
    # spawn: nem másolja le a memóriát, a gyermek process része

    t = Process(target=do_work, args=())
    t.start()
