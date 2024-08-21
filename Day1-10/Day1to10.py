
# * Variables 

name = "Moda" # * String  
age = 21  # * Integer or Number
online = True # * Boolean 


getName = input("Enter your name: ") # * Input 
print(getName) #* Printing the console 


# * Control Flow with Function 

def GetAge() :

    getAge = input("Enter your age: ")

    if int(getAge) > 25 :
        print("Your Adult")
    elif int(getAge) >= 18 and int(getAge) <= 25: 
        print("Your Teenager")
    elif int(getAge) < 18 :
        print("Your Young your ban") 
        return False

if __name__ == "__main__" :
    if getName == "moda" or getName == "Moda" :
        GetAge()
    

    if getName : 
        print(f"Hi {getName} Welcome")