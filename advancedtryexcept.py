favnum = None
while not favnum:
    try:
        favnum = int(input('what is your fave number?'))
    except:
        print('i can only understand digits')

print('of gold thou hast gained ' + str(favnum)) 