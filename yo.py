friends_name = []
friends_age = []
friends_ranking = []
def add_friend():
    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = raw_input("Age?")
    new_age = int(new_age)

    new_ranking = raw_input("Spy ranking?")
    new_ranking = str(new_ranking)

    if len(new_name) > 0 and new_age > 12 and new_ranking >= spy_rank:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_ranking.append(new_ranking)
        print  new_name + " "  +'Added'+" " + "as friend"
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)


def ask_name():
    spy_name = raw_input("Enter Your Name")
    if len(spy_name)>0:
        return spy_name
    else:
        print ("Please enter a name")
        ask_name()
def ask_salutation(name):
    spy_salutaion = str.upper(raw_input("What do you  want me to call you Mr. Or Miss."))
    if len(spy_salutaion)>0:
        if str(spy_salutaion) == "MR":
            full_name = str(spy_salutaion)  + str(name)
            return full_name
        elif str(spy_salutaion) == "MISS":
            full_name = str(spy_salutaion)  + str(name)
            return full_name
        else:
            print("enter valid option")
        ask_ranking(name)


def ask_ranking(name):
    spy_ranking = (raw_input("enter your rank"))
    spy_ranking = int(spy_ranking)
    if spy_ranking == 1 :
        spy_rank = str(" welcome admiral " + str(name))
        print spy_rank
    elif spy_ranking== 2 :
        spy_rank = str("welcome sergent "  + str(name))
        print spy_rank
    elif spy_ranking >= 3 :
        spy_rank = str("welcome cadet " + str(name))
        print spy_rank
    else:
        print str("enter valid number")
from setails import spy_name, spy_salutation, spy_rank, spy_age, spy_is_online, spy_post
print "Hello! Let\'s get started"
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = raw_input(question)
if existing == ("y"):
    print "Authentication complete. Welcome " +spy_salutation + spy_name + " age: " + str(spy_age) + " and rank: " + str(spy_rank) + " Proud to have you onboard" +" " + str(spy_post)
else:
    ask_ranking(ask_salutation(ask_name()))
show_menu = True


menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
menu_choice = raw_input(menu_choices)

if len(menu_choice) > 0:
        menu_choice = int(menu_choice)

        if menu_choice == 1:
             'You chose to update the status'
             add_status = raw_input('enter your status' )
             current_status = add_status
             print  "your current_status is" + " " + current_status
        elif menu_choice == 2:
            print'you want to add a friend'
            add_friend()
        elif menu_choice == 3:
            print 'you want to send a secret message'
        elif menu_choice == 4:
            print 'you want to read a secret message'
        elif menu_choice == 5:
            print 'you want to read chats from a user'
        else:
            show_menu = False