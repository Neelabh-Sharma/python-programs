"""
This Program is a play stone,paper and scissors
between human and AI
"""
import random

def main():
    """
    This is a main body of program!
    """
    instructions()
    for i in range(3):
        human_value=human_input()
        ai_value=ai_input()
        win=winner(human_value,ai_value)
        print(win)
        print("")
    print(score)


def instructions():
    """
    :return:This function only print a set of instruction for user!
    """
    print("Hello Guys this is stone,paper and scissors game!")
    print("1)Stone beats scissors\n2)scissors beats paper\n3)paper beats stone")
    print("______________________________Let's Start!__________________________")

def human_input():
    """
    This function accept user input!
    check it!
    :return:the value like 'stone','paper'&'scissors'
    """
    while True:
        value=input("Enter the value>")
        if value=='stone' or value=='Stone' or value=='STONE':
            return 'stone'
        if value == 'paper' or value == 'Paper' or value == 'PAPER':
            return 'paper'
        if value == 'scissors' or value == 'Scissors' or value == 'SCISSORS':
            return 'scissors'
        print("Check the input")

def ai_input():
    """
    This function produce ai input randomly!
    :return: the value like 'stone','paper'&'scissors'
    """
    ran=random.randint(1,3)
    if ran == 1:
        return 'stone'
    if ran == 2:
        return 'paper'
    if ran == 3:
        return 'scissors'

def winner(human_input,ai_input):
    """
    This function accept two input as following
    :param human_input: input from human/user
    :param ai_input:  input from AI
    :return: 'winner'& 'score of human/user'
    """
    global score
    score=0
    if human_input == ai_input:
        score +=0
        return 'tie'
    if human_input == 'stone':
        if ai_input == 'paper':
            score -=1
            return 'ai win'
        score +=1
        return 'human win'
    if human_input == 'paper':
        if ai_input == 'scissors':
            score -=1
            return 'ai win'
        score +=1
        return 'human win'
    if human_input == 'scissors':
        if ai_input == 'stone':
            score -=1
            return 'ai win'
        score +=1
        return 'human win'

if __name__== '__main__':
    main()