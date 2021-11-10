def starts_with_vowel(word):
    if (word[0] == 'a' or 
        word[0] == 'e' or 
        word[0] == 'i' or 
        word[0] == 'o' or 
        word[0] == 'u'):
        return True
    return False

name = input('what is your name?\n')
print("hello " + name)
color = input('what color is your shirt?\n')
print("There was a spider. It was " + color)
number = input('type any number.\n')   
print("It had party hats that numbered " + number) 
print("Its name was " + name)  
celebrity = input('tell me the name of a celebrity\n')  
friendname = input('who is the last person you hugged?\n') 
print("the spider was friends with " + friendname)    
animal = input('what is the first animal you think of?\n')  
print("Yay! " + friendname) 
print("was a" + ("n " if starts_with_vowel(animal) else " ") + animal)
print("They decided to go to together to see " + celebrity) 
print("They went and had a great time being in love!!\n")

