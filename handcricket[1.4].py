import random

print("\nWelcome back! Let's play 'Hand Cricket'")
print("The test match and super over features are under development!")
print("""\nGame Description:
      This game consists of two formats viz T20 and One Day
      A T20 match consists of 20 overs while an One Day match consists of 50 overs
Rules:
      You would be asked to choose your runs on each ball
      Computer will randomly choose runs and compare it with yours
      If it matches you will lose a wicket else the rules are as follow:
      If you chose 0 or 1 or 2 - Your score would be added by your choice
      If you chose 3 or 5 - Your score would be added by the absolute of (Your choice - Computer choice)
      If you chose 4 - If Computer chose 3 or 5 your score would be added by 2 runs else by 4 runs
      If you chose 6 - If computer chose 4 or 5 your score would be added by the absolute of (Your choice - Computer choice) else by 6 runs
      Same for the computer innings too
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
                computer_wish=random.randint(1,2)
                if computer_wish==1:
                    print("Computer won the toss and decided to bat first")
                    return 2
                else:
                    print("Computer won the toss and decided to bowl first")
                    return 1


def yourinnings(format,state,computer_score=0):
        score = 0
        wickets = 0
        overs = 0
        balls = 0
        run_rate=0.0
        print(f"Your score is {score}/{wickets}({overs}.{balls})")
        if state==2:
            if format==1:
                        print(f"Required Run Rate: {round(((computer_score-score+1)*6)/(((20-overs-1)*6+(6-balls))),2)}")
            elif format==2:
                        print(f"Required Run Rate: {round(((computer_score-score+1)*6)/(((50-overs-1)*6+(6-balls))),2)}")
        if ( format == 1 or format == 2):
            mainflag=True
            counter=0
            while mainflag:
                if state==1:
                    if format==1:
                        if (overs==20 or wickets==10):
                            print("That's end of an innings\n")
                            print(f"Computer requires {score+1} runs in 120 balls to win!")
                            mainflag=False
                            return score
                    else:
                        if (overs==50 or wickets==10):
                            print("That's end of an innings\n")
                            print(f"Computer requires {score+1} runs in 300 balls to win!")
                            mainflag=False
                            return score
                else:
                    if (computer_score>=score):
                        if format==1:
                            if (overs==20 or wickets==10):
                                if computer_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print(f"That's end of an innings\nComputer wins by {computer_score-score} runs!!\n------")
                                mainflag=False
                                return score
                        else:
                            if (overs==50 or wickets==10):
                                if computer_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print(f"That's end of an innings\nComputer wins by {computer_score-score} runs!!\n------")
                                mainflag=False
                                return score
                    elif(computer_score<score):
                        if wickets<9:
                            print(f"Hurray! You win by {10-wickets} wickets!!\n-----")
                        else:
                            print(f"Hurray! You win by {10-wickets} wicket!!\n-----")
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
                                if counter==0:
                                    user_choice_status=user_choice
                                    counter+=1
                                elif counter>=1:
                                    if user_choice==user_choice_status:
                                        computer_choice=user_choice
                                        counter+=1
                                    else:
                                        counter=0       
                                balls+=1
                                break
                        except ValueError:
                            print("Please enter correct range!")
                if ( balls==6):
                    overs+=1
                    balls=0
                if counter<2:
                    if run_rate>10.0:
                        computer_choice=random.randint(2,6)
                    else:
                        computer_choice=random.randint(0,6)
                if ( computer_choice == user_choice):
                    wickets+=1
                    print(f"Computer choice was {computer_choice}\nThat's a wicket!")
                    print(f"Your score is {score}/{wickets}({overs}.{balls})")
                    print(f"Current Run Rate:{round((score*6/((overs*6)+balls)),2)}")
                else:
                    score1=score
                    if user_choice == 3 or user_choice == 5:
                        score+=abs(user_choice-computer_choice)
                    elif user_choice == 4:
                        if computer_choice == 3 or computer_choice==5:
                            score+=2
                        else:
                            score+=4
                    elif user_choice == 6:
                        if computer_choice>=4:
                            score+=abs(user_choice-computer_choice)
                        else:
                            score+=6
                    else:
                        score+=user_choice 
                    run_rate=round((score*6/((overs*6)+balls)),2)   
                    print(f"Computer choice was {computer_choice}\nThat's a {score-score1}!")
                    print(f"Your score is {score}/{wickets}({overs}.{balls})\nCurrent Run Rate:{run_rate}")
                if state==1:
                    if overs>=5:
                        if format==1 and wickets!=10 and (wickets<=7 or overs>=15):
                            print(f"Projected Score: {round(run_rate*20)}")
                        elif format==2 and wickets!=10 and (wickets<=7 or overs>=45 or overs>=15):
                            print(f"Projected Score: {round(run_rate*50)}")
                elif state==2:
                    if format==1 and computer_score>=score and wickets!=10:
                        print(f"You require {computer_score-score+1} runs from {120-balls-(overs*6)} balls to win. Required Run Rate: {round(((computer_score-score+1)*6)/(((20-overs-1)*6+(6-balls))),2)}")
                    elif format==2 and computer_score>=score and wickets!=10:
                        print(f"You require {computer_score-score+1} runs from {300-balls-(overs*6)} balls to win. Required Run Rate: {round(((computer_score-score+1)*6)/(((50-overs-1)*6+(6-balls))),2)}")

def computerinnings(format,state,user_score=0):
        score = 0
        wickets = 0
        overs = 0
        balls = 0
        run_rate=0.0
        print(f"Computer score is {score}/{wickets}({overs}.{balls})")
        if state==2:
            if format==1:
                        print(f"Required Run Rate: {round(((user_score-score+1)*6)/(((20-overs-1)*6+(6-balls))),2)}")
            elif format==2:
                        print(f"Required Run Rate: {round(((user_score-score+1)*6)/(((50-overs-1)*6+(6-balls))),2)}")
        if ( format == 1 or format == 2):
            mainflag=True
            while mainflag:
                if state==1:
                    if format==1:
                        if (overs==20 or wickets==10):
                            print("That's end of an innings\n")
                            print(f"You require {score+1} runs in 120 balls to win!")
                            mainflag=False
                            return score
                    else:
                        if (overs==50 or wickets==10):
                            print("That's end of an innings\n")
                            print(f"You require {score+1} runs in 300 balls to win!")
                            mainflag=False
                            return score
                else:
                    if (user_score>=score):
                        if format==1:
                            if (overs==20 or wickets==10):
                                if user_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print(f"That's end of an innings\nYou win by {user_score-score} runs!!\n------")
                                mainflag=False
                                return score
                        else:
                            if (overs==50 or wickets==10):
                                if user_score==score:
                                    print("That's end of an innings\nThe match is tied!!\n------")
                                else:
                                    print(f"That's end of an innings\nYou win by {user_score-score} runs!!\n------")
                                mainflag=False
                                return score
                    elif(user_score<score):
                        if wickets<9:
                            print(f"Computer wins by {10-wickets} wickets!!\n------")
                        else:
                            print(f"Computer wins by {10-wickets} wicket!!\n------")
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
                if (balls==6):
                    overs+=1
                    balls=0
                if state==2:
                    required_rate1=round(((user_score-score+1)*6)/(((20-overs-1)*6+(6-balls))),2)
                    required_rate2=round(((user_score-score+1)*6)/(((50-overs-1)*6+(6-balls))),2)
                    if format==1:
                        if required_rate1>8.0:
                            computer_choice=random.randint(4,6)
                        else:
                            computer_choice=random.randint(0,6)
                    elif format==2:
                        if required_rate2>8.0:
                            computer_choice=random.randint(4,6)
                        else:
                            computer_choice=random.randint(0,6)
                else:
                    if run_rate<4.0:
                        computer_choice=random.randint(4,6)
                    else:
                        computer_choice=random.randint(0,6)

                if ( computer_choice == user_choice):
                    wickets+=1
                    print(f"Computer choice was {computer_choice}\nThat's a wicket!")
                    print(f"Computer score is {score}/{wickets}({overs}.{balls})")
                    print(f"Current Run Rate:{round((score*6/((overs*6)+balls)),2)}")
                else:
                    score1=score
                    if computer_choice == 3 or computer_choice == 5:
                        score+=abs(user_choice-computer_choice)
                    elif computer_choice == 4:
                        if user_choice == 3 or user_choice==5:
                            score+=2
                        else:
                            score+=4
                    elif computer_choice == 6:
                        if user_choice>=4:
                            score+=abs(user_choice-computer_choice)
                        else:
                            score+=6
                    else:
                        score+=computer_choice 
                    run_rate=round((score*6/((overs*6)+balls)),2) 
                    print(f"Computer choice was {computer_choice}\nThat's a {score-score1}!")
                    print(f"Computer score is {score}/{wickets}({overs}.{balls})\nCurrent Run Rate:{run_rate}")
                if state==1:
                    if overs>=5:
                        if format==1 and wickets!=10 and (wickets<=7 or overs>=15):
                            print(f"Projected Score: {round(run_rate*20)}")
                        elif format==2 and wickets!=10 and (wickets<=7 or overs>=45):
                            print(f"Projected Score: {round(run_rate*50)}")
                elif state==2:
                    if format==1 and user_score>=score and wickets!=10:
                        print(f"Computer requires {user_score-score+1} runs from {120-balls-(overs*6)} balls to win. Required Run Rate: {round(((user_score-score+1)*6)/(((20-overs-1)*6+(6-balls))),2)}")
                    elif format==2 and user_score>=score and wickets!=10:
                        print(f"Computer requires {user_score-score+1} runs from {300-balls-(overs*6)} balls to win. Required Run Rate: {round(((user_score-score+1)*6)/(((50-overs-1)*6+(6-balls))),2)}")
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
        print("Thanks for playing! See you soon!")
        break
    else:
        print("Enter the correct choice")
        



    