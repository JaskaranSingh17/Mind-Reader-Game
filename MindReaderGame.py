import random

player_inputs_list = []

computer_score = 0
player_score = 0

def prediction():
    count_zero = player_inputs_list.count(0)
    count_one = player_inputs_list.count(1)
    if count_zero > count_one :
        predict = 0
    elif count_one > count_zero :
        predict = 1
    else:
        predict = random.randint(0, 1)
    return predict

def update_scores(player_input, predict):
    global player_score, computer_score
    if player_input == predict:
        computer_score = computer_score + 1
    else:
        player_score = player_score+1
    print("Your Score: ", player_score)
    print("Computer Score: ", computer_score)
    print()

def gameplay():
    valid_entries = ['0', '1']
    while True:
        predict = prediction()
        player_input = input("Please Enter Either 0 or 1: ")
        while player_input not in valid_entries:
            print("Invalid Entry !!")
            print()
            player_input = input("Enter Either 0 or 1: ")
        player_input = int(player_input)
        player_inputs_list.append(player_input)
        update_scores(player_input, predict)
        if player_score == 10:
            print("Hurray, You Win !!")
            break
        elif computer_score == 10:
            print("Better Luck Next Time!!")
            break

gameplay()