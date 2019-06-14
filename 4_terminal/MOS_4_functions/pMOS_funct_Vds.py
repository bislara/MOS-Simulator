from math import *
from sympy import *

#funct for creating steps in for loop
def drange(start, stop, step):
    while start < stop:
            yield start
            start += step



#funct to return the value of funct at a particuar value
def func(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0,Po,No,NA,ND):	    
	try:
      	  p=Vgs-Vfb+gm*(sqrt( Po*Phi_t*( e**(-s0/Phi_t )-1) +( NA-ND  )*s0 + No*Phi_t*( e**(s0/Phi_t )-1) ))-s0
	 
	  return p 	 
    	except ZeroDivisionError:
          print("Error!!!!!!!!!!!", s0)
    	  return 0


#funct to find derivative at a particular value
def derivFunc( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0,Po,No,NA,ND ):
    #main function with variable t
    t= Symbol('t')    
    f=Vgs-Vfb+gm*(sqrt( Po*Phi_t*( e**(-t/Phi_t )-1) +( NA-ND  )*t + No*Phi_t*( e**(t/Phi_t )-1) ))-t
    deriv= Derivative(f, t)

    k= deriv.doit().subs({t:s0}) #this puts the value of t as Shi_s in the derivative of the main function
     
    if k==0:
	return 1
    else:
	return k




# Newton_Raphson to find the root of the function
def newtonRaphson( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0,Po,No,NA,ND):

    err=1   	
    count=0
    print("s0 init is ",s0)
    # x(i+1) = x(i) - f(x) / f'(x)
    while abs(err) >= 0.001:
        count=count+1
	try:
      	    err = (func(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0,Po,No,NA,ND))/(derivFunc(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0,Po,No,NA,ND))
	    s0 = s0 - err
 	    
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", s0)


    print("The value of the root is : ","%.4f"% s0)
    print("the no of iterations is ",count)  #no of iterations for each value of Vgs
    return abs(s0)



def func2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL,Po,No,NA,ND):	    
	try:
      	  p=Vgs-Vfb+gm*(sqrt( Po*e**(-Vds/Phi_t)*Phi_t*( e**(-sL/Phi_t )-1) +( NA-ND  )*sL + No*Phi_t*( e**(sL/Phi_t )-1) ))-sL
 	 	 
	  return p

    	except ZeroDivisionError:
          print("Error!!!!!!!!!!!", sL)
    	  return 0



#funct to find derivative at a particular value
def derivFunc2( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL,Po,No,NA,ND ):
    #main function with variable t
    t= Symbol('t')    
    f=Vgs-Vfb+gm*(sqrt( Po*e**(-Vds/Phi_t)*Phi_t*( e**(-t/Phi_t )-1) +( NA-ND  )*t + No*Phi_t*( e**(t/Phi_t )-1) ))-t
    deriv= Derivative(f, t)

    k= deriv.doit().subs({t:sL}) #this puts the value of t as Shi_s in the derivative of the main function
     
    if k==0:
	return 1
    else:
	return k




def newtonRaphson2( w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL,Po,No,NA,ND):

    err=1   	
    count=0
    print("sL init is ",sL)
    # x(i+1) = x(i) - f(x) / f'(x)
    while abs(err) >= 0.001:
        count=count+1
	try:
      	    err = (func2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL,Po,No,NA,ND))/(derivFunc2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL,Po,No,NA,ND))
	    sL = sL - err
 	    
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", sL)

    
    print("The value of the root is : ","%.4f"% sL)
    print("the no of iterations is ",count)  #no of iterations for each value of Vgs
    return abs(sL)



def calculate_Id(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,x0,Po,No,NA,ND):
	
	f=-(-gm/2 + sqrt((gm)**2/4) + Vgs - Vfb )**2 
	n0=-x0
	nL=-x0-Vds
	s0=max(n0,f)
	print("f n N0 is ",f,n0,s0)
	
	sL=max(f,nL)
	print("f n NL is ",f,nL,sL)
	Shi_s0=newtonRaphson(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,s0,Po,No,NA,ND)
	Shi_sL=newtonRaphson2(w,l,mu,Vgs,Vfb,Vds,Cox,gm,Phi_t,Phi_F,sL,Po,No,NA,ND)
	
	Id1=(w/l)*mu*Cox*((Vgs-Vfb)*(Shi_sL-Shi_s0)-0.5*(Shi_sL**2-Shi_sL**2)-(2.0/3)*gm*(Shi_sL**(3.0/2)-Shi_s0**(3.0/2)))
	Id2=(w/l)*mu*Cox*(Phi_t*(Shi_sL-Shi_s0)+Phi_t*gm*(Shi_sL**0.5-Shi_s0**0.5))
	Id=Id1+Id2
	
	return abs(Id*1000)
	

