try:
    a = int(input('give me a number:\n'))
except:
    a = int(input('bad data, enter a number:\n'))    
try:    
    b = int(input('another number please:\n'))
except:
    b = int(input('bad data, enter a number:\n'))    
try:   
    c = int(input('drop a number on me:\n'))
except:
    c = int(input('bad data, enter a number:\n'))
try:    
    d = int(input("let's do this again:\n"))
except:
    d = int(input('bad data, enter a number:\n'))
try:    
    e = int(input('give me one last number, okay:\n'))
except:
    e = int(input('bad data, enter a number:\n'))   
print(a, b, c, d, e)
largest = None
for itervar in [a, b, c, d, e]:
    if largest is None or itervar > largest:
        largest = itervar
print('largest:', largest)        
smallest = None
for itervar in [a, b, c, d, e]:
    if smallest is None or itervar < smallest:
        smallest = itervar
print('smallest:', smallest)     