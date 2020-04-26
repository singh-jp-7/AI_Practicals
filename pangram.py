def pangram():   
    
    alphabet = "qwertyuioplkjhgfdsazxcvbnm"
    string1 = input("Enter the string to check :")
    ispangram = True
    for s in alphabet:
        if s in string1.lower():
            continue
        else:
            ispangram = False
            break
    if(ispangram):
        print("The string is a pangram !")
    else:
        print("No, the sring is not pangram !")

pangram()
