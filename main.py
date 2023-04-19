from random import randint

current_game = 0
wins = 0
plyr_bet = 0
comp_bet = 0
# 0 = rock
# 1 = paper
# 2 = scissors

def print_score():
    print()
    print('you: ' + str(wins) + '\nme: ' + str(current_game - wins))

def calculate_winner(player_1, player_2):
    '''DOCSTRING - calculate_winner(player_1, player_2)
this function determines whether or not player 1 won a game of rock-paper-scissors. returns bool.'''
    if player_1 == player_2:
        return None

    if player_1 == 0:
        return player_2 == 2
    elif player_1 == 1:
        return player_2 == 3
    elif player_1 == 2:
        return player_2 == 1
    else:
        return False

print()
print('you, me, best out of three. go.')
print()

while True:
    print('==========================================|')
    print('rock, paper, scissors, shoot!')
    cmd = input('>> ')

    if cmd == 'rock':
        plyr_bet = 0
    elif cmd == 'paper':
        plyr_bet = 1
    elif cmd == 'scissors':
        plyr_bet = 2
    else:
        print('what?? that\'s not how you play this!')
        continue

    comp_bet = randint(0,2)

    if comp_bet == 0:
        print('<< rock!')
    elif comp_bet == 1:
        print('<< paper!')
    elif comp_bet == 2:
        print('<< scissors!')
    else:
        print('umm, let\'s try this again.')
    print()

    result = calculate_winner(plyr_bet, comp_bet)
    if result == None:
        print('augh! tie! let\'s try again.')

    elif result == True:
        current_game = current_game + 1
        wins = wins + 1
        if current_game < 3:
            print('augh! you got this one!')
        else:
            break

    elif result == False:
        current_game = current_game + 1
        if current_game < 3:
            print('whew, got this one.')
        else:
            break

    if result != None:
        print_score()


print_score()
print()
if wins > 1:
    print('congrats, you win!')
else:
    print('i win!')

print('thanks for playing!')
