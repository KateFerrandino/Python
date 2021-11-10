def count_function(word, target):
    count = 0
    for letter in word:
        if letter == target:
            count = count + 1
    print(count) 

word = (input('what word should we use?\n'))
letter = 'a' 
count_function(word, letter)
count_function(word, 'b')

