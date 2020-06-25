from tkinter import *
from tkinter import ttk

def main():
    # gui
    window = Tk()
    window.title("program")
    # centering
    pw= 1100
    ph = 300
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    window.geometry("%dx%d+%d+%d"%(pw, ph, (sw-pw)/2, (sh-ph)/2))
    window.resizable(False, False)

    window.mainloop()


if __name__ == "__main__":
    main()