import sys

print(sys.version)
def get_login_signup():
    is_valid=0
    while is_valid!=1:
        user_input=input("Welcome! Login or Signup?\n===>").lower()
        if user_input=="login":
            login()
            print('login')
            is_valid=1
        elif user_input=="signup":
            signup()
            print('signup')
            is_valid=1
        else:
            print("Invalid option, check your spelling")

# def signup():
    


def get_round_multiplier():
    is_acceptable_value=0
    while is_acceptable_value!=1:
        user_input=input("1.5x, 2x, or 3x, type your multiplier\n===>")
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
    return multiplier





