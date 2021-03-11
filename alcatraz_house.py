import time
subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")



player = input("What is your name? ")
print("You wake up in a strange room. Looking around the room you see a note, you walk over and start to read the note.")
time.sleep(3)
print("")
print("Hello " + player + ", welcome to my house.")
print("To escape you must solve my riddles")
print("Pick the correct door and you'll be free!")
print("Pick the wrong door and... well lets just say you dont want to pick the wrong door")
print("")
time.sleep(8)
print("Looking around the room you see two doors, one marked A and another marked B. There is a plaque mounted on the wall between them")
print("The plaque says this:")
print("")
def start_game():
    time.sleep(3)
    geog_question()
    

def geog_question():
    print("Question 1. What is the capital of France?")
    print("A. Paris")
    print("B.London")
    print("Type A or B")
    capital_city_answer = input("")
    if capital_city_answer in ("a", "A"):
        print("")
        print("Go through door A")
        time.sleep(2)
        print("In front of you are two more doors and another plaque, this plaque reads:")
        print("Well done " + player + ", you know your geography!")
        print("")
        print("The first clue is 4")      
        print("")
        shape_question()

    elif capital_city_answer in ("b", "B"):
        print("")
        print("Go through door B")
        time.sleep(2)
        print("Here you find another plaque, this plaque reads:")
        print("You are trapped, you need to revise your geography to escape. Start again!")
        time.sleep(2)
        print("You hear a hissing and start to feel dizzy, you wake up in the first room")
        print("")
        time.sleep(2)
        start_game()
    else:
        print("Type A or B ")
        geog_question()



def shape_question():
    print("Question 2. How many sides does an octagon have?")
    print("A. 5")
    print("B. 8")
    print("Type A or B")
    shape_answer = input("")
    if shape_answer.lower() == "a":
        print("")
        print("Go through door A")
        time.sleep(2)
        print("Here you find another plaque, this plaque reads:")
        print("You are trapped, you need to revise your shapes to escape. Start again!")
        time.sleep(2)
        print("You hear a hissing and start to feel dizzy, you wake up in the first room")
        print("")
        time.sleep(2)
        start_game()
        
    elif shape_answer.lower() == "b":
        print("")
        print("Go through door B")
        time.sleep(2)
        print("Infront of you are two more doors and another plaque, this plaque reads:")
        print("Well done " + player + ", you know your shapes!")
        print("")
        print("The second clue is 9")
        horse_question()
    else:
        print("Type A or B ")
        shape_question()




def horse_question():
    print("")
    print("Question 3. What do you call a female horse?")
    print("A. Mare")
    print("B. Doe")
    print("Type A or B")
    horse_answer = input("")
    if horse_answer.lower() == "a":
        print("")
        print("Go through door A")
        time.sleep(2)
        print("Infront of you are two more doors and another plaque, this plaque reads:")
        print("Well done " + player + ", you know your animals!")
        print("The third clue is 3")
        chemical_question()


    elif horse_answer.lower() == "b":
        print("")
        print("Go through door B")
        time.sleep(2)
        print("Here you find another plaque, this plaque reads:")
        print("You are trapped, you need to revise your animals to escape. Start again!")
        time.sleep(2)
        print("You hear a hissing and start to feel dizzy, you wake up in the first room")
        print("")
        time.sleep(2)
        start_game()
    else:
        print("Type A or B ")
        horse_question()



def chemical_question():
    print("")
    print("Question 4. What is the chemical equation of water?")
    print("A. H2O".translate(subscript))
    print("B. HO2".translate(subscript))
    print("Type A or B")
    chemical_answer = input("")
    if chemical_answer.lower() == "a":
        print("")
        print("Go through door A")
        time.sleep(2)
        print("Well done " + player + ", you know your chemestry!")
        print("")
        print("The final clue is 6")
        print("")
        print("Now you choose a door")
        time.sleep(2)
        print("")
        print("Get it right and you're free")
        time.sleep(2)
        print("Get it wrong and well, we'll see")
        time.sleep(2)
        print("Now choose!")
        print("A. 6349")
        print("B. 9463")
        print("C. 4936")
        print("")
        print("Type A, B or C")
        choose_door()
        
    elif chemical_answer.lower() == "b":
        print("")
        print("Go through door B")
        time.sleep(2)
        print("Here you find another plaque, this plaque reads:")
        print("You are trapped, you need to revise your shapes to escape. Start again!")
        time.sleep(2)
        print("You hear a hissing and start to feel dizzy, you wake up in the first room")
        print("")
        time.sleep(2)
        start_game()
    else:
        print("Type A or B ")
        chemical_question()



def choose_door():
    door_answer = input("")
    if door_answer.lower() == "a":
        print("Go through door A")
        time.sleep(2)
        print("Here you find another plaque, this plaque reads:")
        print("You are trapped, you need to pay more attention to the clues I give you. Start again!")
        time.sleep(2)
        print("You hear a hissing and start to feel dizzy, you wake up in the first room")
        print("")
        time.sleep(2)
        start_game()
    elif door_answer.lower() == "b":
        print("Go through door B")
        time.sleep(2)
        print("Here you find another plaque, this plaque reads:")
        print("You are trapped, you need to pay more attention to the clues I give you. Start again!")
        time.sleep(2)
        print("You hear a hissing and start to feel dizzy, you wake up in the first room")
        print("")
        time.sleep(2)
        start_game()
    elif door_answer.lower() == "c":
        print("Go through door C")
        time.sleep(2)
        print("A bright light shines in your eyes, you have escaped!")
        print("play again?")
        print("A. Yes")
        print("B. No")
        play_again = input("")
        if play_again.lower() == "a":
            start_game()
        elif play_again.lower() == "b":
            print("Its been fun " + player)
        else:
            print("Type A or B")
        
    else:
        print("Type A or B or C")




start_game()