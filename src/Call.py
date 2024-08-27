from App import Character 
from Data import data

#* Subclass 

class GetCharacter(Character) :
    
    def __init__(self):
        super().__init__() 
    
    
    def CallName(self) :
        
        for key, values in data.items() :
            print(f'{key}: {values}')
        

if __name__ == '__main__' :
    pass
else :
    print("Rendering Outside of Subclass....")
        

