name = 'Balaji'

def firstFunction(name):
    print("Inside first function",name)

    def secondFunction(name):
        print("Inside second function",name)
        
    secondFunction(name)    

firstFunction("Chandra")        
print("name: ",name)