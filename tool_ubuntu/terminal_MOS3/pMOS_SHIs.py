# importing modules to main_code
from math import *
from sympy import *

import matplotlib.pyplot as plt
from MOS_3_functions.function import *
from matplotlib.widgets import Slider, Button  # import the Slider widget
import numpy as np

global Phi_m, tox, NA, ND, r, count, Qox, Qc

print("Welcome !!!")


# constants initialize
q = 1.6*10**(-19)
Eo = 8.854*10**(-12)
ks = 11.7  # ks for Si
kox = 3.9  # kox for SiO2
Ni = 1.15*10**16  # intrinsic concentration in per m^3
Phi_t = 0.0259  # Thermal Voltage Phi_t=k*t/q2
tox = 2*10**(-9)
ND = 5*10**23
Eg = 0.56  # Eg=EG/2= 1.12/2
NA = 10
Qox = 10**(-5)
Phi_m = 4.1  # for Al
Ea = 4.05  # electron affinity of Silicon
count = 0
Vgb = -1.5

# for more number of graphs and to distinguish between them
colour_count = 0
colours = {1: 'b', 2: 'g', 3: 'r', 4: 'c', 5: 'm', 6: 'y', 7: 'k'}

# variable declaration
r = []
Y_list = {}
V_list = {}

Y_list[count] = []
V_list[count] = []

graph_plot = {}

Es = ks*Eo
Eox = kox*Eo


# plotting_graph
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.35, right=0.95)


plt.title(r'$ \psi_S $ Vs Vcb graph for pMOS')
plt.ylim(0, 3)
plt.xlim(-1.75, 0)
plt.minorticks_on()
plt.tick_params(direction="in")


graph_plot[count] = plt.plot(V_list[count], Y_list[count], color='r', label="")


plt.xlabel('Vcb value')
plt.ylabel(r'$ \psi_S $ value')

# plt.legend()


# button function for adding plots
def setValue(val):
    global count, colour_count, colours, Qox, Vgb
    count = count+1

    # initial list declaration
    Y_list[count] = []
    V_list[count] = []
    graph_plot[count] = []

    # initial calculations
    r = []
    Po = (Ni**2)/ND
    No = ND
    Shi_F = Phi_t*log((ND)/(Ni))

    Cox = Eox/tox
    Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
    gm = (sqrt(2*q*Es*ND))/(Cox)
    f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2

    # Vcb range
    for i in drange(0.01, 1.75, 0.05):
        r.append(i)

    for Vcb in r:
        if abs(Vgb) > abs(Vfb):
            n = -(2*Shi_F+Phi_t*6 + Vcb)
            x0 = max(f, n)  # initial value of NewtonRaphson
            print("x0 is", x0, f, n, Vfb, Vgb)
            val = newtonRaphson(Vgb, x0, Vfb, NA, ND, Phi_t,
                                q, Es, Cox, No, Po, Vcb)

            V_list[count].append(-Vcb)
            Y_list[count].append(abs(val))
        else:
            print("Vgb is less than Vfb")

    colour_count = colour_count+1

    # redrawing the graphs for different parameter value
    plt.axes()
    plt.title(r'$ \psi_S $ Vs Vcb graph')
    plt.ylim(0, 3)
    plt.xlim(-1.75, 0)
    plt.minorticks_on()
    plt.tick_params(direction="in")

    plt.xlabel('Vcb value')
    plt.ylabel(r'$ \psi_S $ value')

    graph_plot[count], = plt.plot(
        V_list[count], Y_list[count], color=colours[colour_count], label="Graph: "+str(count))

    plt.legend()


