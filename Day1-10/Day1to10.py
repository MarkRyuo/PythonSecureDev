
# * Variables 

name = "Moda" # * String  
age = 21  # * Integer or Number
online = True # * Boolean 


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
    

if __name__ == "__main__" :

    # * control flow 
    if getName == "moda" or getName == "Moda" :
        GetAge()
    else :
        print(f"Who are you? {getName}") 
        exit()
    
    

    if getName : 
        print(f"Hi {getName} Welcome")