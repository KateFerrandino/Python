def computepay(rate, hours):
    return rate * hours 

rate_in = int(input('how much per hour?\n'))
hours = int(input('how many hours?\n'))
total = computepay(rate_in, hours)
print(total)  
if hours > 40 :
    overtime = (hours - 40) * rate_in * .5
    print(overtime+total)
else :
    print(total) 
