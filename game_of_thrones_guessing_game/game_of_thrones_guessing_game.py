import random

def quiz_4():
    #Selects a random kingdom from a predefined tuple consisting of  "The Vale", "The Riverlands", "The Stormlands", "The North", "The Iron Islands", "Westeroos", "Dorne".
    #The user will be informed how many letters are in the kingdom.
    #The user gets 5 guesses to determine if a letter is in the kingdom.
    #The computer tells the user whether their guesses were correct or incorrect.
    #The user must then guess the kingdom. 
    kingdoms = ("The Vale", "The Riverlands", "The Stormlands", "The North", "The Iron Islands", "Westeroos", "Dorne")
    random_kingdom = kingdoms[random.randint(0, 6)]
    chances = 5

    print(F"The length of your kingdom is: {len(random_kingdom)}")

    while chances > 0:        
        letter_guess = input("Enter a letter that you believe your kingdom contains: \n")
        if letter_guess.lower() in random_kingdom.lower():
            print("""                                               ,d     
                                               88     
 ,adPPYb,d8 8b,dPPYba,  ,adPPYba, ,adPPYYba, MM88MMM  
a8"    `Y88 88P'   "Y8 a8P_____88 ""     `Y8   88     
8b       88 88         8PP""""""" ,adPPPPP88   88     
"8a,   ,d88 88         "8b,   ,aa 88,    ,88   88,    
 `"YbbdP"Y8 88          `"Ybbd8"' `"8bbdP"Y8   "Y888  
 aa,    ,88                                           
  "Y8bbdP""""")
            print("Awesome!! \nThat letter is in your kingdom!")
            chances -=1
        else:
            print("""8b,dPPYba,   ,adPPYba,  8b,dPPYba,   ,adPPYba,  
88P'   `"8a a8"     "8a 88P'    "8a a8P_____88  
88       88 8b       d8 88       d8 8PP"""""""  
88       88 "8a,   ,a8" 88b,   ,a8" "8b,   ,aa  
88       88  `"YbbdP"'  88`YbbdP"'   `"Ybbd8"'  
                        88                      
                        88""")
            print("Sorry, that letter isn't in your kingdom. \nDon't give up it's not over yet!!")
            chances -=1
    final_answer = input("What is your final answer? \n")

    if final_answer.title() == random_kingdom:
        print("""                                                                     ,d     
                                                                     88     
 ,adPPYba,  ,adPPYba,  8b,dPPYba, 8b,dPPYba,  ,adPPYba,  ,adPPYba, MM88MMM  
a8"     "" a8"     "8a 88P'   "Y8 88P'   "Y8 a8P_____88 a8"     ""   88     
8b         8b       d8 88         88         8PP""""""" 8b           88     
"8a,   ,aa "8a,   ,a8" 88         88         "8b,   ,aa "8a,   ,aa   88,    
 `"Ybbd8"'  `"YbbdP"'  88         88          `"Ybbd8"'  `"Ybbd8"'   "Y888""")
    else:
        print("""                                                                                                          
""                                                                                  ,d     
                                                                                    88     
88 8b,dPPYba,   ,adPPYba,  ,adPPYba,  8b,dPPYba, 8b,dPPYba,  ,adPPYba,  ,adPPYba, MM88MMM  
88 88P'   `"8a a8"     "" a8"     "8a 88P'   "Y8 88P'   "Y8 a8P_____88 a8"     ""   88     
88 88       88 8b         8b       d8 88         88         8PP""""""" 8b           88     
88 88       88 "8a,   ,aa "8a,   ,a8" 88         88         "8b,   ,aa "8a,   ,aa   88,    
88 88       88  `"Ybbd8"'  `"YbbdP"'  88         88          `"Ybbd8"'  `"Ybbd8"'   "Y888""")
        print(F"The correct kingdom was: {random_kingdom}")
  
    retry = input("Would you like to play again? Y/N \n")
    if retry.upper() == "N":
        print("Thanks for playing!! \nSee you next time!")
    elif retry.upper() == "Y":
        print("There's a GTA reference I can make here but I digress.")
        quiz_4()   
    else:
        print("Invalid input!!")
    return ""


name = input("Please enter your name: ")
print(F"Hello {name.title()}!! \nWelcome to the G.O.T. guessing game!")
print("""
 __     __     __     __   __     ______   ______     ______        __     ______        __  __     ______     ______     ______    
/\ \  _ \ \   /\ \   /\ "-.\ \   /\__  _\ /\  ___\   /\  == \      /\ \   /\  ___\      /\ \_\ \   /\  ___\   /\  == \   /\  ___\   
\ \ \/ ".\ \  \ \ \  \ \ \-.  \  \/_/\ \/ \ \  __\   \ \  __<      \ \ \  \ \___  \     \ \  __ \  \ \  __\   \ \  __<   \ \  __\   
 \ \__/".~\_\  \ \_\  \ \_\\"\_\    \ \_\  \ \_____\  \ \_\ \_\     \ \_\  \/\_____\     \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\ 
  \/_/   \/_/   \/_/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/      \/_/   \/_____/      \/_/\/_/   \/_____/   \/_/ /_/   \/_____/ 
                                                                                                                                    
""")
print(quiz_4())
