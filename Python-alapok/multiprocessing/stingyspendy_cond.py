from threading import Thread, Condition


class Stingyspendy:
  money = 100
  # condition variable
  cv = Condition()

  def stingy(self):
    for _ in range(1000000):
      self.cv.acquire()
      self.money += 10
      # értesíti a másik szálat
      self.cv.notify()

      self.cv.release()
    print('Stingy done')

  def spendy(self):
    for _ in range(500000):
      self.cv.acquire()
      while self.money < 20:
        self.cv.wait()
      self.money -= 20
      if self.money < 0:
        print(f"Money in bank: {self.money}")
      self.cv.release()
    print('Spendy done')


ss = Stingyspendy()
t1 = Thread(target=ss.stingy, args=())
t2 = Thread(target=ss.spendy, args=())
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Money in the end: {ss.money}")