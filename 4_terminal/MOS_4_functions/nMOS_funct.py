from math import *
from sympy import *

#funct for creating steps in for loop
def drange(start, stop, step):
    while start < stop:
            yield start
            start += step



#funct to return the value of funct at a particuar value
def func(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0):	    
	try:
      	  p=0	 
	  return p=Vgb-Vfb-gm(sqrt(s0+Phi_t*e**((s0-2*Phi_F)/Phi_t)))-s0
 	 
    	except ZeroDivisionError:
          print("Error!!!!!!!!!!!", s0)
    	  return 0



#funct to find derivative at a particular value
def derivFunc( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0 ):
    #main function with variable t
    t= Symbol('t')    
    f=Vgb-Vfb-gm(sqrt(t+Phi_t*e**((t-2*Phi_F)/Phi_t)))-t
    deriv= Derivative(f, t)

    k= deriv.doit().subs({t:s0}) #this puts the value of t as Shi_s in the derivative of the main function
     
    if k==0:
	return 1
    else:
	return k




# Newton_Raphson to find the root of the function
def newtonRaphson( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0):

    err=1   	
    count=0
    # x(i+1) = x(i) - f(x) / f'(x)
    while abs(err) >= 0.001:
        count=count+1
	try:
      	    err = (func(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0))/(derivFunc(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0))
	    s0 = s0 - err
 	    #print("Shi_s is ",Shi_s)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", s0)


    #print("The value of the root is : ","%.4f"% Shi_s)
    #print("the no of iterations is ",count)  #no of iterations for each value of vgb
    return s0



def func2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL):	    
	try:
      	  p=0	 
	  return p=Vgb-Vfb-gm(sqrt(sL+Phi_t*e**((sL-2*Phi_F-Vds)/Phi_t)))-sl
 	 
    	except ZeroDivisionError:
          print("Error!!!!!!!!!!!", sL)
    	  return 0



#funct to find derivative at a particular value
def derivFunc2( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL ):
    #main function with variable t
    t= Symbol('t')    
    f=Vgb-Vfb-gm(sqrt(t+Phi_t*e**((t-2*Phi_F-Vds)/Phi_t)))-t
    deriv= Derivative(f, t)

    k= deriv.doit().subs({t:sL}) #this puts the value of t as Shi_s in the derivative of the main function
     
    if k==0:
	return 1
    else:
	return k




def newtonRaphson2( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL):

    err=1   	
    count=0
    # x(i+1) = x(i) - f(x) / f'(x)
    while abs(err) >= 0.001:
        count=count+1
	try:
      	    err = (func2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL))/(derivFunc2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL))
	    sL = sL - err
 	    #print("Shi_s is ",Shi_s)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", sL)


    #print("The value of the root is : ","%.4f"% Shi_s)
    #print("the no of iterations is ",count)  #no of iterations for each value of vgb
    return sL



def calculate_Id(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,x0):
	s0=x0
	sL=x0+Vds
	Phi_s0=newtonRaphson(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0)
	Phi_sL=newtonRaphson2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL)

	
	

