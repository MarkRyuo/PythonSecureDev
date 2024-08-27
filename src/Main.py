from Call import GetCharacter 



if __name__ == '__main__' :
    char = GetCharacter()
    print(char.Charloop())
    
    askQ1 = str(input("Do you want to display the data? (Y/n): "))
    
    if askQ1 == "Y" and askQ1 == "y" :
        char.CallName()
    else :
        print("Thank You for participating")

