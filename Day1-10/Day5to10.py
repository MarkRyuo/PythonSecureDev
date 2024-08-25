
#* Loop in dict 
#* Methods to loop a dict:  Key(), values(), items() 
#* Key() -  gets you the keys in a dictionary
#* values() - gets you the values in a dictionary 
#* items() - gets you both the keys and values in a dictionary 

from optparse import Values


dict_of_name = {
    "name1" : "Riyuo",
    "name2" : "Niyari",
    "name3" : "Samantya",
    "name4" : "Jiyan"
}

def loopofname() :

    for values in dict_of_name.values() :
        print(values)
    


if __name__ == '__main__' :
    loopofname()
else :
    print("Error")
