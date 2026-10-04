import sys
room_maps = {
    "Main Lab":{
        "description":"You are in the main lab. There appears to have been a struggle near the desk. The air smells faintly of chemicals. Dr. Orcho's desk is cordoned off. A broken flask sits on the floor.",
        "clue":"broken flask",
        "suspect": None,
         "connected_rooms":["Greenhouse","Server Room","Rival's Office"]
    },
    "Greenhouse":{
        "description":"Humid and filled with fluorescent toxic algae samples and tanks of strange glowing liquid. Emma is here adjusting the lights and observing the samples.",
        "clue":"Muddy footprint",
        "suspect":"Emma",
        "connected_rooms":["Main Lab","Server Room"]
    },
    "Server Room":{
        "description":"A humming computer stands alone in the room. The main drive slot where the formula back logs was stored is empty and flashing a red warning light.",
        "clue":"access card log",
        "suspect":None,
        "connected_rooms":["Main Lab","Greenhouse"]
    },
    "Dr. Serpanise's Office":{
        "description":"A messy office piled high with books and papers. There are paper clips scattered around the room, Dr. Serpanise is behind the pile frantically typing at his desk.",
        "clue":"hard drive",
        "suspect":"Dr. Serpanise",
        "connected_rooms":["Main Lab"]
    }
}

#solution dictionary
crime_solution = {
    "killer": "Dr. Serpanise",
    "weapon": "poisoned algae",
    "motive": "stolen formula"
}


#empty inventory list
inventory = []
detective_name = []


#accusation function
def accusation():
    print("\n======================================================================")
    print("                         ACCUSATION PROCESS                             ")
    print("========================================================================")
    print("You are calling the police. Your answer must be precise...")
    print(f"Your collected clues so far: {inventory}\n")

    guess_killer = input("Who killed Dr. Orcho? (Emma, Dr. Serpanise, Someone else...): ").lower().strip()
    guess_weapon = input("What was the murder weapon/method? (stab, poisoned algae, physical blow): ").lower().strip()
    guess_motive = input("What was the motive? (stolen formula, personal grudge, accident): ").lower().strip()


    if (guess_killer.lower() == crime_solution["killer"].lower()
    and guess_weapon.lower() == crime_solution["weapon"].lower() 
    and guess_motive.lower() == crime_solution["motive"].lower()):
        print(" ")
        print(f"Congratulations Detective {detective_name[0]}!")
        print(f"Your have caught {crime_solution['killer']} and confronted him with the evidence!")
        print("Justice has been served. You have successfully solved the mystery...")
        print("\n===============================================================")
        print(f"You were able to solve the mystery Detective {detective_name[0]}....")
        print("You have proven yourself to be a great detective....")
        print("Until the next mystery....")
        print("We will be in touch Detective...")
        print("=================================================================")
        print("Game Over. Thanks for playing")
        return "GAME OVER"
    else:
        print(" ")
        print("Your deductions were incorrect. The killer realized you were on to them and destroyed the evidence...")
        print("Justice has not been served....")
        print("Try playing again and analysing the clues more carefully...")
        print("\n=========================================================")
        print(f"You were not able to solve the mystery {detective_name[0]}.....")
        print("Game Over. Thanks for playing")
        print("===========================================================")
        return "GAME OVER"

#investigate function
def investigate(current_room):
    clue = room_maps[current_room]["clue"]
    if clue:
        if clue not in inventory:
            print(f"Congrats! You have found a clue: '{clue}'")
            inventory.append(clue)
        else:
            print(f"You have already found the '{clue}' in this room.")
    else:
        print("There are no clue's left to find here...")
    print(f"Current clues found: {inventory}")



