import random
moves=['R','P','S']
game = input("Want to start game Y or N: ").upper()
if game == 'N':
    print ("BYE :(")
while game =='Y':
    computer_move = random.choice(moves)
    player_move=input('R for rock P for paper S for scissors or E to end game:').upper()
    if player_move == computer_move:
        print(f"Same move {computer_move}")
    elif computer_move == 'R' and player_move == 'P' or computer_move == 'P' and player_move == 'S' or computer_move == 'S'and player_move == 'R':
        print(f"You win computer move :{computer_move} Your move:{player_move}")
    elif computer_move == 'P' and player_move == 'R' or computer_move == 'S'and player_move =='P' or computer_move == 'R' and player_move =='S':
        print(f"You Lose :( Computer move:{computer_move} Your move:{player_move}")
    elif player_move == 'E':
        break
    elif player_move != 'E' or 'P' or "S" or 'R':
        print('Invalid Move >:(')
