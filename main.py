#Step 1 
from replit import clear
import random
import hangman_art
import hangman_words

print(f"{hangman_art.logo}\n")
#word_list = ["aardvark", "baboon", "camel", "cat", "house"]
#Randomly choose a word from the word_list
rnd_word = random.choice(hangman_words.word_list)
# Test print
#print(f"Pssst, the solution is {rnd_word}")

word_len = len(rnd_word)
space_word = []

lives = 6

for _ in range(0, word_len):
  space_word += '_'

print(f"Word with {word_len} letters: \n{hangman_words.list2string(space_word, ' ')}\n" )

while True:
  #Ask the user to guess a letter
  guess_letter = input("Guess a letter: ").lower()
  clear()

  cnt = 0
  cnt_word = 0
  for letter in rnd_word:
    if letter == guess_letter:
      space_word[cnt] = letter
      cnt_word += 1
    cnt += 1

  print(f"{hangman_words.list2string(space_word, ' ')}\n")
  #Check if the letter the user guessed is one of the letters in the random word
  if guess_letter in hangman_words.list2string(space_word, ' '):
    print(f"The letter {guess_letter} already guessed")
  # Check the number of lettters in the random work and track the player lifes
  if cnt_word > 0:
    print(hangman_art.stages[lives])
  else:
    print(f"You guesse '{guess_letter}', that's not in the word. You lose a life")
    lives -= 1
    print(hangman_art.stages[lives])

  good = ''.join(space_word)
  if good == rnd_word and lives > 0:
    print("\nYou win ヾ(-_- )ゞ")
    break
  elif lives == 0:
    print("\nYou lose (╥_╥)")
    break