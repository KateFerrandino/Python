def grades ():
    try : 
        score = float(input("What is your score?\n"))
    except :
        score = float(input("Bad score. What is your score?\n"))
    if score > 1 :
        print ('bad score\n')    
    elif score >= 0.9 :
        print ('A')    
    elif score >= 0.8 :
        print ('B')   
    elif score >= 0.7 :
        print ('C')   
    elif score >= 0.6 :
        print ('D')    
    elif score < 0.6 :
        print ('F')
    else :
        print ('bad score')  
grades()                