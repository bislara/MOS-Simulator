# importing modules to main_code
from math import *
from sympy import *

import matplotlib.pyplot as plt
from functions.function import *
from matplotlib.widgets import Slider, Button  # import the Slider widget
import numpy as np
import csv

print("Welcome !!!")
#print("Enter all the values in the MKS system")

global Phi_m, tox, NA, ND, r, count, Qox, Qc, csv_count


# constants initialize
q = 1.6*10**(-19)
Eo = 8.854*10**(-12)
ks = 11.7  # ks for Si
kox = 3.9  # kox for SiO2
Ni = 1.15*10**16
Phi_t = 0.0259  # Thermal Voltage Phi_t=k*t/q

tox = 2*10**(-9)
# tox=tox*10**(-9)
# NA=5*10**23
Phi_m = 4.1  # for Al
Eg = 0.56  # Eg=EG/2= 1.12/2
ND = 5*10**23
NA = 10
Qox = 10**(-5)
Ea = 4.05  # electron affinity of silicon

# variable declaration
r = []
Y_list = {}
V_list = {}
Y1_list = {}
V1_list = {}
Y2_list = {}
V2_list = {}
Y3_list = {}
V3_list = {}
Cox_list = {}
Cox_val_list = {}
csv_list = {}

count = 0
csv_count = 0
Y_list[count] = []
V_list[count] = []
Y1_list[count] = []
V1_list[count] = []
Y2_list[count] = []
V2_list[count] = []
Y3_list[count] = []
V3_list[count] = []
Cox_list[count] = []
Cox_val_list[count] = []

graph_plot = {}
graph_plot1 = {}
graph_plot2 = {}
graph_plot3 = {}
graph_plot4 = {}

Es = ks*Eo
Eox = kox*Eo

colour_count = 0
colours = {1: 'b', 2: 'r', 3: 'g', 4: 'm', 5: 'c', 6: 'y', 7: 'k'}


# plotting_graph
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=False)
plt.subplots_adjust(left=0.08, bottom=0.3, right=0.98, top=0.99)

mu, sigma = 1e-3, 1e-4
#s = np.random.normal(mu, sigma, 10000)


# 1
ax1.set_xlim(-1.6, 0.1)
# ax1.set_ylim(-0.5,0.4)

ax1.set_xlabel('Vgb (V)')
ax1.set_ylabel(r'$\psi_S$ (V)')

ax1.minorticks_on()
ax1.tick_params(direction="in")

# 2
ax2.set_xlabel(r'$ \psi_s$ (V)')
ax2.set_ylabel('Q (C/m^2 *10^(-3))')

ax2.set_xlim(-1.2, 0.1)
ax2.set_ylim(0, 10)
# ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%1.2E'))
ax2.minorticks_on()
ax2.tick_params(direction="in")


# 3
ax3.set_xlim(-1.6, 0.1)
ax3.set_ylim(0, 10)

ax3.set_xlabel('Vgb (V)')
ax3.set_ylabel('Q (C/m^2 *10^(-3))')
ax3.minorticks_on()
ax3.tick_params(direction="in")

# 4
ax4.set_xlim(-2, 0)
ax4.set_ylim(0, 3)

ax4.set_xlabel('Vgb (V)')
ax4.set_ylabel('dQ/dVgb (F/m^2 *10^(-2))')
ax4.minorticks_on()
ax4.tick_params(direction="in")


# 2-D variable of graph
graph_plot[count] = []
graph_plot[count], = plt.plot(
    V_list[count], Y_list[count], color='r', label="")

graph_plot1[count] = []
graph_plot1[count], = plt.plot(
    V1_list[count], Y1_list[count], color='r', label="")

graph_plot2[count] = []
graph_plot2[count], = plt.plot(
    V2_list[count], Y2_list[count], color='r', label="")

graph_plot3[count] = []
graph_plot3[count], = plt.plot(
    V3_list[count], Y3_list[count], color='r', label="")

graph_plot4[count] = []
graph_plot4[count], = plt.plot(
    Cox_list[count], Cox_val_list[count], color='r', label="")

