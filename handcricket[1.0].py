import random

print("Welcome back! Let's play 'Hand Cricket'")
print("The test match feature is under development!")
print("""\nGame Description:
      This game consists of two formats viz T20 and One Day
      A T20 match consists of 20 overs while an One Day match consists of 50 overs
Rules:
      You would be asked to choose your runs on each ball
      Computer will randomly choose runs and compare it with yours
      If it matches you will lose a wicket else yout runs are added to your score
      You have only 10 wickets so play wisely
      After an innings,next innings would be started
      The winner is decided as in the case normal cricket rules
""")

def formatchoice():
    try:
        format_choice = int(input("Enter '1' for a T20 match or '2' for an One Day match :"))
        if format_choice==1 or format_choice==2:
            return format_choice
        else:
            print("Enter a correct option")
            formatchoice()
    except ValueError:
        print("Enter a correct option")
        formatchoice()

def toss():
    print("Toss time!")
    while True:

            user_toss1=input("Enter Your choice (Heads -> 'H' or Tails -> 'T'): ")
            user_toss=user_toss1.upper()
            list_toss=["H","T"]
            computer_toss=random.randint(0,1)
            if user_toss!="H" and user_toss!="T":
                print("Enter the correct choice")
                continue
            if ( list_toss[computer_toss]== user_toss):
                print("You have won the toss!!")
                while True:
                    try:
                        innings_selection=int(input("Enter '1' to bat first or '2' to bowl first: "))
                        if innings_selection!=1 and innings_selection!=2:
                            print("Enter the correct choice")
                            continue
                        else:
                            if innings_selection==1:
                                print("You will bat first!")
                                return 1
                            else:
                                print("You will bowl first!")
                                return 2
                    except ValueError:
                        print("Enter the correct choice")
            else:
                print("Computer won the toss and decided to bowl first")
                return 1


def yourinnings(format,state,computer_score=0):
        score = 0
        wickets = 0
        overs = 0
        balls = 0
        print(f"Your score is {score}/{wickets}({overs}.{balls})")
        if ( format == 1 or format == 2):
            mainflag=True
            while mainflag:
                if state==1:
                    if format==1:
                        if (overs==20 or wickets==10):
                            print("That's end of an innings\n")
                            mainflag=False
                            return score
                    else:
                        if (overs==50 or wickets==10):
                            print("That's end of an innings\n")
                            mainflag=False
                            return score
                else:
                    if (computer_score>=score):
                        if format==1:
                            if (overs==20 or wickets==10):
                                if computer_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print("That's end of an innings\nComputer Wins!!\n------")
                                mainflag=False
                                return score
                        else:
                            if (overs==50 or wickets==10):
                                if computer_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print("That's end of an innings\nComputer Wins!!\n------")
                                mainflag=False
                                return score
                    elif(computer_score<score):
                        print("Hurray! You won!!\n-----")
                        mainflag=False
                        return score

                flag1=True
                while flag1:
                        try:
                            user_choice=int(input("Enter your runs for this ball (0 to 6) :"))
                            if user_choice<0 or user_choice>6:
                                print("Enter the correct range!")
                                continue
                            else:
                                balls+=1
                                break
                        except ValueError:
                            print("Please enter correct range!")
                if ( balls==6):
                    overs+=1
                    balls=0
                computer_choice=random.randint(0,6)
                if ( computer_choice == user_choice):
                    wickets+=1
                    print(f"Computer choice was {computer_choice}\nThat's a wicket!")
                    print(f"Your score is {score}/{wickets}({overs}.{balls})")
                else:
                    score+=user_choice
                    print(f"Computer choice was {computer_choice}\nThat's a {user_choice}!")
                    print(f"Your score is {score}/{wickets}({overs}.{balls})")

def computerinnings(format,state,user_score=0):
        score = 0
        wickets = 0
        overs = 0
        balls = 0
        print(f"Computer score is {score}/{wickets}({overs}.{balls})")
        if ( format == 1 or format == 2):
            mainflag=True
            while mainflag:
                if state==1:
                    if format==1:
                        if (overs==20 or wickets==10):
                            print("That's end of an innings\n")
                            mainflag=False
                            return score
                    else:
                        if (overs==50 or wickets==10):
                            print("That's end of an innings\n")
                            mainflag=False
                            return score
                else:
                    if (user_score>=score):
                        if format==1:
                            if (overs==20 or wickets==10):
                                if user_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print("That's end of an innings\nYou Won!!\n------")
                                mainflag=False
                                return score
                        else:
                            if (overs==50 or wickets==10):
                                if user_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print("That's end of an innings\nYou Won!!\n------")
                                mainflag=False
                                return score
                    elif(user_score<score):
                        print("Computer wins!!\n------")
                        mainflag=False
                        return score
                

                flag1=True
                while flag1:
                        try:
                            user_choice=int(input("Enter your runs for this ball (0 to 6) :"))
                            if user_choice<0 or user_choice>6:
                                print("Enter the correct range!")
                                continue
                            else:
                                balls+=1
                                break
                        except ValueError:
                            print("Please enter correct range!")
                if ( balls==6):
                    overs+=1
                    balls=0
                computer_choice=random.randint(0,6)
                if ( computer_choice == user_choice):
                    wickets+=1
                    print(f"Computer choice was {computer_choice}\nThat's a wicket!")
                    print(f"Computer score is {score}/{wickets}({overs}.{balls})")
                else:
                    score+=computer_choice
                    print(f"Computer choice was {computer_choice}\nThat's a {computer_choice}!")
                    print(f"Computer score is {score}/{wickets}({overs}.{balls})")

def cricketgame():
    format=formatchoice()
    state1=toss()
    if state1==1:
        state2=2
        yourscore=yourinnings(format,state1,0)
        computerinnings(format,state2,yourscore)
    else:
        state2=1
        computerscore=computerinnings(format,state2,0)
        yourinnings(format,state1,computerscore)
    
cricketgame()

while True:
    ask1=input("Do you want to play again? (Yes -> 'Y' or no -> 'N') :")
    ask=ask1.upper()
    if ask=="Y":
        cricketgame()
    elif ask=="N":
        break
    else:
        print("Enter the correct choice")
        



    