#interview suspect function
def interview_suspect(current_room):
    suspect = room_maps[current_room]["suspect"]

    if suspect is None:
        print("\nYou look around.... There is no one in this room to interview.")
        return
    
    print(f"\nYou approach {suspect} to ask some questions....")

    if suspect == "Emma":
        print("\nEmma looks up nervously: 'I was in the Greenhouse all night monitoring our algae samples. I didn't see anyone enter the Main Lab. \nNext thing I know someone found Dr. Orcho dead. I don't even know what to say.'")
        print("The tone of Emma's voice while she says her last words sounds off...")
        print("You raise your eyebrow...")
        if "Muddy footprint" in inventory:
            print("[Confront]... You point to the wet ground.")
            print("You: 'Emma there is a muddy boot footprint right outside Dr. Orcho's lab door that matchs your lab boots.'")
            print("Emma gasps: 'Fine! I went to drop off a sample at midnight, but the door was locked. I heard arguing inside... it sounded like Dr. Serpanise!'")
    elif suspect == "Dr. Serpanise":
        print("\nDr. Serpanise slams his laptop shut: 'I am incredibly busy rewriting my research grants. My funding was cut, and I don't have time for your silly questions.'")
        if "access card log" in inventory:
            print("[Confront]...You show him your digital terminal screen.")
            print("You: 'The server log shows your personal access card unbolted the server room door at 1:45 AM.'")
            print("Dr. Serpanise turns pale: 'That's impossible! Someone must have stolen my card from my desk while I was... taking a walk.'")
            print("....You see a glowing spot of something on the corner of his desk...")
    print("==============================================================================================================================")



#main display menu
def rooms_menu_mainlab():
    print("\n--------Select Which Room to Go To--------")
    print("G - Greenhouse")
    print("S - Server room")
    print("R - Dr. Serpanise's Office")
    print("B - Back to Main menu")


#greenhouse menu
def rooms_menu_greenhouse():
    print("\n--------Select Which Room to Go To--------")
    print("M - Main Lab")
    print("S - Server Room")
    print("B - Back to Main menu")


#server room menu
def rooms_menu_serverroom():
    print("\n--------Select Which Room to Go To--------")
    print("M - Main Lab")
    print("G - Greenhouse")
    print("B - Back to Main menu")


#rival's office menu
def rooms_menu_rivaloffice():
    print("\n--------Select Which Room to Go To--------")
    print("M - Main Lab")
    print("B - Back to Main menu")


#main in room action menu
def in_rooms_menu():
    print("\n------Choose from 1 - 5--------")
    print("1 - Investigate (Search for clues)")
    print("2 - Change room")
    print("3 - Interview (if present)")
    print("4 - Accuse Suspect")
    print("5 - Back to Main menu")




def mainlab():
    print(" ")
    current_room = "Main Lab"
    print(f"Welcome to the {current_room}")
    print(" ")
    print(room_maps[current_room]["description"])
    print(" ")

    while True:
        in_rooms_menu()
        choice = input("Enter your next line of Action: ").strip()
        if choice == "1":
            investigate(current_room)
        elif choice == "2":
            rooms_menu_mainlab()
            user_choice = input("Enter the room you want to enter: ").upper().strip()
            if user_choice == "G":
                result = greenhouse()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "S":
                result = serverroom()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "R":
                result = serpanise_office()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "B":
                confirm = input("Are you sure you want to go back to main menu? (yes/no): ").lower()
                if confirm == "yes":
                    print("Redirecting...\nRedirected")
                    return
            else:
                print("Invalid choice. Please choose again")
        elif choice == "3":
            interview_suspect(current_room)
        elif choice == "4":
            if len(inventory) < 2:
                print("Warning: You do not have enough clues to make an accurate accusation!")
                confirmation = input("Do you still want to make an accusation? (yes/no): ").lower()
                if confirmation != "yes":
                    continue

            result = accusation()
            if result == "GAME OVER":
                sys.exit()
        elif choice == "5":
            return main()




def greenhouse():
    print(" ")
    current_room = "Greenhouse"
    print(f"Welcome to the {current_room}")
    print(" ")
    print(room_maps[current_room]["description"])
    print(" ")

    while True:
        in_rooms_menu()
        choice = input("Enter your next line of Action: ").strip()
        if choice == "1":
            investigate(current_room)
        elif choice == "2":
            rooms_menu_greenhouse()
            user_choice = input("Enter the room you want to enter: ").upper().strip()
            if user_choice == "M":
                result = mainlab()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "S":
                result = serverroom()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "B":
                confirm = input("Are you sure you want to go back to main menu? (yes/no): ").lower()
                if confirm == "yes":
                    print("Redirecting...\nRedirected")
                    return main()
            else:
                print("Invalid choice. Please choose again")
        elif choice == "3":
            interview_suspect(current_room)
        elif choice == "4":
            if len(inventory) < 2:
                print("Warning: You do not have enough clues to make an accurate accusation!")
                confirmation = input("Do you still want to make an accusation? (yes/no): ").lower()
                if confirmation != "yes":
                    continue

            result = accusation()
            if result == "GAME OVER":
                sys.exit()
        elif choice == "5":
                return main()




