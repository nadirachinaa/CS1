import os
import random
import time

'''
Author: Nadira china

Bugs:

Args:
'''


win_art = '''
⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀
⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⣤⣤⣠
⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠶⠶⡆⡼
⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢸⢁⡗
⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⢀⡏⡼⠀
⠀⠀⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢀⠞⡼⠁⠀
⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀⠀
⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠓⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠃⠀⠀⠀⠀⠀⠀
'''
lose_art = '''
⢻⢭⡓⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠸⣏⢖⡲⣅⠀⠀
⣣⢾⡛⣜⢫⣦⠀⠀⢀⣤⠴⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣸⢏⡝⣆⢀
⢿⣧⢹⣬⡷⣚⣒⣶⡾⣍⡞⡱⣞⡇⠀⠀⠀⠀⢀⣠⢤⠖⣦⡤⠤⡶⠦⠤⣤⢶⠲⠤⣄⠀⠀⠀⠀⠀⢀⡤⠶⢶⢤⡀⢸⣛⣮⢞⡜⡚
⠈⡷⣻⢏⠶⣙⢶⣼⠟⡼⣜⡵⠋⠀⠀⠀⣠⠞⡩⢴⣿⣿⣾⣹⠐⢢⢁⡾⡵⠚⢻⣷⣤⡙⠲⢄⠀⠀⢾⣍⡻⣌⢧⣷⡾⡞⣥⢫⡝⣃
⠀⢻⣿⢊⣟⣾⢫⢇⡻⣱⢺⠁⠀⠀⠀⡼⣡⣿⣄⣀⡿⣿⣿⡏⡇⢢⢸⡿⣷⣤⣼⠿⢿⣿⣷⣎⣷⠀⠈⠳⣵⡩⢖⡻⣱⢻⣌⡳⢎⡵
⠀⠀⢻⡧⢞⡧⣋⣮⣕⡣⢿⠀⠀⢀⡼⢃⣻⢿⣿⣿⣧⠾⠟⡙⣧⣂⣌⢣⡛⡿⠿⠷⠾⠿⠿⠣⣌⠳⡀⢰⢯⡱⣫⡶⢥⣛⢮⡓⣏⢶
⠀⠀⠈⢯⡧⣓⢧⡚⣽⣞⡾⠀⢀⡞⠠⣿⠀⡰⢂⣖⣤⣯⣾⣿⣿⣿⣿⣿⣿⣇⠄⣎⣱⣉⢎⡱⣘⡇⠹⡞⣮⢵⢯⣱⠳⡬⢧⡙⣦⠋
⠀⠀⠀⠈⠳⣭⢲⡹⢲⡞⠁⠀⣼⢐⠡⡙⠳⠗⡛⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⡉⠛⣶⣵⠋⡐⢿⠈⠻⣆⢧⡛⢜⣣⠟⠁⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⢰⡇⢊⠔⡡⢊⠔⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠡⣿⢹⡄⢡⢚⣇⠀⠈⠉⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢊⠤⢑⠢⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢹⠃⢢⢻⡄⢊⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠌⢢⠁⢎⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⢿⣿⣿⣿⣿⣿⣿⣏⡄⢣⢺⡇⢼⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡊⠤⠉⢼⣿⣿⣿⣿⠿⠋⡄⠒⡌⢢⠐⡌⠻⣿⣿⣿⣿⣯⠛⢓⠛⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡘⡏⣿⣿⣿⡿⠋⡄⠣⠌⡱⢈⠄⢣⠐⡡⠘⢿⣿⣿⣿⡐⣌⢒⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡅⠸⠿⢛⡡⠘⡄⠣⡘⠄⠣⡘⠄⢣⠐⣉⠂⠻⢿⠿⠁⢼⡲⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣁⠦⠟⡁⢣⠐⡡⠂⡍⠰⢁⠎⡄⠣⢄⡉⠲⢦⣂⣉⢴⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢲⢥⣂⠅⣂⠑⡈⢅⠊⡐⠌⢡⢂⣌⣡⠶⣛⣙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''


def print_board(board):
    print('  1     2     3     4     5  ')
    print(f'1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}')
    print('  ------------------------')
    print(f'2 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][2]} | {board[1][3]}')
    print('  ------------------------')
    print(f'3 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}')
    print('  ------------------------')
    print(f'4 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]}')
    print('  ------------------------')
    print(f'5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}')


def place_ships(board):
    while True:
        try: 
            row = int(input('Enter ship row: ')) - 1
            column = int(input('Enter ship column: ')) - 1

            if row > 4 or row < 0 or column > 4 or column < 0:
                print('Please enter a valid number')
            elif board[row][column] != '⚓':
                print('Please enter an available spot')
            else:
                board[row][column] = '🚢'
                break
        except ValueError:
            print('Enter integers only')


def take_shots(real_board, display_board, hits):      
    while True:
        try: 
            row = int(input('Enter shot row: ')) - 1
            column = int(input('Enter shot column: ')) - 1

            if row > 4 or row < 0 or column > 4 or column < 0:
                print('Please enter a valid number')
            elif display_board[row][column] != '⚓':
                print('Please enter an available spot')
            else:
                break
        except ValueError:
            print('Enter integers only')

    if real_board[row][column] == '🚢':
        display_board[row][column] = '🔥'
        print("Wow! You hit one!")
        hits += 1
        return hits

    else:
        display_board[row][column] = '✖️'
        print("You missed!")


def main():
    while True:
        answer = input("Hello! Want to play Battleship? Type 'yes' to continue! ").lower()
        
        if answer != 'yes':
            print("okay, bye!")
            break

        real_board_player1 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]
        
        real_board_player2 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]
        
        display_board_player1 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]
        
        display_board_player2 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]
        p1_hits = 0
        p2_hits = 0

        print('Placing ships for player 1...')
        time.sleep(1)                                   #pauses the function for however many seconds are in parenthesis in this case (1)
        print_board(real_board_player1)
        
        for i in range(4):
            print(f'Player 1, place ship #{i+1}')
            place_ships(real_board_player1)
            print_board(real_board_player1)
        time.sleep(2)
        os.system('cls')

        print('Placing ships for player 2...')
        time.sleep(1)
        print_board(real_board_player2)

        for i in range(4):
            print(f'Player 2, place ship #{i+1}')
            place_ships(real_board_player2)
            print_board(real_board_player2)
        time.sleep(2)
        os.system('cls')

        print('Time to take shots!')

        while True:
            print('Player 1, take a shot!')
            time.sleep(1)
            print_board(display_board_player2)  
            p1_hits = take_shots(real_board_player2, display_board_player2, p1_hits)

            if p1_hits == 4:
                print_board(display_board_player2)  
                print('Player 1 wins!')
                break

            print('Player 2, take a shot!')
            time.sleep(1)
            print_board(display_board_player1)  
            p2_hits = take_shots(real_board_player1, display_board_player1, p2_hits)

            if p2_hits == 4:
                print_board(display_board_player1)  
                print('Player 2 wins!')
                break
    
main()
