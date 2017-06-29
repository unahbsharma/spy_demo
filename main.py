#DIFFERENT FILES ARE IMPORTED
from setails import friends
from datetime import datetime

friends_name = []
friends_age = []
friends_ranking = []
# TO SELECT A FRIEND FROM FRIENDS LIST
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['name'],
                                                   friend['age'],
                                                   friend['rating'])
        item_number = item_number + 1

    friend_choice = int(raw_input ("Choose from your friends"))

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position
#STEGANOGRAPHY SCRIPT IS IMPORTED
from steganography.steganography import Steganography
#FUNCTION TO READ A MESSAGE
def read_message():
    sender = select_a_friend() #FRIEND IS SELECTED
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)  #MESSAGE IS DECODED
    if secret_text == str("help"):
        print("we have traced your location spy is on the way")
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)     #NEW CHAT IS UPDATED

    print "Your secret message has been saved!"
#FUNCTION TO SEND A MESSAGE
def send_message():
#MESSAGE DETAILS AS USER INPUT
  original_image = raw_input("What is the name of the image?")
  original_image= original_image
  output_path= raw_input("pic")
  output_path = str(output_path)
  text = raw_input("What do you want to say?")
  Steganography.encode(original_image, output_path, text)

  new_chat = {
      "message": text,
      "time": datetime.now(),
      "sent_by_me": True
  }

  friends[select_a_friend()] ['chats'].append(new_chat)

  print "Your secret message image is ready!"

#FUNCTION TO ADD A NEW FRIEND
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

#SPY NAME AS INPUT
def ask_name():
    spy_name = raw_input("Enter Your Name")
    if len(spy_name)>0:
        return spy_name
    else :
        print ("enter only valid characters")
    ask_name()
 #SPY SALUTATION AS INPUT
def ask_salutation(name):
    spy_salutaion = str.upper(raw_input("What do you  want me to call you Mr. Or Miss."))
    if len(spy_salutaion)>0:
        if spy_salutaion == "MR":
            full_name = str(spy_salutaion)  + str(name)
            return full_name
        elif spy_salutaion == "MISS":
            full_name = str(spy_salutaion)  + str(name)
            return full_name
    else:
        print("enter valid option")
        ask_salutation(name)
def read_history():
    read_for = select_a_friend()
    print ("you have selected/" + friends[read_for].salutation +friends [read_for].name + "select a chat history")
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print("[%s] %s: %s" % (chat.time.strftime("%d %B %Y"), 'your message was;',chat.mesage))
        else:
            print("[%s] $s said: %s" % (chat.time.strftime("%d %B % Y"), friends[read_for].name, chat.message))

#SPY RANK AS INPUT
def ask_ranking(name):
    spy_ranking = int(raw_input("enter your rank"))
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
#STARTING OF PROGRAM-------------------------------------------------------
print "Hello! Let\'s get started"
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = raw_input(question)
if existing == ("y"):
    print "Authentication complete. Welcome " +spy_salutation + spy_name + " age: " + str(spy_age) + " and rank: " + str(spy_rank) + " Proud to have you onboard" +" " + str(spy_post)
else:
    ask_ranking(ask_salutation(ask_name()))     #CALLING OF FUNCTIONS FOR USER INPUT
show_menu = True

#MENU OPTIONS TO CHOOSE FROM-----------------
menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chat history \n 6. close the application "
menu_choice = raw_input(menu_choices)
while menu_choice <= 0 or menu_choice > 6:
    menu_choice = int(raw_input('please enter a digit between 1-6'))

#ACTION ACCORDING TO THE CHOICE OF USER

    if menu_choice == 1:
        'You chose to update the status'
        add_status = raw_input('enter your status')
        current_status = add_status
        print  "your current_status is" + " " + current_status
    elif menu_choice == 2:
        print'you want to add a friend'
        add_friend()
    elif menu_choice == 3:
        print 'you want to send a secret message'
        send_message()
    elif menu_choice == 4:
        print 'you want to read a secret message'
        read_message()
    elif menu_choice == 5:
        print 'you want to read chat history'
        read_history()
    elif menu_choice == 6:
        exit()
    else:


            show_menu = False