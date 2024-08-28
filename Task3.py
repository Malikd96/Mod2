#Default Path
#If the user makes an invalid choice at any point, incorporate a pass statement to handle it. 
# HINT: How can an else statement be of use here?


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass

elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You're now lost!")
    else:
        pass
