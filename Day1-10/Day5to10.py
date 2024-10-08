
#* Loop in dict 
#* Methods to loop a dict:  Key(), values(), items() 
#* keys() -  gets you the keys in a dictionary
#* values() - gets you the values in a dictionary 
#* items() - gets you both the keys and values in a dictionary 


dict_of_name = {
    "name1" : "Riyuo",
    "name2" : "Niyari",
    "name3" : "Samantya",
    "name4" : "Jiyan"
}

def loopofname() :

    for values in dict_of_name.values() : #* Looping in values of dictionaries  
        print(values) 
    
    for key in dict_of_name.keys() : #* Looping in keys of dictionaries 
        print(key)
    
    for items in dict_of_name.items() : #* Looping in items of dictionaries 
        print(items)


#* Nested Loop 

Matrix = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]

colors = ["red", "blue", "green"] #* Outer Loop 
fruits = ["apple", "grape", "mango"] #* Inner Loop 

def Nestedloop() :

    #* Nested for loop 

    for row in Matrix : #* Outer loop iterates over each row in the matrix
        for column in row : #* Inner loop iterates over each column/element in the current row
            print(column)
    

    for color in colors : #* Inner Loop 
        for fruit in fruits : #* Outer Loop 
            print(f"{color}: {fruit}")


if __name__ == '__main__' :
    # loopofname()
    Nestedloop()
else :
    print("Error")