def val_update_Vgb(val):
    global tox, NA, Phi_m, count, Qox, Vgb

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []
        Vgb = -slider1.val
        # initial calculations
        r = []
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)
        f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2

        # Vcb range
        for i in drange(0.01, 1.75, 0.05):
            r.append(i)

        for Vcb in r:
            if abs(Vgb) > abs(Vfb):
                n = -(2*Shi_F+Phi_t*6 + Vcb)
                x0 = max(f, n)  # initial value of NewtonRaphson
                print("x0 is", x0, f, n)
                val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                    Phi_t, q, Es, Cox, No, Po, Vcb)

                V_list[count].append(-Vcb)
                Y_list[count].append(abs(val))
            else:
                print("Vgb is less than Vfb")

        # redrawing the graphs for different parameter value
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Tox
def val_update_tox(val):
    global tox, NA, Phi_m, count, Qox, Vgb

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []
        tox = (slider2.val)*10**(-9)
        # initial calculations
        r = []
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)
        f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2

        # Vcb range
        for i in drange(0.01, 1.75, 0.05):
            r.append(i)

        for Vcb in r:
            if abs(Vgb) > abs(Vfb):
                n = -(2*Shi_F+Phi_t*6 + Vcb)
                x0 = max(f, n)  # initial value of NewtonRaphson
                val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                    Phi_t, q, Es, Cox, No, Po, Vcb)

                V_list[count].append(-Vcb)
                Y_list[count].append(abs(val))
            else:
                print("Vgb is less than Vfb")

        # redrawing the graphs for different parameter value
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of NA
def val_update_ND(val):
    global tox, NA, Phi_m, count, Qox, Vgb

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []
        ND = (slider3.val)*10**23
        # initial calculations
        r = []
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)
        f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2

        # Vcb range
        for i in drange(0.01, 1.75, 0.05):
            r.append(i)

        for Vcb in r:
            if abs(Vgb) > abs(Vfb):
                n = -(2*Shi_F+Phi_t*6 + Vcb)
                x0 = max(f, n)  # initial value of NewtonRaphson
                val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                    Phi_t, q, Es, Cox, No, Po, Vcb)

                V_list[count].append(-Vcb)
                Y_list[count].append(abs(val))
            else:
                print("Vgb is less than Vfb")

        # redrawing the graphs for different parameter value
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Phi_m
def val_update_Phi(val):
    global tox, NA, Phi_m, count, Qox, Vgb

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []
        Phi_m = slider4.val
        # initial calculations
        r = []
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)
        f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2

        # Vcb range
        for i in drange(0.01, 1.75, 0.05):
            r.append(i)

        for Vcb in r:
            if abs(Vgb) > abs(Vfb):
                n = -(2*Shi_F+Phi_t*6 + Vcb)
                x0 = max(f, n)  # initial value of NewtonRaphson
                val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                    Phi_t, q, Es, Cox, No, Po, Vcb)

                V_list[count].append(-Vcb)
                Y_list[count].append(abs(val))
            else:
                print("Vgb is less than Vfb")

        # redrawing the graphs for different parameter value
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Qox
def val_update_Qox(val):
    global tox, NA, Phi_m, count, Qox, Vgb

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []
        Qox = (slider5.val)*10**(-6)
        # initial calculations
        r = []
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/(Cox)
        f = -(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb)**2

        # Vcb range
        for i in drange(0.01, 1.75, 0.05):
            r.append(i)

        for Vcb in r:
            if abs(Vgb) > abs(Vfb):
                n = -(2*Shi_F+Phi_t*6 + Vcb)
                x0 = max(f, n)  # initial value of NewtonRaphson
                val = newtonRaphson(Vgb, x0, Vfb, NA, ND,
                                    Phi_t, q, Es, Cox, No, Po, Vcb)

                V_list[count].append(-Vcb)
                Y_list[count].append(abs(val))
            else:
                print("Vgb is less than Vfb")

        # redrawing the graphs for different parameter value
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# button_declaration
axButton = plt.axes([0.83, 0.10, 0.06, 0.06])  # xloc,yloc,width,heights
btn = Button(axButton, ' ADD ')


# button on click callback function
btn.on_clicked(setValue)


# Sliders declaration
axSlider1 = plt.axes([0.1, 0.21, 0.55, 0.02])  # xloc,yloc,width,height
slider1 = Slider(axSlider1, 'Vgb', valmin=1, valmax=2.5, valinit=-
                 Vgb, valfmt='Vgb is '+'-'+'%1.2f'+' V', color="blue")


axSlider2 = plt.axes([0.1, 0.17, 0.55, 0.02])  # xloc,yloc,width,height
slider2 = Slider(ax=axSlider2, label='Tox', valmin=1, valmax=8,
                 valinit=tox*10**(9), valfmt='tox is '+'%1.2f' + ' nm', color="green")


axSlider3 = plt.axes([0.1, 0.13, 0.55, 0.02])  # xloc,yloc,width,height
slider3 = Slider(axSlider3, 'ND', valmin=1, valmax=100, valinit=ND /
                 (10**22), valfmt='ND is '+'%1.2f' + ' *10**22 m^-3')


axSlider4 = plt.axes([0.1, 0.09, 0.55, 0.02])  # xloc,yloc,width,height
slider4 = Slider(axSlider4, r'$\phi_m$', valmin=3.5, valmax=4.5,
                 valinit=Phi_m, valfmt=r'$\phi_m$ is '+'%1.2f', color="red")


axSlider5 = plt.axes([0.1, 0.04, 0.55, 0.02])  # xloc,yloc,width,height
slider5 = Slider(axSlider5, 'Qox', valmin=1, valmax=1000, valinit=Qox *
                 10**6, valfmt='Qox is '+'%1.2f'+'*10^(-6)' +' C/m^2', color="yellow")


# sliders on change function call
slider1.on_changed(val_update_Vgb)
slider2.on_changed(val_update_tox)
slider3.on_changed(val_update_ND)
slider4.on_changed(val_update_Phi)
slider5.on_changed(val_update_Qox)

plt.show()


print("Thank you for using the tool \n")
