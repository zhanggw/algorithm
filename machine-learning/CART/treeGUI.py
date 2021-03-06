from numpy import *

from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure

import cart

def reDraw(tolS,tolN):
    pass


def drawNewTree():
    pass


if __name__ == '__main__':
    root = Tk()

    reDraw.f = Figure(figsize=(5,4), dpi=100)
    reDraw.canvas = FigureCanvasTkAgg(reDraw.f, master=root)
    reDraw.canvas.show()
    reDraw.canvas.get_tk_widget().grid(row=0, columnspan=3)

    # Label(root, text = "Plot place holder").grid(row=0, columnspan=3)
    Label(root, text = "tolN").grid(row=1, column=0)
    tolNentry = Entry(root)
    tolNentry.grid(row=1,column=1)
    tolNentry.insert(0, '10')
    Label(root, text="tolS").grid(row=2, column=0)
    tolSentry = Entry(root)
    tolSentry.grid(row=2, column=1)
    tolSentry.insert(0, '1.0')
    Button(root, text='reDraw',command=drawNewTree).grid(row=1,column=2,rowspan=3)
    chkBtnVar = IntVar()
    chkBtn = Checkbutton(root, text="Model Tree", variable=chkBtnVar)
    chkBtn.grid(row=3, column=0, columnspan=2)

    reDraw.rawDat = cart.loadDataSet('sine.txt')
    reDraw.testDat = arange(min(reDraw.rawDat[:,0]), max(reDraw.rawDat[:,0]), 0.01)
    reDraw(1.0, 10)

    root.mainloop()


