import urllib.request
import json
import time


def count_letters(url, frequency):
  response = urllib.request.urlopen(url)
  txt = str(response.read())

  for l in txt:
    letter = l.lower()
    if letter in frequency:
      frequency[letter] += 1


def main():
  frequency = {}
  for c in "abcdefghijklmnopqrstuvwxyz":
    frequency[c] = 0
  start = time.time()
  for i in range(1000, 1020):
    count_letters(f'https://www.rfc-editor.org/rfc/rfc{i}.txt', frequency)
  end = time.time()
  print(json.dumps(frequency, indent=4))
  print(f"done, time taken: {end - start}")


# 22s
main()
