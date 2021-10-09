from threading import Thread, Lock


class Stingyspendy:
  money = 100
  mutex = Lock()

  def stingy(self):
    for _ in range(1000000):
      self.mutex.acquire()
      self.money += 10
      self.mutex.release()
    print('Stingy done')

  def spendy(self):
    for _ in range(1000000):
      self.mutex.acquire()
      self.money -= 10
      self.mutex.release()
    print('Spendy done')


ss = Stingyspendy()
t1 = Thread(target=ss.stingy, args=())
t2 = Thread(target=ss.spendy, args=())
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Money in the end: {ss.money}")