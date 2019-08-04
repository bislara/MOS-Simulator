from math import *
from sympy import *
global t,deriv,dydx,count
count=0

def func( x ): 
    return x*log(x)/log(10) - 1.2
  
def derivFunc( x ): 
    return deriv.doit().subs({t:x}) 
  
# Function to find the root 
def newtonRaphson( x ): 
    global count
    h = func(x) / derivFunc(x) 

    while abs(h) >= 0.01: 
        count=count+1
	try:
      	    h = func(x)/derivFunc(x)    
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
      
    print("The value of the root is : ", 
                             "%.4f"% x)
    print("the no of iterations is ",count) 
   


x0 = input("enter the initial value : ") # Initial val 
x0 = int(x0)
#x0 =5
t= Symbol('t')    
f=t*log(t)/log(10) - 1.2
deriv= Derivative(f, t)
#print(deriv.doit())
dydx=deriv.doit()
#deriv.doit()
newtonRaphson(x0) 
