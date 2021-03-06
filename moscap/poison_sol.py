# importing modules to main_code
from math import *
from sympy import *

import matplotlib.pyplot as plt
from functions.nMOS_funct import *
from matplotlib.widgets import Slider, Button, TextBox  # import the Slider widget
from scipy.integrate import odeint
import numpy as np
import csv

print("Welcome !!!")

#global declarations
global Phi_m, tox, NA, ND, r, count, Qox, Qc, q, Es, Phi_t, Shi_F, Eg, csv_count


# constants initialize
q = 1.6*10**(-19)
Eo = 8.854*10**(-12)
ks = 11.7  # ks for Si
kox = 3.9  # kox for SiO2
Ni = 1.15*10**16  # per m^3
Phi_t = 0.0259  # Thermal Voltage Phi_t=k*t/q

tox = 2*10**(-9)
NA = 5*10**23
Phi_m = 4.1
Eg = 0.56  # Eg=EG/2
ND = 10
x0 = 0  # initial value declaration
Vgb = 0.1
Qox = 10**(-5)
Ea = 4.05  # electron affinity of Silicon

# for more number of graphs and to distinguish between them
colour_count = 0
colours = {0: 'w', 1: 'b', 2: 'g', 3: 'r', 4: 'c', 5: 'm', 6: 'y', 7: 'k'}
count = 0
csv_count = 0

# variable declaration
Es = ks*Eo
Eox = kox*Eo

No = (Ni**2)/NA
Po = NA
Cox = Eox/tox

Shi_F = Phi_t*log((NA)/(Ni))
Vfb = +Phi_m-Ea-Eg-Shi_F-Qox/Cox

gm = (sqrt(2*q*Es*NA))/(Cox)


z = {}
z[count] = [[], []]
yt = []
PhiF_list = {}
condut_list = {}
graph_plot = {}
graph_plot2 = {}
csv_list = {}

y = {}
y[count] = []
PhiF_list[count] = []

# function for solving the differential equation

def model(x, t):
    y = x[0]
    dy = x[1]
    K = 0
    xdot = [[], []]
    xdot[0] = dy
    xdot[1] = -(q/Es)*(Po*(e**(-y/Phi_t)-1)-No*(e**(y/Phi_t)-1))
    # print(xdot[1])
    return xdot


# plotting_intial_graph
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.35, right=0.95)

graph_plot[count] = []
graph_plot[count], = plt.plot(
    yt, y[count], color=colours[colour_count], label="")

graph_plot2[count] = []
graph_plot2[count], = plt.plot(
    yt, PhiF_list[count], color=colours[colour_count], label="")


plt.title(r'$ \psi $ VS y graph')
plt.ylim(-1.5, 1.5)
plt.xlim(0, 5*10**(-8))
plt.minorticks_on()
plt.tick_params(direction="in")


plt.xlabel('y value')
plt.ylabel(r'$ \psi $ value')

# plt.legend()


