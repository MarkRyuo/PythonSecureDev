from App import Character 

class GetCharacter(Character) :
    
    def __init__(self):
        super().__init__() 
    
    
    def CallName(self) :
        print('Hello') 

if __name__ == '__main__' :
    pass
else :
    print("Rendering Outside of Subclass....")
        

