import math

print('solve ax^2 + bx + c = 0 here')

a = int(input('write a: '))

b = int(input('write b: '))

c = int(input('write c: '))

if (a == 0):
    print('you shuldnt make a = 0')
    exit()

print('the equation is' , a ,'x^2 + ' , b , 'x + ' , c , ' = 0')

delta = b ** 2 - (4 * a * c)

if(delta < 0):
    print('delta is equal: ' , delta )
    print('there is no solution')
    print('this simple program is owned by Akbar')

    exit()

    
sqrt = math.sqrt(delta)

X1 = (-1 * b + sqrt ) / ( 2 * a ) 
X2 = (-1 * b - sqrt ) / ( 2 * a )
print('delta is equal: ' , delta )



if (delta > 0):
    print('there is 2 solution and they are')
    
    print('1-' , X1)
    print('2-' , X2)
    


elif (delta == 0):
        print('there is 1 solution and it is')
        print(X1)

            
print('this simple program is owned by Akbar')

exit()
