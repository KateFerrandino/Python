try :
    hours = int(input('enter hours'))
except :
    hours = int(input('I only understand numerals try again'))
try :
    rate = int(input('enter rate'))
except: 
    rate = int(input('I only understand numerals, enter rate'))
wages = hours * rate
if hours > 40 :
    overtime = (hours - 40) * rate * .5
    print(overtime+wages)
else :
    print(wages) 

