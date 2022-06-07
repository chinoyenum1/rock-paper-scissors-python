import random


Options = [{"R": "ROCK"}, {"P": "PAPER"}, {"S": "SCISSORS"}]


def get_player_selection():
    while True:
        try:
            player_input = input("Enter a choice (rock[R], paper[P], scissors[S]): ")

            for option in Options:
                for key in option.keys():
                    if player_input.upper() == key:
                        selection = option[key]
                        # print(selection)
                        return selection
            raise KeyError("Invalid Selection")
        except KeyError as e:
            print(e)
            continue


def get_computer_selection():
    selection = random.randint(0, len(Options) - 1)
    for key in Options[selection].keys():
        option = Options[selection][key]
        return option


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "ROCK":
        if computer_action == "SCISSORS":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "PAPER":
        if computer_action == "ROCK":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "SCISSORS":
        if computer_action == "PAPER":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


while True:
    player_selection = get_player_selection()
    computer_selection = get_computer_selection()
    print(f"Player({player_selection}): Computer({computer_selection})")
    determine_winner(player_selection, computer_selection)
    if player_selection == computer_selection:
        continue
    else:
        break
