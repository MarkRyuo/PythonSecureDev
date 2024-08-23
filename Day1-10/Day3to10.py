
# * Variable that assign into multiple values 

name, age , active = "moda", 21, True 

print(name)
print(age)
print(active)

# * Global variable 

# * What is age before? and what is the age after

def getAge() :

    global age 
    age = 30 

    print(age)