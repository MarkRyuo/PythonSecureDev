

# * Loops - For loop, While loop 
# * Basic data structure: List, tuple, dict, set 


# Todo Create a list of names and loop it 

list_Name = [
    "Riyuo",
    "Niyari",
    "Sopheya",
    "Jian"
]

# Todo Try to display list of name 

def Getname() :

    for i in list_Name :
        print(i)

    for x in range(1, 5) :
        print(x)

    for j in range(1, 5) : 
        return list_Name[j]




if __name__ == '__main__' :

    Getname()