def Jake(string):
    upper=0
    lower=0
    for i in string:
        if i.isupper():
           upper+=1
        elif i.islower():
           lower+=1
        else:
           pass
    print("Count of Upper case charachters is : ",upper) 
    print("Count of Lower case charachters is : ",lower)   

Jake(input("Provide a string : "))