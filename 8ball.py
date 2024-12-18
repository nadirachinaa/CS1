import random

responses = ["yes", "no", "maybe", "ask later"]                                                      #the computer will generate random words for responses 
question_words = ["am", "will", "is", "how", "where", "what", "who"]                                 #the first word of the users questions 

while True:                                                                                          #while the code is true
    question = input('HI! Im your magic 8 ball!! Whats your question? Enter stop to end. ').lower()  #asking the user ifthey want to play
    first_word = question.split()[0]                                                                 #the first word split

    if question == "stop":                                                                           #if the user types stop
        break                                                                                        #break code
    elif "?" in question and first_word in question_words:                                           #has to have ? mark and the first word has to be one of the question words 
        print(random.choice(responses))                                                              #prints random response 
    else:                                                                                            #if the code was something else
        print("That's not a question!")                                                              #print that the question isnt a question 
