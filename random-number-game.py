import random
import sqlite3

def get_round_multiplier():
    is_acceptable_value=0
    print("1.5x, 2x, or 3x, type your multiplier")
    while is_acceptable_value!=1:
        user_input=input("===>")
        try: float(user_input)

        except:
            try: float(user_input[:-1])
            except:
                print("That's not a multiplier try again!")
            else:
                if float(user_input[:-1])==1.5 or float(user_input[:-1]) ==2.0 or float(user_input[:-1])==3.0:
                    multiplier=float(user_input[:-1])
                    is_acceptable_value=1
                else:
                    print("That's not a multiplier try again! Error 2")
        else: 
            if type(float(user_input))==float:
                if float(user_input)==1.5 or float(user_input) ==2.0 or float(user_input)==3.0:
                    multiplier=float(user_input)
                    is_acceptable_value=1
                else:
                    print("That's not a multiplier try again! Error 1")
                    continue

    if multiplier==1.5:
        end_range=2
    elif multiplier==2.0:
        end_range=3
    elif multiplier==3.0:
        end_range=10
    
    return [end_range,multiplier]

def is_number(user_input):
    try:
        float(user_input)
    except:
        return 0
    else:
        return 1

def get_wager():
    user_money=players["Teddy"]
    print(f"You have ${user_money:.2f}")
    print("How much do you wanna put down?")
    is_acceptable_value=0
    while is_acceptable_value!=1:
        user_input=input("===>")
        if is_number(user_input)==1: 
            if float(user_input)<=user_money:
                wager=float(user_input)
                is_acceptable_value=1
            else:
                print("Not enough money!")
        else:
            print("Try again! Not an acceptable value")
    return wager

def human_pick_number(end_range):
    is_acceptable_value=0
    print(f"Ok pick a number 1-{end_range}")
    while is_acceptable_value!=1:
        user_input=input(f"===>")
        if is_number(user_input)==1:
            if float(user_input)>=1 and float(user_input)<=end_range:
                return float(user_input)
            else:
                print("Not a valid number!")
        else:
            print("Not a valid number!")

def comp_pick_number(end_range):
    return random.randint(1,end_range)

def play_round(user):
    # user_money=players["Teddy"]
    wager=get_wager()
    multiplier_list=get_round_multiplier()
    end_range=multiplier_list[0]
    multiplier=multiplier_list[1]
    human_number=human_pick_number(end_range)
    computer_number=comp_pick_number(end_range)

    user_money=user_money-wager
    if human_number==computer_number:
        user_money=user_money+(wager*multiplier)
        # players["Teddy"]=user_money
        print("U WON!!!")
        print(f"You now have ${user_money:.2f}")
    else:
        # players["Teddy"]=user_money
        print("You lost :(")
        print(f"You now have ${user_money:.2f}")

    play_again=input("play again? y/n\n===>")
    if play_again=="y":
        play_round()
    else:
        return

# players={
#     "Teddy":10,
#     "Nathan":20
# }

def intro():
    print("""



===========================================================
WELCOME TO MULTI-PY. WHERE YOU CAN MULTI...PY YOUR MONEY!!!
===========================================================

            Login or signup to get started
                (type login or signup)





    """)

    is_valid=False
    while is_valid==False:
        l_or_s=input("===>").lower()
        if l_or_s=="login":
            login()
            is_valid=True
        elif l_or_s=="signup" or l_or_s=="sign up" or l_or_s=="sign-up":
            is_valid=True
            user_data=signup()
            return user_data
            
        else:
            print("Invalid option, check your spelling")
        
def signup():
    #Create database file and users table
    connection=sqlite3.connect('users.db')
    cur=connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS
    users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, money REAL)""")
    #User signup process
    print("""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
-----------------------------------------------------------
                        SIGN UP
       *Note: all users are saved locally and are not 
              accessable outside this computer
-----------------------------------------------------------
    
                Please Enter a Username




    """)
    is_valid=0
    while is_valid==0:
        user_input=input("===>")
        try:
            cur.execute("INSERT INTO users(username,password,money) VALUES(?,?,?)",(user_input,123,20.00))
            connection.commit()
            is_valid=1
        except:
            print("Username already exists.")

    

    def set_password(username):
        
        def set_inital_pass():
            print("""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
-----------------------------------------------------------
                        SIGN UP
       *Note: all users are saved locally and are not 
              accessable outside this computer
-----------------------------------------------------------
    
                Please Enter a Password




            """)
            pass_input=input("===>")
            if pass_input=="back":
                set_inital_pass()
            user_data=conf_pass(pass_input)
            return(user_data)

        def conf_pass(inital_pass):
            while True:
                print("""
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n      
-----------------------------------------------------------
                        SIGN UP
    *Note: all users are saved locally and are not 
            accessable outside this computer
-----------------------------------------------------------
    
            Please Confirm Your Password
            *Or type back to set it again



                """)
                
                conf_pass_input=input("===>")
                if conf_pass_input.lower()=="back":
                    return set_inital_pass()
                elif conf_pass_input==inital_pass:
                    cur.execute("UPDATE users SET password=? WHERE username=?",(conf_pass_input,username))
                    connection.commit()
                    cur.execute("SELECT * FROM users WHERE username=?",(username,))
                    data=cur.fetchone()
                    connection.commit()
                    return data
                else:
                    print("Passwords do not match")
        user_data=set_inital_pass()
        return user_data
    user_data=set_password(user_input)
    return user_data


def game():
    user_data=intro()
    print(user_data)
    # play_round(user)

game()