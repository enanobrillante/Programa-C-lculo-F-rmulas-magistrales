from tkinter import * #libreria para graficos
from tkinter import messagebox
from io import open

def CremaBase():

	root=Tk()
	root.title("Calculadora de Fórmula Crema Base")
	#root.config(width=400,height=600)
	#imagenFondo=PhotoImage(file="PB500px.png")
	#LabelFondo=Label(root,image=imagenFondo)
	#LabelFondo.pack()

	root.deiconify()
	

	"""---------------------FUNCIONES CALCULOS-----------------"""

	def calculo():
		
		
		global num_ingresado
		
		if len(cuadro1.get()) == 0 :
			messagebox.showwarning("Atención","Debe insertar la cantidad de producto a crear")
			root.mainloop()
		else:
			while True:
				root.deiconify()
	
				try:
					num_ingresado=int(cuadro1.get())
					break
				except ValueError:
					
					return messagebox.showwarning("Atención","No puede ingresar LETRAS para realizar el cálculo.\n Vuelva a intentarlo.")
				
	
		resultado1=19.6078*num_ingresado/100
		resultado2=4.901*num_ingresado/100
		resultado3=73.52*num_ingresado/100
		resultado4=1.96*num_ingresado/100

		cuadro2.config(text=round(resultado1))
		cuadro3.config(text=round(resultado2)) 
		cuadro4.config(text=round(resultado3)) 
		cuadro5.config(text=round(resultado4)) 
 

		


	#def guardarCSV():

		#m1=open("Fórmula Crema Masajes de "+str(num_ingresado)+" Gr.csv","w")
		#m1_c=csv.writer(m1)


		#m1.close()

	def guardar():

		#guardarCSV()

		if len(cuadro1.get()) == 0:
			messagebox.showwarning("Atención","Debe insertar la cantidad de producto a crear")
			root.mainloop()

		else:

			valor=messagebox.askquestion("Guardar","¿Desea guardar el cálculo realizado?")
			if valor=="yes":  #evaluamos si el usuario ha pulsado "si"
			
				num_ingresado=int(cuadro1.get())
				archivo_texto=open("Fórmula Crema Masajes de "+str(num_ingresado)+" Gr.txt","w")

				archivo_texto.write("Fórmula Crema Masajes\n"+"Cantidad de producto a realizar: "+str(num_ingresado)+" Gr.\n"+
					"Insumos:\n"+
					"Aceite de oliva: "+str(cuadro2.cget("text"))+" Gr.\n"+
					"Cera lanette: "+str(cuadro3.cget("text"))+" Gr.\n"+
					"Agua destilada: "+str(cuadro4.cget("text"))+" Gr.\n"+
					"Borax: "+str(cuadro5.cget("text"))+" Gr.\n")
			
				archivo_texto.close()

				messagebox.showinfo("Mensaje","Archivo .txt creado con éxito")

				root.destroy()
			

	def Borrar():

		cuadro1.delete(0,END)
		cuadro2.config(text="")
		cuadro3.config(text="")
		cuadro4.config(text="")
		cuadro5.config(text="")

	def salir():
		valor=messagebox.askquestion("Salir","¿Desea salir de cálculo Crema Base?")
		if valor=="yes": #evaluamos si el usuario ha pulsado "si"
			root.destroy()
	#----------------------FRAME-----------------------------------

	miFrame=Frame(root)
	miFrame.pack()
	


	num1=StringVar()
	num_ingresado=int()



	cuadro1=Entry(miFrame,textvariable=num_ingresado)
	cuadro1.grid(row=0,column=1,padx=0,pady=0)
	cuadro1.config(justify="right",width=12)

	cuadro2=Label(miFrame)
	cuadro2.grid(row=1,column=1,padx=10,pady=10)
	cuadro2.config(borderwidth=2, relief="groove",bg="white",width=10,justify="right")

	cuadro3=Label(miFrame)
	cuadro3.grid(row=2,column=1,padx=10,pady=10)
	cuadro3.config(borderwidth=2, relief="groove",bg="white",width=10,justify="right")

	cuadro4=Label(miFrame)
	cuadro4.grid(row=3,column=1,padx=10,pady=10)
	cuadro4.config(borderwidth=2, relief="groove",bg="white",width=10,justify="right")

	cuadro5=Label(miFrame)
	cuadro5.grid(row=4,column=1,padx=10,pady=10)
	cuadro5.config(borderwidth=2, relief="groove",bg="white",width=10,justify="right")

	#----------------------LABEL---------------------------------------


	label1=Label(miFrame,text="Cantidad de producto a realizar:")
	label1.grid(row=0,column=0,sticky="e", padx=10,pady=10)

	label2=Label(miFrame,text="Aceite Oliva:")
	label2.grid(row=1,column=0,sticky="e", padx=10,pady=10)

	label3=Label(miFrame,text="Cera lanette:")
	label3.grid(row=2,column=0,sticky="e", padx=10,pady=10)

	label4=Label(miFrame,text="Agua Destilada:")
	label4.grid(row=3,column=0,sticky="e", padx=10,pady=10)

	label5=Label(miFrame,text="Borax:")
	label5.grid(row=4,column=0,sticky="e", padx=10,pady=10)

	labelGr1=Label(miFrame,text="Gr.")
	labelGr1.grid(row=0,column=3,sticky="e", padx=5,pady=5)

	labelGr2=Label(miFrame,text="Gr.")
	labelGr2.grid(row=1,column=3,sticky="e", padx=5,pady=5)

	labelGr3=Label(miFrame,text="Gr.")
	labelGr3.grid(row=2,column=3,sticky="e", padx=5,pady=5)

	labelGr4=Label(miFrame,text="Gr.")
	labelGr4.grid(row=3,column=3,sticky="e", padx=5,pady=5)

	labelGr5=Label(miFrame,text="Gr.")
	labelGr5.grid(row=4,column=3,sticky="e", padx=5,pady=5)



	#--------------------------BOTONES-----------------------------

	miFrame2=Frame(root)
	miFrame2.pack()


	botonBorrar=Button(miFrame2, text="Borrar Todo", command=Borrar)
	botonBorrar.grid(row=0, column=0,sticky="e", padx=10,pady=10)
	botonBorrar.config(cursor="hand2")

	botonGuardar=Button(miFrame2, text="Guardar",command=guardar)
	botonGuardar.grid(row=0, column=2,sticky="e", padx=10,pady=10)
	botonGuardar.config(cursor="hand2")

	botonEjecutar=Button(miFrame2, text="Ejecutar",command=calculo)
	botonEjecutar.grid(row=0, column=3,sticky="e", padx=10,pady=10)
	botonEjecutar.config(cursor="hand2")

	botonSalir=Button(miFrame2, text="Salir", command=salir)
	botonSalir.grid(row=0, column=4,sticky="e", padx=10,pady=10)
	botonSalir.config(cursor="hand2")




	resultado=0




	root.mainloop()