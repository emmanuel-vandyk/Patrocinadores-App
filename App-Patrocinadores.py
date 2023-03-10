from tkinter import *


#### SET ROOT ####
root = Tk()
root.title("App de patrocinadores")
root.tk_setPalette("darkgrey")
root.geometry("680x740+400+30")

#Background ROOT
backgnd = PhotoImage(file="iconos/banner_sponsors2.png")
label_bg = Label(root, image=backgnd).place(x=0, y=0)

#Icono App
root.iconbitmap("iconos/ea.ico")

#FUNCIONES

def seleccionar():
    monitor.config(text=f"{opcion.get()}")

def reiniciar():
    opcion.set("")
    monitor.config(text="Selecciona un sponsor")
    monitor.tk_setPalette("darkgrey")


#Variable para darle funcionalidad a los botones
opcion = StringVar()
opcion.set("")

#Seleccion de sponsor
monitor = Label(root, text="Selecciona un sponsor")
monitor.pack(anchor=N, pady=20)
monitor.config(font=("Cambria", 36, "bold"))

#Logos de patrocinadores
img1 = PhotoImage(file="iconos/adidas_64x64.png")
img2 = PhotoImage(file="iconos/puma_64x64.png")
img3 = PhotoImage(file="iconos/nike_64x64.png")
img4 = PhotoImage(file="iconos/topper.png")
img5 = PhotoImage(file="iconos/umbro_64x64.png")
img6 = PhotoImage(file="iconos/under-armour.png")


# Radio Buttons
rb1 = Radiobutton(root, value='Adidas', variable=opcion, command=seleccionar, indicatoron=0, image=img1, textvariable=backgnd)
rb1.pack(anchor=CENTER, pady=10)

rb2 = Radiobutton(root, value='Puma', variable=opcion, command=seleccionar, indicatoron=0, image=img2)
rb2.pack(anchor=CENTER, pady=10)

rb3 = Radiobutton(root, value='Nike', variable=opcion, command=seleccionar, indicatoron=0, image=img3)
rb3.pack(anchor=CENTER, pady=10)

rb4 = Radiobutton(root, value='Topper', variable=opcion, command=seleccionar, indicatoron=0, image=img4)
rb4.pack(anchor=CENTER, pady=10)

rb5 = Radiobutton(root, value='Umbro', variable=opcion, command=seleccionar, indicatoron=0, image=img5)
rb5.pack(anchor=CENTER, pady=10)


rb6 = Radiobutton(root, value='Under Armour', variable=opcion, command=seleccionar, indicatoron=0, image=img6)
rb6.pack(anchor=CENTER, pady=10)


#Boton de reinicio
btn_reeboot = Radiobutton(root, text="Reiniciar", command=reiniciar, font="Cambria 18", indicatoron=0, fg="white", selectcolor="black").pack(anchor=CENTER, pady=20)

root.mainloop()