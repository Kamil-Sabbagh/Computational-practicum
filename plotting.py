from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib


def plotMethods(exact, euler, improved, runge_kutta, f, a, dataPlot, x0, X):
    a.clear()
    a.grid()
    a.set_xlabel('X', fontsize = 5)
    a.set_ylabel('Y', fontsize = 5)

    line1, = a.plot(exact[0], exact[1], linewidth = 0.7)
    line2, = a.plot(euler[0], euler[1], linewidth = 0.7)
    line3, = a.plot(improved[0], improved[1], linewidth = 0.7)
    line4, = a.plot(runge_kutta[0], runge_kutta[1], linewidth = 0.7)

    a.legend([line1, line2, line3, line4],
               ['Exact solution', 'Euler method', 'Improved Euler method', 'Runge-Kutta method'], loc=4, prop={'size': 2})
    axes = f.gca()
    axes.set_xlim([x0, X])
    a.tick_params(axis='both', which='major', labelsize=2)
    a.set_xlabel('X', fontsize = 5)
    a.set_ylabel('Y', fontsize = 5)
    a.set_title("Solutions")
    dataPlot.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)

def plotErrors(error1, error2, error3, f, a, exact, dataPlot, x0, X):
    a.clear()
    a.grid()

    err_line1, = a.plot(exact[0], error1, linewidth = 0.7)
    err_line2, = a.plot(exact[0], error2, linewidth = 0.7)
    err_line3, = a.plot(exact[0], error3, linewidth = 0.7)
    a.legend([err_line1, err_line2, err_line3],
                ['Euler method error', 'Improved Euler method error', 'Runge-Kutta method error'],  loc=4, prop={'size': 2})
    axes = f.gca()
    axes.set_xlim([x0, X])
    a.tick_params(axis='both', which='major', labelsize=2)
    a.set_xlabel('X', fontsize = 5)
    a.set_title("Local error")
    dataPlot.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)

def plot_total_errors(error1, error2, error3, f, a, dataPlot, n0, n1):
    a.clear()
    a.grid()


    err_line1, = a.plot(range(n0, n1+1), error1, linewidth = 0.7)
    err_line2, = a.plot(range(n0, n1+1), error2, linewidth = 0.7)
    err_line3, = a.plot(range(n0, n1+1), error3, linewidth = 0.7)
    a.legend([err_line1, err_line2, err_line3],
             ['Euler method', 'Improved Euler method', 'Runge-Kutta method'], loc=2, prop={'size': 2})

    axes = f.gca()
    axes.set_xlim([n0, n1])
    a.tick_params(axis='both', which='major', labelsize=2)
    a.set_xlabel('N', fontsize = 5)
    a.set_title("Total error")
    dataPlot.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)




