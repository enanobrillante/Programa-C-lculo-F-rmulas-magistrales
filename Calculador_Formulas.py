from tkinter import * #libreria para graficos
from tkinter import messagebox
from ProcesCremaBase import CremaBase
from ProcesEnjuagueBucal import Enjuague

 

root=Tk()
root.title("Programa para calcular Fórmulas Magistrales")
root.resizable(False,False)
#root.geometry("500x360+459+200")
root.iconbitmap("PB.ico")
#root.config(bg="black")

imagenFondoPrincipal=PhotoImage(file="PB500px.png")
labelfondoPrincipal=Label(root,image=imagenFondoPrincipal)
labelfondoPrincipal.pack()


miFrame=Frame(root)
miFrame.pack(expand=False)
#miFrame.config(bg="black")
#miFrame.pack()





#------------------Funciones----------------------------




def cerrarPrograma():

	valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
	if valor=="yes": #evaluamos si el usuario ha pulsado "si"
		root.destroy()
		

def acercade():

	messagebox.showinfo("Calculador de Fórmulas 2018","Creador: Tissone Mauro\nProducto bajo licencia de\n Ponte Bonita 2018")



barraMenu=Menu(root)
root.config(menu=barraMenu,width=100,height=50)
     

#-----------------elementos del menu--------------------

ArchivoMenu=Menu(barraMenu, tearoff=0)
CremaMenu=Menu(barraMenu, tearoff=0)
AceiteMenu=Menu(barraMenu,tearoff=0)
OleatoMenu=Menu(barraMenu,tearoff=0)
DentalMenu=Menu(barraMenu,tearoff=0)
ExfoMenu=Menu(barraMenu,tearoff=0)
TonicoMenu=Menu(barraMenu,tearoff=0)
Acercade=Menu(barraMenu,tearoff=0)


#--------------------------------------------------------

barraMenu.add_cascade(label="Archivo", menu=ArchivoMenu)
barraMenu.add_cascade(label="Cremas", menu=CremaMenu)
barraMenu.add_cascade(label="Aceites", menu=AceiteMenu)
barraMenu.add_cascade(label="Oleátos", menu=OleatoMenu)
barraMenu.add_cascade(label="Cuidado_dental", menu=DentalMenu)
barraMenu.add_cascade(label="Exfoliantes", menu=ExfoMenu)
barraMenu.add_cascade(label="Tónicos", menu=TonicoMenu)
barraMenu.add_command(label="Acerca de...",command=acercade)


ArchivoMenu.add_command(label="Abrir")
ArchivoMenu.add_command(label="Guardar")
ArchivoMenu.add_command(label="Guardar como...")
ArchivoMenu.add_command(label="Imprimir")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label="Salir",command=cerrarPrograma)


CremaMenu.add_command(label="Crema base",command=CremaBase)
CremaMenu.add_command(label="Crema para manos")
CremaMenu.add_command(label="Crema facial")
CremaMenu.add_command(label="Crema corporal")


AceiteMenu.add_command(label="Aceite base")
AceiteMenu.add_command(label="Aceite Limón")
AceiteMenu.add_command(label="Aceite Lavanda")
AceiteMenu.add_command(label="Aceite Romero")

OleatoMenu.add_command(label="Óleo uñas")
OleatoMenu.add_command(label="Óleo Escencial(Alegría)")
OleatoMenu.add_command(label="Óleo facial")


DentalMenu.add_command(label="Pasta Dental")
DentalMenu.add_command(label="Enjuague bucal",command=Enjuague)

#--------------------------------------------------------------------




root.mainloop()
