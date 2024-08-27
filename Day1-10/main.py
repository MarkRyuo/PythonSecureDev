from curses.ascii import isdigit
from requests import get
from Data import data

#* Create Character Checker
#* In the Temporal Incident  



#* Check if the character in the data is alive, by inputting the name.

def check_alive() -> str  :
    
    charname = str(input("Enter the name: ")) 

    for key, value in data.items() :
        # print(f"{key}, {value}")
        if value["username"] == charname :

            if value["alive"] :
                print(f"{charname} is alive")
            else :
                print(f"{charname} is unknown")
    
    return charname 


#* Create a CRUD operation 

def get_username() -> str :

    getName = input("Enter your username: ") 

    data = list(()) #* Create a empty list

    while True : 

        if getName.isdigit() : 
            return "Hello"
        else : 
            return f"Enter a name: "




if __name__ == '__main__' :
    # check_alive()
    print(get_username())