from abc import ABC, abstractmethod
from Data import data 

#* Super Class 

class Character(ABC) :
    
    def __init__(self) -> None :
        pass
    
    @abstractmethod
    def CallName(self) :
           