# plt.legend()


# button function for adding plots
def setValue(val):
    global count, colour_count, colours, Qox
    count = count+1

    # list initialization
    Y_list[count] = []
    V_list[count] = []
    graph_plot[count] = []
    Y1_list[count] = []
    V1_list[count] = []
    graph_plot1[count] = []
    Y2_list[count] = []
    V2_list[count] = []
    graph_plot2[count] = []
    Y3_list[count] = []
    V3_list[count] = []
    graph_plot3[count] = []
    Cox_list[count] = []
    Cox_val_list[count] = []
    graph_plot4[count] = []

    r = []
    Po = (Ni**2)/ND
    No = ND
    Shi_F = Phi_t*log((ND)/(Ni))
    n = -(2*Shi_F+Phi_t*6)
    Cox = Eox/tox
    Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
    gm = (sqrt(2*q*Es*ND))/(Cox)

    # drange funct for creating steps in for loop
    for i in drange(-1.9, -0.2, 0.05):
        r.append(i)

    for Vgb in r:
        f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
        x0 = max(f, n)
        # print(Vgb,Vfb,x0)
        val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)

        Qc = (charge_funct(NA, Phi_t, Es, q, val, Shi_F, ND, Po, No))
        dq_dVgb = deriv_funct(val, Qc, NA, Phi_t, Es, q,
                              Shi_F, Vgb, Vfb, ND, Cox, No, Po)

        V_list[count].append(Vgb)
        Y_list[count].append(abs(val))

        V1_list[count].append(val)
        Y1_list[count].append(Qc*1000)

        V2_list[count].append(Vgb)
        Y2_list[count].append(Qc*1000)

        V3_list[count].append(Vgb)
        Y3_list[count].append(dq_dVgb*100)

        Cox_list[count].append(Vgb)
        Cox_val_list[count].append(Cox*100)

    colour_count = colour_count+1

    plt.sca(ax1)
    graph_plot[count], = plt.plot(
        V_list[count], Y_list[count], color=colours[colour_count], label="Curve "+str(count))
    plt.legend()

    plt.sca(ax2)
    graph_plot1[count], = plt.plot(
        V1_list[count], Y1_list[count], color=colours[colour_count], label="Curve "+str(count))
    plt.legend()

    plt.sca(ax3)
    graph_plot2[count], = plt.plot(
        V2_list[count], Y2_list[count], color=colours[colour_count], label="Curve "+str(count))
    plt.legend()

    plt.sca(ax4)
    graph_plot3[count], = plt.plot(
        V3_list[count], Y3_list[count], color=colours[colour_count], label="Curve "+str(count))
    graph_plot4[count], = plt.plot(
        Cox_list[count], Cox_val_list[count], color=colours[colour_count], linestyle='--')

    plt.legend()


