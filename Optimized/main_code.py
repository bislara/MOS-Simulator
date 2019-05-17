#importing modules to main_code
import matplotlib.pyplot as plt
from functions.function import *

print("Welcome !!!")
print("Enter all the values in the MKS system")


#constants initialize
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q
q=1.6*10**(-19)	        
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Eo=8.854*10**(-12)	
Ni=1.15*10**16		
i=0
r=[]
x0=[]
Y_list=[]
V_list=[]


#variable initialize
global Vgb_1,Vgb_2,Phi_g,tox,NA,ND




#user input
Vgb_1=float(input("Enter the value of starting value of Vgb :"))
Vgb_2=float(input("Enter the value of end value of Vgb :"))
Phi_g=float(input("Enter the value of the gate voltage :"))
tox=float(input("Enter the value of oxide thickness in nm :"))
tox=tox*10**(-9)
NA= float(input("Enter the value of NA :"))
ND= float(input("Enter the value of ND :"))





#initial calculations
Es=ks*Eo		
Eox=kox*Eo		#permittivity
Cox=Eox/tox		#oxide_capacitance per unit area
No=(Ni**2)/NA
Po=NA
Shi_F=Phi_t*log((NA)/(Ni))	#Fermi_energy
Vfb=-Phi_g-Shi_F		#Flatband_voltage

#to take 0.1 steps in Vgb
for i in range(int(Vgb_1),int(Vgb_2*10)):
	r.append(i/10.0)

#intial value calculations for Newton Raphson method
for Vgb in r:
	gm=(sqrt(2*q*Es*NA))/(Cox)	                        #body effect coefficient
	Shi_sa=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2 	#weak_inversion approximation
	Phi_o=0.826+0.026*6		                        #strong_inversion approximation
	x0.append(min(Shi_sa,Phi_o))		                


#main function with variable t
t= Symbol('t')    
f=Vfb + t + (sqrt(2*q*Es)/Cox) *(sqrt( Po*Phi_t*( e**(-t/Phi_t )-1) +( NA-ND  )*t + No*Phi_t*( e**(t/Phi_t )-1) )  ) -Vgb

deriv= Derivative(f, t)





#main_calculations

#loop for newton Raphson method and using diff intial value for diff Vgb
j=0
for Vgb in r:
	val=newtonRaphson(Vgb,x0[j],Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,deriv,t)  
	#print("the val is : ",val)
	Y_list.append(val)
	V_list.append(Vgb)
	j=j+1





# plotting_graph

#limiting the graph
plt.ylim(0.7,1.2)
plt.xlim(0,1.5)

plt.plot(V_list, Y_list,color ='r',label="NA=5*10^20")

#labelling the axes
plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

# show a legend on the plot 
plt.legend() 

plt.title('Vgb VS SHI graph') 
  
plt.show()   
