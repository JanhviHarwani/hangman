import tkinter as tk
from tkinter import messagebox
import random

class Hangman:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.word_list = ["python", "hangman", "challenge", "interface", "developer"]
        self.max_attempts = 6
        self.initialize_game()

    def initialize_game(self):
        self.word_to_guess = random.choice(self.word_list).upper()
        self.correct_guesses = set()
        self.wrong_guesses = set()
        self.attempts_left = self.max_attempts

        self.word_label = tk.Label(self.root, text=self.get_display_word(), font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 18))
        self.attempts_label.pack(pady=10)

        self.letter_frame = tk.Frame(self.root)
        self.letter_frame.pack()

        self.buttons = []
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            button = tk.Button(self.letter_frame, text=letter, font=("Arial", 18), width=4,
                               command=lambda letter=letter: self.guess_letter(letter))
            button.grid(row=i // 6, column=i % 6, padx=5, pady=5)
            self.buttons.append(button)

    def get_display_word(self):
        return " ".join([letter if letter in self.correct_guesses else "_" for letter in self.word_to_guess])

    def guess_letter(self, letter):
        if letter in self.correct_guesses | self.wrong_guesses:
            return

        if letter in self.word_to_guess:
            self.correct_guesses.add(letter)
            self.word_label.config(text=self.get_display_word())

            if all(letter in self.correct_guesses for letter in self.word_to_guess):
                self.end_game(win=True)
        else:
            self.wrong_guesses.add(letter)
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

            if self.attempts_left == 0:
                self.end_game(win=False)

        self.update_buttons()

    def update_buttons(self):
        for button in self.buttons:
            if button["text"] in self.correct_guesses | self.wrong_guesses:
                button.config(state="disabled", disabledforeground="black")

    def end_game(self, win):
        if win:
            messagebox.showinfo("Hangman", f"Congratulations! You've guessed the word: {self.word_to_guess}")
        else:
            messagebox.showinfo("Hangman", f"Game Over! The word was: {self.word_to_guess}")
        
        self.reset_game()

    def reset_game(self):
        self.word_label.destroy()
        self.attempts_label.destroy()
        self.letter_frame.destroy()
        self.initialize_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()
