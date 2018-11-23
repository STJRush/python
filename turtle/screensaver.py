from turtle import *
import random
color('green', 'blue')
#begin_fill()
bgcolor("black")


number1=random.random()  
number1=100*number1     
print(int(number1))

number2=random.random()  
number2=100*number2   
print(int(number2))

while True:

    for x in range(80):
        
        

        speed(x)

        forward(200)
        left(100)
        
        forward(100)
        left(50)
        
        forward(50)
        left(25)
        
    

    clear()
    number1=random.random()  
    number1=100*number1     
    print(int(number1))

    number2=random.random()  
    number2=100*number2   
    print(int(number2))

    goto(number1, number2)
    


