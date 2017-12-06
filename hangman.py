import random

def print_wrong(g):
  print("Not in solution:")
  for c in g:
    print("{} ".format(c), end='')
    
  print("\n" * 3)
    
    
def print_found(word, letters):
  print("Word to guess:")
  
  for c in word:
    if c in letters:
      print(c, end='')
    else:
      print('_', end='')
  

def game(word):
  wrong_guesses = []
  found_letters = []
  tries = 0
  
  while tries < 6:
    print()
    
    # Read user guess
    guess = input("Enter a single letter: ");
    
    # Must be only one character
    if (len(guess) != 1) or (guess == ' '):
      print("Invalid input. Enter only one letter!")
      continue
    
    # Check if letter was already tried
    if (guess in wrong_guesses) or (guess in found_letters):
      print("You already tried that letter!")
      continue
    
    # Check if character is in word
    if guess in word:
      # Add to solution
      found_letters.append(guess)
    else:  
      # Add to wrong guesses
      wrong_guesses.append(guess)
      tries += 1
    
    # Print eveything back
    print_wrong(wrong_guesses);
    print_found(word, found_letters);
    
    # Check if all letters were found
    for c in word:
      if c not in found_letters:
        break
    else:
      print("\n\nCongratulation, you found the word with only {} wrong guesses =)".format(tries))
      return True
    
  # Game over
  print("\nSorry! You didn't find the word.")
  print("The solution was: " + word)
  return False


def main():
  games_total = 0
  games_won = 0;
  
  # Create a list of words
  words = [
    "bird",
    "escutcheon",
    "boat",
    "misery",
    "yellow",
    "appartment",
    "development",
    "idiot",
    "nincompoop"
  ]
  
  # Print welcome message
  print('''
  Hello and welcome to Martin's Hangman!
  
  You have 6 tries to guess the hidden word. Good luck!
  ''')
  
  play_again = 'y'  
  
  while play_again != 'n':
    # Pick a random word from the list
    word = random.choice(words)
    
    print()
    print('_' * len(word))
    
    # Start the game
    if game(word):
      games_won += 1
      
    games_total += 1
    
    # Ask player to play again
    play_again = input("\n\nWould you like to play another game? [y/N] ")[0].lower()  
  
  # Print total games stats
  print("You found {} word(s) out of {} game(s) for a {}% success rate!".format(games_won, games_total, int(round(games_won * 100 / games_total))))
  
  
main()
