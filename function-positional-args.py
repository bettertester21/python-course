
def add_numbers(name,*args):
    print(args)
    print(type(args))
    total = 0
    for num in args:
        total = total + num
        
    print('Total is: ',total)        

# add_numbers('Anand',1,2,3,4,5,6,7,8,9)    

add_numbers('Anand')    

