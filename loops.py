while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
iterationvalues = [2, 7, 13, 14, 28]
for value in iterationvalues:
    print(value)
print('done')    
count = 0
for iterationvalues in [2, 7, 13, 14, 28]:
    count = count + 1
print('count: ', count)    
total = 0
for iterationvalues in [2, 7, 13, 14, 28]:
    total = total + iterationvalues
print('total: ', total)    
average = total / 5
print(average)
