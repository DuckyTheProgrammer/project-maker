from tkinter import *
from PIL import Image, ImageTk

rootapp = Tk()
rootapp.title("Application")

#functions


def changeLang():
    changelangroot = Toplevel(rootapp)
    changelangroot.title("Choose Language")

    def kalanchosen():
        labeltext = "Chosen Language: Georgian"
        chosenlang.config(text=labeltext)
        createButton.configure(state=NORMAL)
        changelangroot.destroy()

    def enlanchosen():
        labeltext = "Chosen Language: English"
        chosenlang.config(text=labeltext)
        createButton.configure(state=NORMAL)
        changelangroot.destroy()

    def rulanchosen():
        labeltext = "Chosen Language: Russian"
        chosenlang.config(text=labeltext)
        createButton.configure(state=NORMAL)
        changelangroot.destroy()



    #Frames
    
    chlancanvas = Canvas(changelangroot,  width=300, height=200, bg="#262D42")
    chlancanvas.pack()

    chlanframe = Frame(chlancanvas, bg="white")
    chlanframe.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.9)

    #Buttons

    kalan = Button(chlancanvas,text="GEORGIAN", font=("Havinec", 17), command=kalanchosen)
    kalan.place(rely=0.2, relx=0.09, relwidth=0.8, relheight=0.15)

    enlan = Button(chlancanvas,text="ENGLISH", font=("Havinec", 17), command=enlanchosen)
    enlan.place(rely=0.4, relx=0.09, relwidth=0.8, relheight=0.15)

    rulan = Button(chlancanvas,text="RUSSIAN", font=("Havinec", 17), command=rulanchosen)
    rulan.place(rely=0.6, relx=0.09, relwidth=0.8, relheight=0.15)


def createproject():
    text = chosenlang['text']
    if text == "Chosen Language: Georgian":
        print("[STATUS] Client has chosen Georgian Lnaguage")
        karoot = Toplevel(rootapp)
        karoot.title("KA v0.1")

    elif text == "Chosen Language: English":
        print("[STATUS] Client has chosen English Lnaguage")

    elif text == "Chosen Language: Russian":
        print("[STATUS] Client has chosen Russian Lnaguage")

#App design

canvas = Canvas(rootapp, width=350, height=600, bg="#262D42")
canvas.pack()   

mainframe = Frame(canvas, bg="white")
mainframe.place(relx=0.075, rely=0.15, relheight=0.75, relwidth=0.85)

detailframe = Frame(canvas, bg="white")
detailframe.place(relx=0.075, rely=0.11, relheight=0.001, relwidth=0.85)

titletext = Label(canvas, text="MENU", bg="#262D42", fg="white", font=("Courier", 35))
titletext.place(relx=0.065, rely=0.035)

titletext2 = Label(canvas, text="(Project Creator)", bg="#262D42", fg="white", font=("Courier", 13))
titletext2.place(relx=0.32, rely=0.061)

versionetext = Label(canvas, text="v 0.1 [BETA]", bg="#262D42", fg="white", font=("Courier", 12, "italic"))
versionetext.place(relx=0.65, rely=0.1)

btnLabel = Button(mainframe,text="CHOOSE LANGUAGE", font=("Havinec", 17), command=changeLang)
btnLabel.place(rely=0.1, relx=0.09, relwidth=0.8, relheight=0.07)

createButton = Button(mainframe,text="CREATE PROJECT", font=("Havinec", 17), state=DISABLED, command=createproject)
createButton.place(rely=0.2, relx=0.09, relwidth=0.8, relheight=0.07)

chosenlang = Label(mainframe, text="Chosen Language: None", font=("Havinec", 17))
chosenlang.place(rely=0.8, relx=0.09, relwidth=0.8, relheight=0.07)



rootapp.mainloop()