# button_on_click function
def setValue(val):
    global count, colour_count, colours, Vgb, Vfb, tox, NA, Phi_m, yt
    count = count+1
    print("count is ", count)
    yt = np.linspace(0, 500*10**(-9), 1000)

    z[count] = [[], []]
    graph_plot[count] = []
    graph_plot2[count] = []

    No = (Ni**2)/NA
    Po = NA
    Cox = Eox/tox
    Qox = 10**(-5)
    Shi_F = Phi_t*log((NA)/(Ni))
    Vfb = +Phi_m-Ea-Eg-Shi_F-Qox/Cox
    print("Vfb is ", Vfb, Phi_m, Shi_F, Eg, Vgb)

    if Vgb > Vfb and count != 0:
        gm = (sqrt(2*q*Es*NA))/(Cox)
        f = (-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
        n = 2*Shi_F+Phi_t*6
        x0 = min(f, n)
        # print x0
        val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)
        d = -(sqrt(2*q*Es*NA)//Es)*sqrt(Phi_t*e**(-val/Phi_t)+val -
                                        Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(+val/Phi_t)-val-Phi_t))

        y[count] = []
        PhiF_list[count] = []
        ini = [val, d]
        z[count] = odeint(model, ini, yt)
        for i in z[count]:
            i[0] = i[0]*(-1)
            if i[0] > -10**(-50) or i[0] < -1.5:
                y[count].append((0+i_old)/2)
                i_old = (0+i_old)/2
            else:
                y[count].append(i[0])
                i_old = i[0]
            PhiF_list[count].append(-Eg-Shi_F)
        colour_count = colour_count+1

        plt.axes()
        plt.title(r'$\psi$ VS y graph')
        plt.ylim(-2.5, 1.5)
        plt.xlim(0, 5*10**(-8))

        plt.xlabel('y value')
        plt.ylabel(r'$\psi$ value')

        graph_plot[count], = plt.plot(
            yt, y[count], color=colours[colour_count], label="Graph")
        graph_plot2[count], = plt.plot(
            yt, PhiF_list[count], color=colours[colour_count], label=r"$E_I$", linestyle='--')
        if count == 1:
            plt.legend()
    else:
        print("Vgb is less than Vfb")


# slider val change function
def val_update_Vgb(val):
    global Vgb, tox, NA, Phi_m, count, colour_count, Vfb

    Vgb = slider1.val
    # print(Vgb,Vfb)
    if Vgb > Vfb and count != 0:
        f = (-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
        n = 2*Shi_F+Phi_t*6
        x0 = min(f, n)
        # print x0
        val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)
        d = -(sqrt(2*q*Es*NA)//Es)*sqrt(Phi_t*e**(-val/Phi_t)+val -
                                        Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(+val/Phi_t)-val-Phi_t))
        y[count] = []
        PhiF_list[count] = []

        ini = [val, d]
        z[count] = odeint(model, ini, yt)
        # print(z[count])
        for i in z[count]:
            i[0] = i[0]*(-1)
            if i[0] > -10**(-50) or i[0] < -1.5:
                y[count].append((0+i_old)/2)
                i_old = (0+i_old)/2
            else:
                y[count].append(i[0])
                i_old = i[0]
            PhiF_list[count].append(-Eg-Shi_F)
        graph_plot[count].set_ydata(y[count])
    # graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(PhiF_list[count])
        plt.draw          # redraw the plot

    else:
        print("Vgb is less than Vfb")


# Tox textbox submit function
def submit_tox(text):
    global Vgb, tox, NA, Phi_m, count, colour_count, Vfb
    tox = float(text)*10**(-9)
    Cox = Eox/tox
    Vfb = +Phi_m-Ea-Eg-Shi_F-Qox/Cox

    if Vgb > Vfb and count != 0:
        gm = (sqrt(2*q*Es*NA))/(Cox)
        f = (-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
        n = 2*Shi_F+Phi_t*6
        x0 = min(f, n)
        # print x0
        val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)
        d = -(sqrt(2*q*Es*NA)//Es)*sqrt(Phi_t*e**(-val/Phi_t)+val -
                                        Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(+val/Phi_t)-val-Phi_t))
        y[count] = []
        PhiF_list[count] = []

        ini = [val, d]
        z[count] = odeint(model, ini, yt)
        for i in z[count]:
            i[0] = i[0]*(-1)
            if i[0] > -10**(-50) or i[0] < -1.5:
                y[count].append((0+i_old)/2)
                i_old = (0+i_old)/2
            else:
                y[count].append(i[0])
                i_old = i[0]
            PhiF_list[count].append(-Eg-Shi_F)
        graph_plot[count].set_ydata(y[count])
        # graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(PhiF_list[count])
        plt.draw          # redraw the plot

    else:
        print("Vgb is less than Vfb")


