pali="race car"

def palindrome(pali):
    if pali=="":
        return ("empty string")
    elif pali!=pali[::-1]:
        return False
    else:
        return True
    
    
print(palindrome(pali))
    
    