

def setValue(val):
	global count,colour_count,colours,Y_list,V_list,txt
	count=count+1
	print("count is ",count)
	
	Y_list[count]=[]
	V_list[count]=[]
	graph_plot[count]=[]
	r=[]
	Po=NA	
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F	#ignoring the potential drop across the oxide layer
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
	
	for i in range(-5,15):
		r.append(i/10.0)
	
	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
		x0= min(f,n)	
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		#print("the val is : ",val)
		Y_list[count].append(val)
		V_list[count].append(Vgb)
	colour_count=colour_count+1
	txt.remove()	
	plt.axes()
	plt.ylim(0,1.2) 
	plt.xlim(-1,2) 
#	title_slider(count)
	txt= plt.text(0.2, -0.15, 'Slider '+str(count), fontsize=18)	
	graph_plot[count],= plt.plot(V_list[count], Y_list[count],color =colours[colour_count],label="Curve "+str(count))	
	plt.legend()




#sliders Update functions
def val_update_tox(val):
    global tox,NA,Phi_m,count,Y_list,V_list,graph_plot
	
    if count!=0:
	r=[]
	Y_list[count]=[]
	V_list[count]=[]
	tox=slider1.val
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F
	Cox=Eox/tox		
	gm=(sqrt(2*q*Es*NA))/(Cox)

	for i in range(Vfb*10+1,20):
		r.append(i/10.0)

   	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list[count].append(val)
		V_list[count].append(Vgb)

	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot


def val_update_NA(val):
    global tox,NA,Phi_m,count,Y_list,V_list,graph_plot

    if count!=0:
	Y_list[count]=[]
	V_list[count]=[]
	r=[]
	NA=(slider2.val)*10**23
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
   	
	for i in range(Vfb*10+1,20):
		r.append(i/10.0)

	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list[count].append(val)
		V_list[count].append(Vgb)
	
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot


def val_update_Phi(val):
    global tox,NA,Phi_m,count,Y_list,V_list,graph_plot

    if count!=0:
	print("Count inside Phi_m is ",count)
	Y_list[count]=[]
	V_list[count]=[]
	r=[]
	Phi_m=slider3.val
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
   	
	for i in range(Vfb*10+1,20):
		r.append(i/10.0)

	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list[count].append(val)
		V_list[count].append(Vgb)
	
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot



