
# * Variables 

name = "Moda" # * String -> str 
age = 21  # * Integer or Number -> int 
online = True # * Boolean -> bool


getName = input("Enter your name: ") # * Input 
print(getName) #* Printing the console 


# * Control Flow with Function 

def GetAge() :

    getAge = input("Enter your age: ")

    if int(getAge) > 25 : # ? If age is greater to 25 they Adult
        print("Your Adult")
    elif int(getAge) >= 18 and int(getAge) <= 25:  # ? If age is greater or equal to 18 and less than or equal 25, they Teenager
        print("Your Teenager")
    elif int(getAge) < 18 :
        print("Your Young your ban") # ? If age is less than to 18, they too young and they ban in the system 
        return False
    

# * specify the datatypes 
specifyname = str("Moda")
specifyage = int(21)
specifyonline = bool(True)


#* Checking Data types 
print(type(specifyname))

#* Python has many builtin method or function 

lowername = str("Moda")
print(lowername.upper())


if __name__ == "__main__" : # * This is 

    # * control flow 
    if getName == "moda" or getName == "Moda" :
        GetAge()
    else :
        print(f"Who are you? {getName}") 
        exit()
    
    

    if getName : 
        print(f"Hi {getName} Welcome")