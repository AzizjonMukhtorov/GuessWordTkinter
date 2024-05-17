from tkinter import *
import random as rdm

words1 = ['Donkey', 'Aeroplane', 'America', 'Program',
          'Python', 'language', 'Cricket', 'Football',
          'Hockey', 'Spaceship', 'bus', 'flight']

word1 = rdm.choice(words1).lower()

def found_word():
    global guesses1, turns1

    guess1 = entry_field.get().lower()
    entry_field.delete(0, END)
    
    if guess1 in word1 and guess1 not in guesses1:
        guesses1 += guess1
    elif guess1 not in word1:
        turns1 -= 1
        text.set(f"Wrong Guess. {turns1} lives left.")
        if turns1 == 0:
            text.set("User Loses. The word was " + word1)
            return
    
    failed1 = 0
    display_word = ''
    for char in word1:
        if char in guesses1:
            display_word += char + ' '
        else:
            display_word += '✖️ '
            failed1 += 1

    if failed1 == 0:
        text.set("User Wins! The correct word is: " + word1)
    else:
        text.set(display_word)

root = Tk()
root.title("Guess the word")
root.geometry("500x400")

label = Label(root, text="Guess the word")
label.pack()

entry_field = Entry(root, width=40, border=4)
entry_field.pack()

btn_check = Button(root, text="Check", command=found_word)
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy)
btn_quit.pack()

guesses1 = ''
turns1 = 10

text = StringVar()
text.set("You have 10 lives! Let's go!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()
