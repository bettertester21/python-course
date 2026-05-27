
def print_details(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("Your age is: ",kwargs.get('age'))
 

print_details(name='Anand',age=29,address='123, BTM Layout,Bangalore-98')    