# textbox NA submit function
def submit_NA(text):
    global Vgb, tox, NA, Phi_m, count, colour_count, Vfb
    NA = float(text)*10**(20)

    No = (Ni**2)/NA
    Po = NA
    Cox = Eox/tox
    Qox = 10**(-5)
    Shi_F = Phi_t*log((NA)/(Ni))
    Vfb = +Phi_m-Ea-Eg-Shi_F-Qox/Cox

    if Vgb > Vfb and count != 0:
        gm = (sqrt(2*q*Es*NA))/(Cox)
        f = (-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
        n = 2*Shi_F+Phi_t*6
        x0 = min(f, n)
        # print x0
        val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)
        d = -(sqrt(2*q*Es*NA)//Es)*sqrt(Phi_t*e**(-val/Phi_t)+val -
                                        Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(+val/Phi_t)-val-Phi_t))
        y[count] = []
        PhiF_list[count] = []

        ini = [val, d]
        z[count] = odeint(model, ini, yt)
        for i in z[count]:
            i[0] = i[0]*(-1)
            if i[0] > -10**(-50) or i[0] < -1.5:
                y[count].append((0+i_old)/2)
                i_old = (0+i_old)/2
            else:
                y[count].append(i[0])
                i_old = i[0]
            PhiF_list[count].append(-Eg-Shi_F)
        graph_plot[count].set_ydata(y[count])
        # graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(PhiF_list[count])
        plt.draw          # redraw the plot

    else:
        print("Vgb is less than Vfb")


# Phi_m textbox submit function
def submit_Phi_m(text):
    global Vgb, tox, NA, Phi_m, count, colour_count, Vfb
    Phi_m = float(text)

    Vfb = +Phi_m-Ea-Eg-Shi_F-Qox/Cox
    print("Vfb is ", Vfb)
    # print(Vgb,Vfb)
    if Vgb > Vfb and count != 0:
        gm = (sqrt(2*q*Es*NA))/(Cox)
        f = (-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
        n = 2*Shi_F+Phi_t*6
        x0 = min(f, n)
        # print x0
        val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)
        d = -(sqrt(2*q*Es*NA)//Es)*sqrt(Phi_t*e**(-val/Phi_t)+val -
                                        Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(+val/Phi_t)-val-Phi_t))
        y[count] = []
        PhiF_list[count] = []

        ini = [val, d]
        z[count] = odeint(model, ini, yt)
        for i in z[count]:
            i[0] = i[0]*(-1)
            if i[0] > -10**(-50) or i[0] < -1.5:
                y[count].append((0+i_old)/2)
                i_old = (0+i_old)/2
            else:
                y[count].append(i[0])
                i_old = i[0]
            PhiF_list[count].append(-Eg-Shi_F)
        graph_plot[count].set_ydata(y[count])
        # graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(PhiF_list[count])
        plt.draw          # redraw the plot

    else:
        print("Vgb is less than Vfb")


# # funct to save the data points in csv file
# def setData(val):
#     global tox, ND, Phi_m, Qox, csv_count, count, Vgb
#     # initial calculations
#     csv_list[csv_count] = []
#     yt = np.linspace(0, 500*10**(-9), 1000)
#     print(yt)
#     r = []
#     No = (Ni**2)/NA
#     Po = NA
#     Cox = Eox/tox
#     Qox = 10**(-5)
#     Shi_F = Phi_t*log((NA)/(Ni))
#     Vfb = +Phi_m-Ea-Eg-Shi_F-Qox/Cox

#     list_no = 0
#     if csv_count == 0 and Vgb > Vfb:
#         csv_list[csv_count].append([])
#         csv_list[csv_count][list_no] = [
#             'Vgb ='+str(Vgb),'Tox ='+str(tox), 'NA ='+str(NA), 'Phi_m ='+str(Phi_m)]
#         list_no += 1
#         csv_list[csv_count].append([])
#         csv_list[csv_count][list_no] = ['y ('+str(csv_count)+')', 'Shi ('+str(
#             csv_count)+')']
#         list_no += 1
#         gm = (sqrt(2*q*Es*NA))/(Cox)
#         f = (-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
#         n = 2*Shi_F+Phi_t*6
#         x0 = min(f, n)
#         # print x0
#         val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)
#         d = -(sqrt(2*q*Es*NA)//Es)*sqrt(Phi_t*e**(-val/Phi_t)+val -
#                                         Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(+val/Phi_t)-val-Phi_t))

