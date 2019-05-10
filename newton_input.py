from math import *
from sympy import *

def func( x ): 
    return x*e**x - 2
  
def derivFunc( x ): 
    return e**x + x*e**x
  
# Function to find the root 
def newtonRaphson( t ):
    x= Symbol('x')
    f=func(t) 
    deriv=Derivative(func(x),x)
    h = func(t) / deriv.doit().subs({x:t}) 
    while abs(h) >= 0.01: 
        h = func(t)/ deriv.doit().subs({x:t})
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
      
    print("The value of the root is : ", 
                             "%.4f"% x) 
   
x0 = 5 # Initial val 
newtonRaphson(x0)
