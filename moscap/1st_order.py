import matplotlib.pyplot as plt

from functions.function import *
from matplotlib.widgets import Slider,Button  # import the Slider widget
from scipy.integrate import odeint
import numpy as np

print("Welcome !!!")
#print("Enter all the values in the MKS system")

global Phi_m,tox,NA,ND,r,count,Qox,Qc,q,Es,Phi_t,Shi_F


#constants initialize
q=1.6*10**(-19)	      
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Ni=1.15*10**16		
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q

tox=2*10**(-9)
NA=5*10**23
Phi_m=0.56
ND=10
x0=0


#variable declaration
Es=ks*Eo		
Eox=kox*Eo		

Vgb=0.3

No=(Ni**2)/NA
Po=NA
Cox=Eox/tox
Qox=10**(-5)
Shi_F=Phi_t*log((NA)/(Ni)) 	
Vfb=-Phi_m-Shi_F-Qox/Cox

gm=(sqrt(2*q*Es*NA))/(Cox)
f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
n=2*Shi_F+Phi_t*6
x0= min(f,n)
print("x0 is :",x0)
val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po) 



# function that returns dz/dt
def model(z,t):
    #print(-(sqrt(2*q*Es*NA)/Es)*sqrt(Phi_t*e**(-z/Phi_t)+z-Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(z/Phi_t)-z-Phi_t)))
    dydt = -(sqrt(2*q*Es*NA)/Es)*sqrt(Phi_t*e**(-z/Phi_t)+z-Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(z/Phi_t)-z-Phi_t))
    return dydt


# time pointss
t = np.linspace(0,50*10**(-9),1000)


# solve ODE
z = odeint(model,val,t)
for i in z :
	i[0]=i[0]*(-1)
#print(z[0])


# plot results
plt.plot(t,z,'b-',label='Shi VS y')
plt.ylim(-1.5,1.5)
plt.xlim(0,5*10**(-8))


plt.ylabel('Shi')
plt.xlabel('Y')
plt.legend()
plt.show()


