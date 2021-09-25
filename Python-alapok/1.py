sentence = input('Írj be egy mondatot: ')

digits = 0
letters = 0

for char in sentence:
  if char.isdigit():
    digits += 1
    if char.isalpha():
      letters += 1

print(f"betűk: {letters} számok: {digits}")