from abc import ABC, abstractmethod
from Data import data 

#* Super Class 

class Character(ABC) :
    
    def __init__(self) -> None :
        pass
    
    def Charloop(self) :
        
        getName = str(input("Enter a name of Character: "))
        
        for key, values in data.items() :
            if values["Uname"] == getName :
                return "Name is already in the Data!"
            else : 
                return "Not Valid"
    
    @abstractmethod
    def CallName() :
            pass 
    
    @classmethod
    def CallAge(cls, ) -> str :
        
        return "I dont Know"

if __name__ == '__main__' :
    pass
else : 
    print("Rendering Outside of Superclass....")