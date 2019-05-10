from math import *
from sympy import *
global Y,deriv,dydx,count
count=0
h=5
global Vgb,Vfb,q,Es,Cox,Po,No,St,NA,ND

# Vgb= int(input("Enter the value of Vgb "))
# Vfb= int(input("Enter the value of Vfb "))
# q= int(input("Enter the value of q "))
# Es= int(input("Enter the value of Es "))
# Cox= int(input("Enter the value of Cox "))
# Po= int(input("Enter the value of Po "))
# No= int(input("Enter the value of No "))
# St= int(input("Enter the value of St "))
# NA= int(input("Enter the value of NA "))
# ND= int(input("Enter the value of ND "))
x0 = float(input("enter the initial value : "))
Vgb=1
Vfb=-1
NA=10**24
ND=10**15
St=0.026
q=1.6*10**(-19)
Es=1.05*10**(-10)
Cox=1.726*10**(-2)
No=10**15
Po=10**24

def func( Y ): 
    global Vgb,Vfb,q,Es,Cox,Po,No,St,NA,ND
    #print("I am inside func  " , Y)
    try: 
      	  p=Vfb + Y + (sqrt(2*q*Es)/Cox) *(sqrt( Po*St*( e**(-Y/St )-1) +( NA-ND  )*Y + No*St*( e**(Y/St )-1) )  ) -Vgb
      	  return p
    except ZeroDivisionError:
          print("Error!!!!!!!!!!!", Y)
    	  return 0    

def derivFunc( Y ): 
    
    k= deriv.doit().subs({t:Y})
    print("I am inside deriv func  ", k)
    if k==0:
	return 1
    else:  
	return k

  
# Function to find the root 
def newtonRaphson( Y ): 
    global count
    global Vgb,Vfb,q,Es,Cox,Po,No,St,NA,ND,h
    if derivFunc(Y)!=0:
    	h = (func(Y) )/ (derivFunc(Y)) 
    	print("h is ",h)

    while abs(h) >= 0.05: 
        count=count+1
	try:
      	    h = func(Y)/derivFunc(Y)
            print("the value of deriv is ",derivFunc(Y))
	    print("the value of funct is ",func(Y))
	    Y = Y - h    
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", Y)
        # x(i+1) = x(i) - f(x) / f'(x) 
         
      
    print("The value of the root is : ", 
                             "%.4f"% Y)
    print("the no of iterations is ",count) 
   


t= Symbol('t')    
f=Vfb + t + (sqrt(2*q*Es)/Cox) *(sqrt( Po*St*( e**(-t/St )-1) +( NA-ND  )*t + No*St*( e**(t/St )-1) )  ) -Vgb
deriv= Derivative(f, t)


#print(deriv.doit())
dydx=deriv.doit()
#deriv.doit()
newtonRaphson(x0) 
