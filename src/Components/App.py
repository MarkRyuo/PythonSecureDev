from abc import ABC, abstractmethod
from Data import data 

#* Super Class 

class Character(ABC) :
    
    def __init__(self) -> None :
        pass
    
    def Charloop(self) :
        
        getName = str(input("Enter a name of Character: w"))
        
        for key, values in data.items() :
            if values["Uname"] == 
    
    @abstractmethod
    def CallName(self) :
            pass 
    
    @classmethod
    def CallAge(cls, ) -> str :
        
        return "I dont Know"