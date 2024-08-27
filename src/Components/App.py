from abc import ABC, abstractmethod
from Data import data 

#* Super Class 

class Character(ABC) :
    
    def __init__(self) -> None :
        pass
    
    def Charloop(self) :
        
    
    @abstractmethod
    def CallName(self) :
            pass 
    
    @classmethod
    def CallAge(cls, ) -> str :
        
        return 