# sliders Update functions of Tox
def val_update_tox(val):
    global tox, ND, Phi_m, count, Qox

    if count != 0:
        # list initialization
        r = []
        Y_list[count] = []
        V_list[count] = []
        Y1_list[count] = []
        V1_list[count] = []
        Y2_list[count] = []
        V2_list[count] = []
        Y3_list[count] = []
        V3_list[count] = []
        Cox_list[count] = []
        Cox_val_list[count] = []

        tox = (slider1.val)*10**(-9)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        n = -(2*Shi_F+Phi_t*6)
        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)

        for i in drange(-1.9, Vfb-0.01, 0.05):
            r.append(i)

        for Vgb in r:
            f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
            x0 = max(f, n)
            val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                Phi_t, q, Es, Cox, No, Po)
            Qc = (charge_funct(NA, Phi_t, Es, q, val, Shi_F, ND, Po, No))
            dq_dVgb = deriv_funct(val, Qc, NA, Phi_t, Es,
                                  q, Shi_F, Vgb, Vfb, ND, Cox, No, Po)
            V_list[count].append(Vgb)
            Y_list[count].append(abs(val))

            V1_list[count].append(val)
            Y1_list[count].append((Qc)*1000)

            V2_list[count].append(Vgb)
            Y2_list[count].append((Qc)*1000)

            V3_list[count].append(Vgb)
            Y3_list[count].append(dq_dVgb*100)

            Cox_list[count].append(Vgb)
            Cox_val_list[count].append(Cox*100)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot1[count].set_ydata(Y1_list[count])
        graph_plot1[count].set_xdata(V1_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(Y2_list[count])
        graph_plot2[count].set_xdata(V2_list[count])
        plt.draw          # redraw the plot
        graph_plot3[count].set_ydata(Y3_list[count])
        graph_plot3[count].set_xdata(V3_list[count])
        graph_plot4[count].set_ydata(Cox_val_list[count])
        graph_plot4[count].set_xdata(Cox_list[count])

        plt.draw          # redraw the plot


# sliders Update functions of NA
def val_update_ND(val):
    global tox, NA, Phi_m, count, Qox, ND

    if count != 0:
        # list initialization
        Y_list[count] = []
        V_list[count] = []
        Y1_list[count] = []
        V1_list[count] = []
        Y2_list[count] = []
        V2_list[count] = []
        Y3_list[count] = []
        V3_list[count] = []
        Cox_list[count] = []
        Cox_val_list[count] = []

        r = []
        ND = (slider2.val)*10**22
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        n = -(2*Shi_F+Phi_t*6)
        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)

        for i in drange(-1.9, Vfb-0.01, 0.05):
            r.append(i)

        for Vgb in r:
            f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
            x0 = max(f, n)
            val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                Phi_t, q, Es, Cox, No, Po)
            Qc = (charge_funct(NA, Phi_t, Es, q, val, Shi_F, ND, Po, No))
            dq_dVgb = deriv_funct(val, Qc, NA, Phi_t, Es,
                                  q, Shi_F, Vgb, Vfb, ND, Cox, No, Po)
            V_list[count].append(Vgb)
            Y_list[count].append(abs(val))

            V1_list[count].append(val)
            Y1_list[count].append((Qc)*1000)

            V2_list[count].append(Vgb)
            Y2_list[count].append((Qc)*1000)

            V3_list[count].append(Vgb)
            Y3_list[count].append(dq_dVgb*100)

            Cox_list[count].append(Vgb)
            Cox_val_list[count].append(Cox*100)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot1[count].set_ydata(Y1_list[count])
        graph_plot1[count].set_xdata(V1_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(Y2_list[count])
        graph_plot2[count].set_xdata(V2_list[count])
        plt.draw          # redraw the plot
        graph_plot3[count].set_ydata(Y3_list[count])
        graph_plot3[count].set_xdata(V3_list[count])
        graph_plot4[count].set_ydata(Cox_val_list[count])
        graph_plot4[count].set_xdata(Cox_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Phi_m
def val_update_Phi(val):
    global tox, NA, Phi_m, count, Qox, ND

    if count != 0:
        # list initialization
        Y_list[count] = []
        V_list[count] = []
        Y1_list[count] = []
        V1_list[count] = []
        Y2_list[count] = []
        V2_list[count] = []
        Y3_list[count] = []
        V3_list[count] = []
        Cox_list[count] = []
        Cox_val_list[count] = []

        r = []
        Phi_m = slider3.val
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        n = -(2*Shi_F+Phi_t*6)
        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)

        for i in drange(-1.9, Vfb-0.01, 0.05):
            r.append(i)

        for Vgb in r:
            f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
            x0 = max(f, n)
            val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                Phi_t, q, Es, Cox, No, Po)
            Qc = (charge_funct(NA, Phi_t, Es, q, val, Shi_F, ND, Po, No))
            dq_dVgb = deriv_funct(val, Qc, NA, Phi_t, Es,
                                  q, Shi_F, Vgb, Vfb, ND, Cox, No, Po)
            V_list[count].append(Vgb)
            Y_list[count].append(abs(val))

            V1_list[count].append(val)
            Y1_list[count].append((Qc)*1000)

            V2_list[count].append(Vgb)
            Y2_list[count].append((Qc)*1000)

            V3_list[count].append(Vgb)
            Y3_list[count].append(dq_dVgb*100)

            Cox_list[count].append(Vgb)
            Cox_val_list[count].append(Cox*100)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot1[count].set_ydata(Y1_list[count])
        graph_plot1[count].set_xdata(V1_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(Y2_list[count])
        graph_plot2[count].set_xdata(V2_list[count])
        plt.draw          # redraw the plot
        graph_plot3[count].set_ydata(Y3_list[count])
        graph_plot3[count].set_xdata(V3_list[count])
        graph_plot4[count].set_ydata(Cox_val_list[count])
        graph_plot4[count].set_xdata(Cox_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Qox
def val_update_Qox(val):
    global tox, NA, Phi_m, count, Qox, ND

    if count != 0:
        # list initialization
        Y_list[count] = []
        V_list[count] = []
        Y1_list[count] = []
        V1_list[count] = []
        Y2_list[count] = []
        V2_list[count] = []
        Y3_list[count] = []
        V3_list[count] = []
        Cox_list[count] = []
        Cox_val_list[count] = []
        r = []

        Qox = (slider4.val)*10**(-6)  # getting slider value

        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        n = -(2*Shi_F+Phi_t*6)
        Cox = Eox/tox

        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)

        for i in drange(-1.9, Vfb-0.01, 0.05):
            r.append(i)

        for Vgb in r:
            f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
            x0 = max(f, n)
            val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                Phi_t, q, Es, Cox, No, Po)
            Qc = (charge_funct(NA, Phi_t, Es, q, val, Shi_F, ND, Po, No))
            dq_dVgb = deriv_funct(val, Qc, NA, Phi_t, Es,
                                  q, Shi_F, Vgb, Vfb, ND, Cox, No, Po)
            V_list[count].append(Vgb)
            Y_list[count].append(abs(val))

            V1_list[count].append(val)
            Y1_list[count].append((Qc)*1000)

            V2_list[count].append(Vgb)
            Y2_list[count].append((Qc)*1000)

            V3_list[count].append(Vgb)
            Y3_list[count].append(dq_dVgb*100)

            Cox_list[count].append(Vgb)
            Cox_val_list[count].append(Cox*100)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot
        graph_plot1[count].set_ydata(Y1_list[count])
        graph_plot1[count].set_xdata(V1_list[count])
        plt.draw          # redraw the plot
        graph_plot2[count].set_ydata(Y2_list[count])
        graph_plot2[count].set_xdata(V2_list[count])
        plt.draw          # redraw the plot
        graph_plot3[count].set_ydata(Y3_list[count])
        graph_plot3[count].set_xdata(V3_list[count])
        graph_plot4[count].set_ydata(Cox_val_list[count])
        graph_plot4[count].set_xdata(Cox_list[count])
        plt.draw          # redraw the plot


