from tkinter import *
i=0
def kliker(event):
    global i
    i+=1
    lbl.configure(text=i)
def kliker_(event):
    global i
    if i>0: i-=1
    lbl.configure(text=i)
def ent_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    #ent.delete(0,END)
    text=var.get()
    ent.insert(END,text)
win=Tk()
win.title("Anastasia Vasard")
win.geometry("600x400")

btn=Button(win,text="Vajuta siia", font="Arial 30", fg="Red", bg="lightblue", width=15, height=3, relief=GROOVE) #SUNKEN) #GROOVE) #RAISED
lbl=Label(win, text="...",width=15, height=3, relief="ridge")
ent=Entry(win,fg="blue",width=15,font="Arial 30")
var=IntVar() #StringVar()
var.set(1)
r1=Radiobutton(win,text="Esimene", variable=var, value=1, font="Arial 30", fg="green", command=valik)
r2=Radiobutton(win,text="Teine", variable=var, value=2, font="Arial 30", fg="green", command=valik)
r3=Radiobutton(win,text="Kolmas", variable=var, value=3, font="Arial 30", fg="green", command=valik)

btn.bind("<Button-1>",kliker)#1km
btn.bind("<Button-3>",kliker_)#pkm
ent.bind("<Return>", ent_to_lbl)#Enter
lbl.pack()
btn.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
win.mainloop()