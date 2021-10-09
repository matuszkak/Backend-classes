import urllib.request
import json
import time
from threading import Thread, Lock


def count_letters(url, frequency, mutex: Lock):
  response = urllib.request.urlopen(url)
  txt = str(response.read())
  mutex.acquire()
  for l in txt:
    letter = l.lower()
    if letter in frequency:
      frequency[letter] += 1
  mutex.release()


def main():
  frequency = {}
  mutex = Lock()
  for c in "abcdefghijklmnopqrstuvwxyz":
    frequency[c] = 0
  start = time.time()
  threads = []
  for i in range(1000, 1020):
    t = Thread(target=count_letters,
               args=(f'https://www.rfc-editor.org/rfc/rfc{i}.txt', frequency,
                     mutex))
    t.start()
    threads.append(t)
  for t in threads:
    # azt jelzi a fő prgm-nak h várjon amíg a szál végez
    t.join()
  end = time.time()
  print(json.dumps(frequency, indent=4))
  print(f"done, time taken: {end - start}")


# 2,33 s
main()
