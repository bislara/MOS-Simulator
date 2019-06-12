#importing modules to main_code
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from functions.function import *

#variable declaration
global Vgb_1,Vgb_2,Phi_g,tox,NA,ND,Condition


print("Welcome !!!")
print("Enter all the values in the MKS system")


#constants initialize
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q
q=1.6*10**(-19)	        
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Ni=1.15*10**16		
i=0
plot_type=0
r=[]	
Y_list={}
V_list={}

Condition=1
colour_count=1
colours={1:'b',2:'g',3:'r',4:'c',5:'m',6:'y',7:'k'}

while Condition == 1: 
	#switch case functions
	def tox_type(): 
		global tox,NA,Phi_g
		tox=[]
		tox.append(float(input("Enter the value of oxide thickness in nm :\n")))
		tox_no = raw_input("Do you want to enter more value of Tox? Y/N \n")
		while tox_no == 'Y': 
			tox.append(float(input("Enter the value of oxide thickness in nm :\n")))
			tox_no = raw_input("Do you want to enter more value of Tox? Y/N\n")
		NA= float(input("Enter the value of NA in m^3 :\n"))
		Phi_g=float(input("Enter the value of the gate voltage :\n"))
		tox = [i * 10**(-9) for i in tox]
		

	def NA_type(): 
		global tox,NA,Phi_g
		NA=[]
		NA.append(float(input("Enter the value of NA in per m^3 :\n")))
		NA_no = raw_input("Do you want to enter more value of NA? Y/N\n")
		while NA_no == 'Y': 
			NA.append(float(input("Enter the value of NA in per m^3 :\n")))
			NA_no = raw_input("Do you want to enter more value of NA? Y/N\n")
		tox= float(input("Enter the value of tox  in nm:\n"))
		Phi_g=float(input("Enter the value of the gate voltage :\n"))
		tox=tox*10**(-9)

	def Phi_g_type():
		global tox,NA,Phi_g
		Phi_g=[]
		Phi_g.append(float(input("Enter the value of Phi_m :\n")))
		Phi_no = raw_input("Do you want to enter more value of Phi_m? Y/N\n")
		while Phi_no == 'Y': 
			Phi_g.append(float(input("Enter the value of Phi_m :\n")))
			Phi_no = raw_input("Do you want to enter more value of Phi_m? Y/N\n")
		tox= float(input("Enter the value of tox  in nm:\n"))
		NA=float(input("Enter the value of the NA in per m^3 :\n"))
		tox=tox*10**(-9)
		

	#conditions of switch case
	switcher={
		1: tox_type,	   
		2: NA_type,
		3: Phi_g_type	
		}

	#switch case
	def cases(argument): 
		func=switcher.get(argument,"Enter valid number...")
		if func == 'Enter valid number...':
			print(func)
		else :	
			func()


	#user input
	Vgb_1=float(input("Enter the value of starting value of Vgb :\n"))
	Vgb_2=float(input("Enter the value of end value of Vgb :\n"))

	print("Which type of graph do you want? \n 1.Tox graph\n 2.NA graph\n 3.Phi_m graph ?\n")
	plot_type = input("Enter the number :")
	if plot_type!=0: 
		cases(plot_type)

	ND= float(input("Enter the value of ND :\n"))






	#initial calculations
	Es=ks*Eo		
	Eox=kox*Eo		#permittivity

	#to take 0.1 steps in Vgb
	for i in range(int(Vgb_1),int(Vgb_2*10)):
		r.append(i/10.0)
	




	#main_calculations

	#loop for newton Raphson method and using diff intial value for diff Vgb
	if plot_type==1:
	    No=(Ni**2)/NA
	    Po=NA
	    Shi_F=Phi_t*log((NA)/(Ni))	#Fermi_energy
	    Vfb=-Phi_g-Shi_F		#Flatband_voltage
	    n=2*Shi_F+Phi_t*6
	    for i in tox:
		Y_list[i]=[]
		V_list[i]=[]
		Cox=(Eox/i)		#oxide_capacitance per unit area
		gm=(sqrt(2*q*Es*NA))/(Cox)
		for Vgb in r:
			f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
			x0= min(f,n)
			val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
			Y_list[i].append(val)
			V_list[i].append(Vgb)	
		
		plt.plot(V_list[i], Y_list[i], color=colours[colour_count],label="tox= "+str(i))
		colour_count=colour_count+1
		

	elif plot_type==2 :
	   Cox=(Eox/tox)		#oxide_capacitance per unit area 	
	   for i in NA:
		Y_list[i]=[]
		V_list[i]=[]
		No=(Ni**2)/i
		Po=i
		Shi_F=Phi_t*log((i)/(Ni))	#Fermi_energy
		Vfb=-Phi_g-Shi_F		#Flatband_voltage
		gm=(sqrt(2*q*Es*i))/(Cox)
		n=2*Shi_F+Phi_t*6
		for Vgb in r:
			f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
			x0= min(f,n)
			val=newtonRaphson(Vgb,x0,Vfb,i,ND,Phi_t,q,Es,Cox,No,Po)  
			Y_list[i].append(val)
			V_list[i].append(Vgb)

		plt.plot(V_list[i], Y_list[i],color =colours[colour_count],label="NA= "+str(i))
		colour_count=colour_count+1
		

	elif plot_type==3: 
	   Cox=(Eox/tox)		#oxide_capacitance per unit area
	   No=(Ni**2)/NA
	   Po=NA
	   Shi_F=Phi_t*log((NA)/(Ni)) 	
	   gm=(sqrt(2*q*Es*NA))/(Cox)
	   n=2*Shi_F+Phi_t*6	
	   for i in Phi_g:
		Y_list[i]=[]
		V_list[i]=[]	#Fermi_energy
		Vfb=-i-Shi_F		#Flatband_voltage	
		for Vgb in r:
			f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
			x0= min(f,n)
			val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
			Y_list[i].append(val)
			V_list[i].append(Vgb)
		plt.plot(V_list[i], Y_list[i],color =colours[colour_count],label="NA= "+str(i))
		colour_count=colour_count+1
		

	else :
		print("Wrong type of plot choosen")


	# plotting_graph

	#limiting the graph
	plt.ylim(0,1.2)
	plt.xlim(0,1.5)

	#labelling the axes
	plt.xlabel('Vgb value') 
	plt.ylabel('SHI value')

	# show a legend on the plot 
	plt.legend() 

	plt.title('Vgb VS SHI graph') 
	plt.show()

	#if want to continue to plot more
	Condition = input("Do you want to simulate more? 1/0")
	if Condition == 0:
		break
	   	
	colour_count=1
	Y_list={}
	V_list={}
	plot_type=0
	r=[]
	
print("Thank you for using the tool!!!  ")
