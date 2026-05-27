
def order_pizza(name,address,**toppings):
    print("Order is for: ",name)
    print("Order shipping address is: ",address)
    price = 18.00
    for key,value in toppings.items():
        price = price + 2.00
    print(f"Total price is: {price}")    
    # return price

total_price = order_pizza(name='Anand',address='123, BTM Layout,Bangalore-98',jalapenos = True,extra_chese=True,ham = True)    

