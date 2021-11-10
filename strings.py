fruit = 'banana'
index = 0
while index > len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

a = 'monty python'
print (a[0:5])  
print(fruit[:3])  
print (fruit[4:])

greeting = 'hello world'
greeting2 = 'J' + greeting[1:]
print(greeting2)

word = 'waterweevilw'
count = 0
for letter in word:
        if letter == 'w':
            count = count + 1
print(count)            