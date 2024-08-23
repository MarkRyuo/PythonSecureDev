
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


#* Create number increamenting 

count = 0 

def increament() :
    global count 
    count += 1 
    print(f"After: {count}")


if __name__ == "__main__" :

    getAge()

    print(f"Before: {count}")
    print(f"Before: {count}")
    increament()