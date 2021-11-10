import random
for i in range (10):
    x = random.random()
    print(x)
for i in range (10):
    y = random.randint(5, 10)
    print(y)   
t = ["100z", "101y", "102x"]    
z = random.choice(t)
print(z)
def print_lyrics():
    print('goodbye yellowbrick road')
    print("I'm going back to my cloud")
def addtwo(a, b):
    added = a + b
    return added    
x = addtwo(3, 5)
print(x)    

print_lyrics()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()      