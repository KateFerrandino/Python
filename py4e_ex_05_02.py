largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        trynum = int(num)
        if largest is None or trynum > largest :
            largest = trynum 
        if smallest is None or trynum < smallest :
            smallest = trynum 
    except :
        print('Invalid input')    
     


print("Maximum is", largest)
print("Minimum is", smallest)     