# funct to save the data points in csv file
def setData(val):
    global tox, ND, Phi_m, Qox, csv_count, count
    # initial calculations
    csv_list[csv_count] = []
    r = []
    Po = (Ni**2)/ND
    No = ND
    Shi_F = Phi_t*log((ND)/(Ni))
    n = -(2*Shi_F+Phi_t*6)
    Cox = Eox/tox
    Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
    gm = (sqrt(2*q*Es*ND))/(Cox)

    for i in drange(-1.9, Vfb-0.01, 0.05):
            r.append(i)

    list_no = 0
    if csv_count == 0:
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no]=['Tox ='+str(tox),'ND ='+str(ND),'Phi_m ='+str(Phi_m),'Qox ='+str(Qox)]
        list_no+=1
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no] = ['Vgb ('+str(csv_count)+')', 'Shi_s ('+str(
            csv_count)+')', 'Qc ('+str(csv_count)+')', 'dq/dVgb ('+str(csv_count)+')']
        list_no += 1
        for Vgb in r:
            csv_list[csv_count].append([])
            f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
            x0 = max(f, n)
            val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                Phi_t, q, Es, Cox, No, Po)
            Qc = (charge_funct(NA, Phi_t, Es, q, val, Shi_F, ND, Po, No))
            dq_dVgb = deriv_funct(val, Qc, NA, Phi_t, Es,
                                  q, Shi_F, Vgb, Vfb, ND, Cox, No, Po)
            csv_list[csv_count][list_no].append(Vgb)
            csv_list[csv_count][list_no].append(val)
            csv_list[csv_count][list_no].append(Qc)
            csv_list[csv_count][list_no].append(dq_dVgb)
            list_no += 1

        with open('Datasets/pMOS.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([])
            writer.writerows(csv_list[csv_count])
        print("Written 1st time")
        csv_count += 1

    elif csv_count != 0:
        list_no = 0
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no]=['Tox ='+str(tox),'ND ='+str(ND),'Phi_m ='+str(Phi_m),'Qox ='+str(Qox)]
        list_no+=1
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no] = ['Vgb ('+str(csv_count)+')', 'Shi_s ('+str(
            csv_count)+')', 'Qc ('+str(csv_count)+')', 'dq/dVgb ('+str(csv_count)+')']
        list_no += 1

        for Vgb in r:
            csv_list[csv_count].append([])
            f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2
            x0 = max(f, n)
            val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                Phi_t, q, Es, Cox, No, Po)
            Qc = (charge_funct(NA, Phi_t, Es, q, val, Shi_F, ND, Po, No))
            dq_dVgb = deriv_funct(val, Qc, NA, Phi_t, Es,
                                  q, Shi_F, Vgb, Vfb, ND, Cox, No, Po)
            csv_list[csv_count][list_no].append(Vgb)
            csv_list[csv_count][list_no].append(val)
            csv_list[csv_count][list_no].append(Qc)
            csv_list[csv_count][list_no].append(dq_dVgb)
            list_no += 1

        with open('Datasets/pMOS.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([])
            writer.writerows(csv_list[csv_count])
        print("saved data for "+str(csv_count)+" times")
        csv_count += 1

    else:
        print("Sorry couldn't save the data")


# button_declaration
axButton = plt.axes([0.83, 0.15, 0.06, 0.06])  # xloc,yloc,width,heights
btn = Button(axButton, ' ADD ')

axButton1 = plt.axes([0.83, 0.05, 0.08, 0.06])  # xloc,yloc,width,heights
btn1 = Button(axButton1, ' Save Data ',hovercolor='r')

# button on click callback function
btn.on_clicked(setValue)
btn1.on_clicked(setData)


# Sliders declaration
axSlider1 = plt.axes([0.1, 0.20, 0.55, 0.02])  # xloc,yloc,width,height
slider1 = Slider(ax=axSlider1, label='Tox', valmin=1, valmax=8,
                 valinit=tox*10**(9), valfmt='tox is '+'%1.2f' + ' nm', color="green")


axSlider2 = plt.axes([0.1, 0.15, 0.55, 0.02])  # xloc,yloc,width,height
slider2 = Slider(axSlider2, 'ND', valmin=1, valmax=100, valinit=ND /
                 (10**22), valfmt='ND is '+'%1.2f' + ' *10**22 m^-3')


axSlider3 = plt.axes([0.1, 0.10, 0.55, 0.02])  # xloc,yloc,width,height
slider3 = Slider(axSlider3, r'$\phi_m$', valmin=4, valmax=4.5,
                 valinit=Phi_m, valfmt=r'$\phi_m$ is '+'%1.2f'+' eV', color="red")


axSlider4 = plt.axes([0.1, 0.05, 0.55, 0.02])  # xloc,yloc,width,height
slider4 = Slider(axSlider4, 'Qox', valmin=1, valmax=1000, valinit=Qox *
                 10**6, valfmt='Qox is '+'%1.2f'+'*10^(-6)' + ' C/m^2', color="yellow")


# sliders on change function call
slider1.on_changed(val_update_tox)
slider2.on_changed(val_update_ND)
slider3.on_changed(val_update_Phi)
slider4.on_changed(val_update_Qox)

plt.show()


print("Thank you for using the tool \n")
