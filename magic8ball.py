#Name: Hillel Finder
    #Prog Purpose: This Magic 8-Ball code uses a Python tuple since the user
    #does not ave the ability to change 8-Ball Answers.
    #However the program could have used a Python list instead of a tuple.
#NOTE: Tuples use parenthese; lists use square-braces.

import random
answers_8_ball = ("As I see it, yes", "Ask again later", "Better not tell you now",
                  "Cannot predict now", "Concentate and ask again", "Don't count on it",
                  "It is certain", "It is decidedly so", "Most likely",
                  "My reply is no", "My sources say no", "Outlook good!",
                  "Outlook not so good!", "Reply hazy; try again", "Signs point to yes",
                  "Very doubtful", "Without a doubt", "Yes", "Definitely yes",
                  "You may rely on it", "HELL YEAH BROTHER", "AIN'T NO WAY, SISTER", )

def main():

    print("I am the MAGIC 8-BALL and can answer any YES or NO question!")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the MAGIC 8-BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO question? ")
        print("The MAGIC 8-BALL says: ",answer)

        askAgain = input("\nWould you like to ask me another question (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO":
            another_question = False
        elif askAgain.upper() == "Y" or askAgain.upper() == "YES":
            another_question = True
        else:
            print("I'm magic, and even I don't know what that means. Yikes...")
            another_question = False

    print("\nCome back again when you have other important questions...")
    print("...MAGIC 8-BALL OUT!")

main()
