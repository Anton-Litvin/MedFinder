from tkinter import *
from tkinter import ttk
#import tkVideoPlayer

def createTablo():
    def fullscreenOut(event):
        root.attributes("-fullscreen", False)
    def fullscreenIn(event):
        root.attributes("-fullscreen", True)
    #Создание и разметка окна
    root = Tk()
    root.title("Tablo")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    resolution = str(width)+"x"+str(height)
    root.geometry(resolution+"0"+"0") #1900x1080
    root.attributes("-fullscreen", True)
    for r in range(2): root.rowconfigure(index=r, weight=1)
    for c in range(2): root.columnconfigure(index=c, weight=1)

    #Создание и разметка информационной панели
    dataFrame = ttk.Frame(borderwidth=1,
                    relief=SOLID,
                    height=height,
                    width=width-960,
                    padding=[0, 0, 0, 0]
                    )
    dataFrame.grid_propagate(False)
    for r in range(6): dataFrame.rowconfigure(index=r, weight=1)
    for c in range(3): dataFrame.columnconfigure(index=c, weight=1)

    #Создание массивов переменных
    clientList = []
    clientStatus = []
    clientWindows = []
    for i in range(5):
        NumTab = StringVar()
        NumTab.set("")
        Pr = StringVar()
        Id = StringVar()
        Id.set("--")
        clientList.append(NumTab)
        clientStatus.append(Pr)
        clientWindows.append(Id)

    #Ввод начальных значений
    for r in range(6):
        for c in range(3):
            if c == 0:
                if r == 0:
                    client = ttk.Label(dataFrame,
                                text="Клиент",
                                anchor=CENTER,
                                font=("Arial", 60),
                                background="#1266B1",
                                foreground="#FFFFFF",
                                borderwidth=1,
                                #relief=SOLID
                                )
                    client.grid(row=r, column=c,
                                ipadx=6, ipady=6,
                                padx=0, pady=0,
                                sticky=NSEW)
                else:
                    client = ttk.Label(dataFrame,
                                        textvariable=clientList[r-1],
                                        anchor=CENTER,
                                        font=("Arial", 60),
                                        background="#1266B1",
                                        foreground="#FFFFFF", #"#1286B1",
                                        borderwidth=1,
                                        #relief=SOLID
                                        )
                    client.grid(row=r, column=c,
                                ipadx=6, ipady=6,
                                padx=0, pady=0,
                                sticky=NSEW)
            elif c== 1:
                if r == 0:
                    status = ttk.Label(dataFrame,
                                        font=("Arial", 60),
                                        background="#1266B1",
                                        foreground="#FFFFFF",
                                        borderwidth=1,
                                        #relief=SOLID
                                        )
                    status.grid(row=r, column=c,
                            ipadx=6, ipady=6,
                            padx=0, pady=0,
                            sticky=NSEW)
                else:
                    status = ttk.Label(dataFrame,
                                        textvariable=clientStatus[r-1],
                                        font=("Arial", 60),
                                        background="#1266B1",
                                        foreground="#FFFFFF", #"#1286B1",
                                        borderwidth=1,
                                        #relief=SOLID
                                        )
                    status.grid(row=r, column=c,
                            ipadx=6, ipady=6,
                            padx=0, pady=0,
                            sticky=NSEW)
            elif c == 2:
                if r == 0:
                    window = ttk.Label(dataFrame,
                                text="Окно",
                                anchor=CENTER,
                                font=("Arial", 60),
                                background="#1266B1",
                                foreground="#FFFFFF",
                                borderwidth=1,
                                #relief=SOLID
                                )
                    window.grid(row=r, column=c,
                                    ipadx=6, ipady=6,
                                    padx=0, pady=0,
                                    sticky=NSEW)
                else:
                    window = ttk.Label(dataFrame,
                                textvariable=clientWindows[r-1],
                                anchor=CENTER,
                                font=("Arial", 60),
                                background="#1266B1",
                                foreground="#FFFFFF", #"#1286B1",
                                borderwidth=1,
                                #relief=SOLID
                                )
                    window.grid(row=r, column=c,
                                    ipadx=6, ipady=6,
                                    padx=0, pady=0,
                                    sticky=NSEW)

    dataFrame.grid(row=0,column=0, rowspan=2) #Вывод информационной панели

    #Создание и вывод QR-кодов
    QRimage = PhotoImage(file="static\QR.png") #QR.png resolution=960x506
    QRcodes = ttk.Label(root, image=QRimage)

    QRcodes.grid(row=1, column=1, sticky=SE)

    root.bind("<KeyPress-F11>", fullscreenOut)
    root.bind("<KeyPress-F12>", fullscreenIn)
    #root.mainloop()
    return (root, clientList, clientStatus, clientWindows)