def serverroom():
    print(" ")
    current_room = "Server Room"
    print(f"Welcome to the {current_room}")
    print(" ")
    print(room_maps[current_room]["description"])
    print(" ")

    while True:
        in_rooms_menu()
        choice = input("Enter your next line of Action: ").strip()
        if choice == "1":
            investigate(current_room)
        elif choice == "2":
            rooms_menu_serverroom()
            user_choice = input("Enter the room you want to enter: ").upper().strip()
            if user_choice == "M":
                result = mainlab()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "G":
                result = greenhouse()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "B":
                confirm = input("Are you sure you want to go back to main menu? (yes/no): ").lower()
                if confirm == "yes":
                    print("Redirecting...\nRedirected")
                    return
                else:
                    print("Invalid choice. Please choose again")
        elif choice == "3":
            interview_suspect(current_room)
        elif choice == "4":
            if len(inventory) < 2:
                print("Warning: You do not have enough clues to make an accurate accusation!")
                confirmation = input("Do you still want to make an accusation? (yes/no): ").lower()
                if confirmation != "yes":
                    continue

            result = accusation()
            if result == "GAME OVER":
                sys.exit()
        elif choice == "5":
            return main()



def serpanise_office():
    print(" ")
    current_room = "Dr. Serpanise's Office"
    print(f"Welcome to {current_room}")
    print(" ")
    print(room_maps[current_room]["description"])
    print(" ")

    while True:
        in_rooms_menu()
        choice = input("Enter your next line of Action: ").strip()
        if choice == "1":
            investigate(current_room)
        elif choice == "2":
            rooms_menu_rivaloffice()
            user_choice = input("Enter the room you want to enter: ").upper().strip()
            if user_choice == "M":
                result = mainlab()
                if result == "GAME OVER":
                    return "GAME OVER"
                return
            elif user_choice == "B":
                confirm = input("Are you sure you want to go back to main menu? (yes/no): ").lower()
                if confirm == "yes":
                    print("Redirecting...\nRedirected")
                    return
                else:
                    print("Invalid choice. Please choose again")
        elif choice == "3":
            interview_suspect(current_room)
        elif choice == "4":
            if len(inventory) < 2:
                print("Warning: You do not have enough clues to make an accurate accusation!")
                confirmation = input("Do you still want to make an accusation? (yes/no): ").lower()
                if confirmation != "yes":
                    continue

            result = accusation()
            if result == "GAME OVER":
                sys.exit()

        elif choice == "5":
            return main()



def main_menu():
    print("\n==========Detective's Main Menu==========")
    print("M - Goes to Main Lab")
    print("G - Goes to Greenhouse")
    print("S - Goes to Server Room")
    print("R - Goes to Dr. Serpanise's Office")
    print("Q - Quits the game")
    print("===========================================")



def main():
    print("\nYou are playing ....")
    print(" ")
    print("================================================================================")
    print("                        The Tragic Case of Dr. Orcho                            ")
    print("================================================================================")
    print(" ")
    print("2:00 AM Dr. Orcho is found dead in his lab....")
    print("Next to him is a broken flask of what appears to be glowing algae...")
    print("The formula for his revolutionary fluorescent toxic algae is gone... the back log's have disappeared...")
    print("The laboratory is under police surveillance now....")
    print("It is currently 2:50 AM....")
    print("Your Objectives are as follows: \nFind the killer, the weapon and the motive before they destroy the evidence and escape...")

    user_name = input("What is your name detective? ").strip()
    

    if user_name not in detective_name:
        detective_name.append(user_name)
        print("Your name has been saved in the database, detective. Please proceed...")
    else:
        print("Your name has already been saved in the database, detective....")
    print(" ")

    while True:
        main_menu()

        user_choice = input(f"Select what to do next Detective {detective_name[0]}: ").upper()

        if user_choice == "M":
            result = mainlab()
            if result == "GAME OVER":
                sys.exit()
        elif user_choice == "G":
            result = greenhouse()
            if result == "GAME OVER":
                sys.exit()
        elif user_choice == "S":
            result = serverroom()
            if result == "GAME OVER":
                sys.exit()
        elif user_choice == "R":
            result = serpanise_office()
            if result == "GAME OVER":
                sys.exit()
        elif user_choice == "Q":
            confirm = input("Are you sure you want to exit the game? (yes/no): ").lower()
            if confirm == "yes":
                print("Thank you for playing...")
                print("Exiting game...")
                break
        else:
            print("Invalid choice. Please choose again")

        print("")

if __name__ == "__main__":
    main()