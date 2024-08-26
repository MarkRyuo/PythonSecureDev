

#* Create a Secure Login 

#* Temporal Incident  


# todo create a data by name of characters in the Temporal Incident

data = {
    "Char1": {
        "username" : "Moda",
        "age" : 21,
        "alive" : False
    },

    "Char2" : {
        "username" : "Niyari",
        "age" : 19,
        "alive": True
    },
    
    "Char3" : {
        "username" : "Riyuo",
        "age" : 19,
        "alive" : False
    },

    "Char4" : {
        "username" : "Samantya",
        "age" : 19,
        "alive" : True
    },

    "Char5" : {
        "username" : "Jiyan",
        "age" : 19,
        "alive" : True
    },
    

}

#* Check if the character in the data is alive, Input the name 

def check_alive() :

    charname = input("Enter the name: ") 

    for key, value in data.items() :
        print(f"{key}, {value}")
        if value["username"] == charname :

            if value["alive"] :
                print(f"{charname} is alive")
            else :
                print(f"{charname} is unknown")
            
        else :
            print(f"{charname} is not found")



if __name__ == '__main__' :
    check_alive()