import random
import hangman_constants

selected_word = list(random.choice(hangman_constants.word_list))
guessed_word = ['_' for c in selected_word]
current_iteration = len(hangman_constants.hangman_stages)-2
correct_guess_iteration = 0
end_game = False

def fill_blanks(guessed_word):
    print(*guessed_word)

def draw_hangmen():
    global current_iteration
    global end_game

    print(hangman_constants.hangman_stages[current_iteration])
    current_iteration -= 1
    if current_iteration < 0:
        print("Man died!")
        end_game = True

print(hangman_constants.logo)

while not end_game:
    fill_blanks(guessed_word)
    guessed_letter = input("Guess a letter: ").lower()
    try:
        index = selected_word.index(guessed_letter)
        guessed_word[index] = guessed_letter
        selected_word[index] = '_'
        correct_guess_iteration += 1
        if len(selected_word) == correct_guess_iteration:
            print("You won!")
            end_game = True
    except ValueError:
        draw_hangmen()

print("Game over...")