#         ini = [val, d]
#         z[count] = odeint(model, ini, yt)
#         for j in len(yt):
#             csv_list[csv_count][list_no].append(yt[j])
#             csv_list[csv_count][list_no].append(z[count][j])    
#             list_no += 1

        
#         with open('./Dataset/moscap/Shi_Vs_y.csv', 'w') as csvFile:
#             writer = csv.writer(csvFile)
#             writer.writerow([])
#             writer.writerows(csv_list[csv_count])
#         print("Written 1st time")
#         csv_count += 1

#     elif csv_count != 0 and Vgb>Vfb:
#         list_no = 0
#         csv_list[csv_count].append([])
#         csv_list[csv_count][list_no] = [
#             'Vgb ='+str(Vgb),'Tox ='+str(tox), 'NA ='+str(NA), 'Phi_m ='+str(Phi_m)]
#         list_no += 1
#         csv_list[csv_count].append([])
#         csv_list[csv_count][list_no] = ['y ('+str(csv_count)+')', 'Shi ('+str(
#             csv_count)+')']
#         list_no += 1
#         gm = (sqrt(2*q*Es*NA))/(Cox)
#         f = (-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
#         n = 2*Shi_F+Phi_t*6
#         x0 = min(f, n)
#         # print x0
#         val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)
#         d = -(sqrt(2*q*Es*NA)//Es)*sqrt(Phi_t*e**(-val/Phi_t)+val -
#                                         Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(+val/Phi_t)-val-Phi_t))

#         ini = [val, d]
#         z[count] = odeint(model, ini, yt)
#         for j in len(yt):
#             csv_list[csv_count][list_no].append(yt[j])
#             csv_list[csv_count][list_no].append(z[count][j])    
#             list_no += 1

#         with open('./Dataset/moscap/Shi_Vs_y.csv', 'a') as csvFile:
#             writer = csv.writer(csvFile)
#             writer.writerow([])
#             writer.writerows(csv_list[csv_count])
#         print("saved data for "+str(csv_count)+" times")
#         csv_count += 1

#     else:
#         print("Sorry couldn't save the data")

# button_declaration
axButton = plt.axes([0.83, 0.15, 0.06, 0.06])  # xloc,yloc,width,heights
btn = Button(axButton, ' ADD ')

# axButton1 = plt.axes([0.83, 0.05, 0.08, 0.06])  # xloc,yloc,width,heights
# btn1 = Button(axButton1, ' Save Data ')

# button on click callback function
btn.on_clicked(setValue)
# btn1.on_clicked(setData)


# Sliders declaration
axSlider1 = plt.axes([0.1, 0.20, 0.55, 0.02])  # xloc,yloc,width,height
slider1 = Slider(ax=axSlider1, label='Vgb', valmin=-1, valmax=3,
                 valinit=Vgb, valfmt='Vgb is '+'%1.3f' + ' V', color="green")

# sliders on change function call
slider1.on_changed(val_update_Vgb)


# Text Box declaration and on_submit function call
toxbox = plt.axes([0.2, 0.14, 0.4, 0.04])
tox_box = TextBox(toxbox, 'Tox in nm', initial=str(tox*10**9))
tox_box.on_submit(submit_tox)

NAbox = plt.axes([0.2, 0.08, 0.4, 0.04])
NA_box = TextBox(NAbox, 'NA in 10**20', initial=str(NA/10.0**20))
NA_box.on_submit(submit_NA)

Phi_mbox = plt.axes([0.2, 0.02, 0.4, 0.04])
Phi_m_box = TextBox(Phi_mbox, r'$ \phi_M $'+' in eV', initial=str(Phi_m))
Phi_m_box.on_submit(submit_Phi_m)


# finally display the graph...
plt.show()


print("Thank you for using the tool \n")
