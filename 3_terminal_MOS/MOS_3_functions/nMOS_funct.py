from math import *
from sympy import *


#funct for creating steps in for loop
def drange(start, stop, step):
    while start < stop:
            yield start
            start += step

#funct to return the value of funct at a particuar value
def func(Vgb, Shi_s,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb):	    
	try:
      	  p=Vfb + Shi_s + ((sqrt(2*q*Es))/(Cox)) *(sqrt( Po*Phi_t*( e**(-Shi_s/Phi_t )-1) +( NA-ND  )*Shi_s + No*e**(-Vcb/Phi_t)*Phi_t*( e**(Shi_s/Phi_t )-1) )  ) -Vgb	  
	  return p
 	 
    	except ZeroDivisionError:
          print("Error!!!!!!!!!!!", Shi_s)
    	  return 0



#funct to find derivative at a particular value
def derivFunc( Shi_s,Vgb,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb):
    #main function with variable t
    t= Symbol('t')    
    f=Vfb + t + (sqrt(2*q*Es)/Cox) *(sqrt( Po*Phi_t*( e**(-t/Phi_t )-1) +( NA-ND  )*t + No*e**(-Vcb/Phi_t)*Phi_t*( e**(t/Phi_t )-1) )  ) -Vgb

    deriv= Derivative(f, t)

    k= deriv.doit().subs({t:Shi_s}) #this puts the value of t as Shi_s in the derivative of the main function
     
    if k==0:
	return 1
    else:
	return k




# Newton_Raphson to find the root of the function
def newtonRaphson( Vgb, Shi_s ,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb):

    err=1   	
    count=0
    # x(i+1) = x(i) - f(x) / f'(x)
    while abs(err) >= 0.001:
        count=count+1
	try:
      	    err = (func(Vgb,Shi_s,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb))/(derivFunc(Shi_s,Vgb,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb))
	    Shi_s = Shi_s - err
 	    #print("Shi_s is ",Shi_s)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", Shi_s)


    print("The value of the root is : ","%.4f"% Shi_s)
    print("the no of iterations is ",count)  #no of iterations for each value of vgb
    return Shi_s



def charge_funct(NA,Phi_t,Es,q,Shi_s,Phi_F,ND,Po,No,Vcb):
	#Qc=-(sqrt(2*q*Es*NA))*(sqrt(Phi_t*e**(-Shi_s/Phi_t)+Shi_s-Phi_t+e**(-2*Phi_F/Phi_t)*(Phi_t*e**(Shi_s/Phi_t)-Shi_s-Phi_t)))
	Qc=-(sqrt(2*q*Es))*(sqrt(Po*Phi_t*(e**(-Shi_s/Phi_t)-1)+(NA-ND)*Shi_s+No*e**(-Vcb/Phi_t)*Phi_t*(e**(Shi_s/Phi_t)-1)))
	return Qc


def deriv_funct(Shi_s,Qc,NA,Phi_t,Es,q,Phi_F,Vgb,Vfb,ND,Cox,No,Po,Vcb):
	
	t= Symbol('t')    
	V =Vfb + t + (sqrt(2*q*Es)/Cox) *(sqrt( Po*Phi_t*( e**(-t/Phi_t )-1) +( NA-ND  )*t + No*e**(-Vcb/Phi_t)*Phi_t*( e**(t/Phi_t )-1) )  ) 
    	deriv= Derivative(V, t)
	k= deriv.doit()


	Q=-(sqrt(2*q*Es))*(sqrt(Po*Phi_t*(e**(-t/Phi_t)-1)+(NA-ND)*t+No*e**(-Vcb/Phi_t)*Phi_t*(e**(t/Phi_t)-1)))
	der= Derivative(Q, t)
	d= der.doit()

	dq_dv=d/k
	put=dq_dv.subs({t:Shi_s})
	return abs(put)

