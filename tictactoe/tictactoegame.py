
##### Select a player
def select_players():
    select_player = input("Which player do you want? 1 or 2 ")
    if select_player == '1':
        select_player = 'O'
    else: 
        select_player = 'X'
    return select_player

##### Match Three things like XXX or OOO
# 012
# 345
# 678
# 036
# 147
# 258
# 048
# 246

# TEST_LIST1 = ['O','2','3','4','O','6','7','8','O']
def check_end(TEST_LIST):
    case1 = TEST_LIST[0] == TEST_LIST[1] == TEST_LIST[2]
    case2 = TEST_LIST[3] == TEST_LIST[4] == TEST_LIST[5]
    case3 = TEST_LIST[6] == TEST_LIST[7] == TEST_LIST[8]
    case4 = TEST_LIST[0] == TEST_LIST[3] == TEST_LIST[6]
    case5 = TEST_LIST[1] == TEST_LIST[4] == TEST_LIST[7]
    case6 = TEST_LIST[2] == TEST_LIST[5] == TEST_LIST[8]
    case7 = TEST_LIST[0] == TEST_LIST[4] == TEST_LIST[8]
    case8 = TEST_LIST[2] == TEST_LIST[4] == TEST_LIST[6]
    if case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8:
        return True
    else:
        return False
# print(check_end(TEST_LIST1))

##### Make a coordinate system
ANSWER_LIST = ['1','2','3','4','5','6','7','8','9']
QUIZ = f'''
            |         |
        {ANSWER_LIST[0]}   |    {ANSWER_LIST[1]}    |    {ANSWER_LIST[2]}
    ________|_________|_________
            |         |
        {ANSWER_LIST[3]}   |    {ANSWER_LIST[4]}    |    {ANSWER_LIST[5]}
    ________|_________|_________
            |         |
        {ANSWER_LIST[6]}   |    {ANSWER_LIST[7]}    |    {ANSWER_LIST[8]}
            |         |
    '''
print(QUIZ)

##### Play a game
##### AI
import random
select_player = select_players() # 'O' or 'X'
keep_going = True
if select_player == 'O':
    another_player = 'X'
else:
    another_player = 'O'
print(f'Player 1 : {select_player} vs. Player 2 : {another_player}')
for _ in range(len(ANSWER_LIST)):
    while keep_going:
        if check_end(ANSWER_LIST):
            print(f'Congratulation! You Win!')
            keep_going = False
        else:    
            computer_going = True
            select_position = input('Which one do you want to get? 1~9 : ')
            if ANSWER_LIST[int(select_position) -1] == select_position: # '1~9'
                ANSWER_LIST[int(select_position) -1] = select_player
                while computer_going:
                    computer_position = random.randint(1, 9)
                    if ANSWER_LIST[computer_position -1] == select_player or ANSWER_LIST[computer_position -1] == another_player: # already positioned by the player
                        if check_end(ANSWER_LIST):
                            print(f'You Lose!')
                            computer_going = False
                            keep_going = False
                        else:
                            pass
                    else:
                        ANSWER_LIST[computer_position -1] = another_player # 
                        computer_going = False
                        print(ANSWER_LIST)
                
                # count_position = input('Which one do you want to ')
            elif ANSWER_LIST[int(select_position) -1] == another_player:
                print(f'This position is already selected for another player. Please select another position.') 
                print(ANSWER_LIST)
            else:
                print(f'This position is already selected for you. Please select another position.') 
                print(ANSWER_LIST)
            QUIZ = f'''
                |         |
            {ANSWER_LIST[0]}   |    {ANSWER_LIST[1]}    |    {ANSWER_LIST[2]}
        ________|_________|_________
                |         |
            {ANSWER_LIST[3]}   |    {ANSWER_LIST[4]}    |    {ANSWER_LIST[5]}
        ________|_________|_________
                |         |
            {ANSWER_LIST[6]}   |    {ANSWER_LIST[7]}    |    {ANSWER_LIST[8]}
                |         |
        '''
            print(QUIZ)



