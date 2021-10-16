
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = 0

while a == 0:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def encrypt(text, shift):
    word = []
    indexWord = 0

    for l in text:
      word.append(l)

    for i in word:
      for l in range(0, len(alphabet)):
        if i == alphabet[l]:
          indexWord=word.index(i)
          word[indexWord] = alphabet[l+shift]

    display = ''

    for x in word:
      display += x

    print(display)

  def decrypt(text, shift):
    word = []
    indexWord = 0

    for l in text:
      word.append(l)

    for i in word:
      for l in range(0, len(alphabet)):
        if i == alphabet[l]:
          indexWord=word.index(i)
          word[indexWord] = alphabet[l-shift]

    display = ''

    for x in word:
      display += x

    print(display)

  if direction == "encode":
    encrypt(text, shift)
    end_game = input("Repeat or End?\n").lower
    if end_game == "end":
      a = 1
  elif direction == "decode":
    decrypt(text, shift)
    end_game = input("Repeat or End?\n").lower
    if end_game != "repeat":
      a = 1
  else:
    print("Not valid.")