import random
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
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠓⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠖⠃⠀⠀⠀⠀⠀⠀
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
rps =["rock", "paper", "scissors"]                                                                                             # rock paper scissors list/chain

while True:                                                                                                                    # Forver loop 
    user_score = 0                                                                                                             # the players score
    bot_score = 0                                                                                                              # the bots score
    score_limit = 5                                                                                                            # the score limmit to win
    play = input("Hello friend! Wanna play rock, paper, scissors? Enter 'q' to quit and anything else to continue.")

    if play == "q":
        break
    
    while user_score < score_limit and bot_score < score_limit:
        user_rps = input("choose ur weapon!:")
        computer_rps = random.choice(rps)
        
        print(f"You chose {user_rps}, while the bot chose {computer_rps}")
        
        if user_rps == computer_rps:
            print("you tied!!!")
        elif user_rps =="rock" and computer_rps =="paper":
            print("bot wins!!!!")
            bot_score += 1
        elif user_rps =="rock" and computer_rps =="scissors":
            print("user wins!!!!")
            user_score += 1
        elif user_rps == "paper" and computer_rps =="scissors":
            print("bot wins!!!!")
            bot_score += 1
        elif user_rps == "paper" and computer_rps =="rock":
            print("user wins!!!!")
            user_score += 1
        elif user_rps== "scissors" and computer_rps =="rock":
            print("bot wins!!!!")
            bot_score += 1
        elif user_rps== "scissors" and computer_rps =="rock":
            print("user wins!!!!")
            user_score += 1
        else:
            print("Invalid")
        print(f"User: {user_score} - Bot: {bot_score}")

    if user_score > bot_score:
        print ("YESS YOU WINN BADDIEE!!")
        print(win_art)
    else:
        print("YOU LOSE")
        print(lose_art)







 
