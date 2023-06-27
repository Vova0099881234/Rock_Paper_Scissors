import random
import tkinter as tk

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_choice = choice_var.get()

    if player_choice not in choices:
        result_var.set("Invalid choice. Please try again.")
        return

    player_choice_index = choices.index(player_choice)
    computer_choice_index = random.randint(0, 2)
    computer_choice = choices[computer_choice_index]

    player_result = "You chose: " + player_choice
    computer_result = "Computer chose: " + computer_choice

    player_result_var.set(player_result)
    computer_result_var.set(computer_result)

    if player_choice_index == computer_choice_index:
        result_var.set("It's a tie!")
    elif (player_choice_index == 0 and computer_choice_index == 2) or \
            (player_choice_index == 1 and computer_choice_index == 0) or \
            (player_choice_index == 2 and computer_choice_index == 1):
        result_var.set("You win!")
    else:
        result_var.set("Computer wins!")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create choice variable and set default value
choice_var = tk.StringVar(window)
choice_var.set("rock")

# Create result variables
player_result_var = tk.StringVar(window)
computer_result_var = tk.StringVar(window)
result_var = tk.StringVar(window)

# Create labels for player and computer choices
player_result_label = tk.Label(window, textvariable=player_result_var)
player_result_label.pack(pady=10)

computer_result_label = tk.Label(window, textvariable=computer_result_var)
computer_result_label.pack(pady=10)

# Create option menu for player choice
choice_label = tk.Label(window, text="Choose:")
choice_label.pack()

choice_menu = tk.OptionMenu(window, choice_var, "rock", "paper", "scissors")
choice_menu.pack()

# Create button to play the game
play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack(pady=10)

# Create label for displaying the result
result_label = tk.Label(window, textvariable=result_var)
result_label.pack()

# Run the main window's event loop
window.mainloop()
