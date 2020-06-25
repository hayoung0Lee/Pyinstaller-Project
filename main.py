from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#0: not selected, 1: file process, 2: dir process
TYPE = 0 
TARGET=""
STATUS_MESSAGE=""

def main():
    # gui
    window = Tk()
    window.title("program")
    # centering
    pw= 430
    ph = 200
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    window.geometry("%dx%d+%d+%d"%(pw, ph, (sw-pw)/2, (sh-ph)/2))
    window.resizable(False, False)

    def openFile():
        global TYPE
        global TARGET
        global STATUS_MESSAGE

        try: 
            TARGET = filedialog.askopenfilename(initialdir = "D:/", title="파일 선택", filetypes=(("XML","*.xml"),("all files","*.*")))
            if not TARGET: 
                TYPE = 0
                TARGET = ""
                STATUS_MESSAGE.set('파일/폴더를 선택해주세요')
            else:
                TYPE = 1
                STATUS_MESSAGE.set("선택된 파일:%s"%TARGET)
        except: 
            # error
            pass
        
        
    def openDir():
        global TYPE
        global TARGET
        global STATUS_MESSAGE

        try:
            TARGET = filedialog.askdirectory(initialdir = "D:/", title="폴더 선택")
            if not TARGET: 
                    TYPE = 0
                    TARGET = ""
                    STATUS_MESSAGE.set('파일/폴더를 선택해주세요')
            else:
                TYPE = 2
                STATUS_MESSAGE.set("선택된 폴더:%s"%TARGET)
        except: 
            # error
            pass

        
    # 버튼
    fileWindow = ttk.Button(window, text="파일 선택", width=20, command=openFile)
    fileWindow.place(x=50, y=30)
    dirWindow = ttk.Button(window, text="폴더 선택", width=20, command=openDir)
    dirWindow.place(x=220, y=30)

    processBtn = ttk.Button(window, text="처리 하기", width=20, )
    processBtn.place(x=50, y=80)

    processBtn = ttk.Button(window, text="중단 하기", width=20, )
    processBtn.place(x=220, y=80)

    global TYPE
    global STATUS_MESSAGE
    
    STATUS_MESSAGE = StringVar()
    messageLabel = ttk.Label(window, textvariable=STATUS_MESSAGE)
    messageLabel.place(x=50, y=140)

    TYPE = 0
    STATUS_MESSAGE.set('파일/폴더를 선택해주세요')

    window.mainloop()


if __name__ == "__main__":
    main()