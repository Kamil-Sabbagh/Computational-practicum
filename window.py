from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *

from plotting import *
from methods import *

def input():
    x0 = float(x0_entry.get())
    y0 = float(y0_entry.get())
    X = float(X_entry.get())
    n = int(n_entry.get())
    n0 = int(N0_entry.get())
    n1 = int(N1_entry.get())

    exact = exact_solution(x0, y0, X, n)
    euler = euler_method(x0, y0, X, n)
    improved = improved_euler_method(x0, y0, X, n)
    runge_kutta = runge_kutta_method(x0, y0, X, n)

    error1 = compute_error(exact[1], euler[1])
    error2 = compute_error(exact[1], improved[1])
    error3 = compute_error(exact[1], runge_kutta[1])

    g_error = global_error(x0, y0, X, n0, n1)

    plotMethods(exact, euler, improved, runge_kutta, f1, a, dataPlot1, x0, X)
    plotErrors(error1, error2, error3, f1, a2, exact, dataPlot1, x0, X)
    plot_total_errors(g_error[0], g_error[1], g_error[2], f1, a3, dataPlot1, n0, n1)

master = Tk()

f_top = Frame()
f_mid = Frame()
f_bot = Frame()
master.title("Computational methods")

x0_entry = Entry(f_top, width=15)
y0_entry = Entry(f_top, width=15)
X_entry = Entry(f_top, width=15)
n_entry = Entry(f_top, width=15)
N0_entry = Entry(f_top, width=15)
N1_entry = Entry(f_top, width=15)

x0_label = Label(f_mid, width=15, text = "enter x0")
y0_label = Label(f_mid, width=15, text = "enter y0")
X_label = Label(f_mid, width=15, text = "enter X")
n_label = Label(f_mid, width=15, text = "enter n")
N0_label =  Label(f_mid, width=15, text = "enter N0")
N1_label = Label(f_mid, width=15, text = "enter N1")

button = Button(f_bot, width=90, text="Submit", command=input)

f_top.pack()
f_mid.pack()
f_bot.pack()

x0_entry.pack(side=LEFT)
y0_entry.pack(side=LEFT)
X_entry.pack(side=LEFT)
n_entry.pack(side=LEFT)
N0_entry.pack(side=LEFT)
N1_entry.pack(side=LEFT)

x0_label.pack(side=LEFT)
y0_label.pack(side=LEFT)
X_label.pack(side=LEFT)
n_label.pack(side=LEFT)
N0_label.pack(side=LEFT)
N1_label.pack(side=LEFT)
button.pack()

f1 = Figure(figsize=(2,2), dpi=300)
a = f1.add_subplot(131)
a2 = f1.add_subplot(132)
a3 = f1.add_subplot(133)

dataPlot1 = FigureCanvasTkAgg(f1, master=master)
master.geometry('1200x800')
master.mainloop()
