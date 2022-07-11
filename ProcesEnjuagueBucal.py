from tkinter import * #libreria para graficos
from tkinter import messagebox
from io import open

def Enjuague():

	root=Tk()
	root.title("Calculo de Fórmula: Enjuague Bucal")
	root.config(width=400,height=600,bg="black")
	root.deiconify()



	"""---------------------FUNCIONES CALCULOS-----------------"""

	def calculo():
		
		
		global num_ingresado
		
		if len(cuadro1.get()) == 0 :
			messagebox.showwarning("Atención","Debe insertar la cantidad de producto a crear")
			root.mainloop()
		else:
			while True:
				try:
					num_ingresado=int(cuadro1.get())
					break
				except ValueError:
					
					return messagebox.showwarning("Atención","No puede ingresar LETRAS para realizar el cálculo.\n Vuelva a intentarlo.")
				
			resultado1=76.213*num_ingresado/100
			resultado2=19.902*num_ingresado/100
			resultado3=3.883*num_ingresado/100
			resultado4=5.825*num_ingresado/100
			resultado5=3.398*num_ingresado/100
			resultado6=2.912*num_ingresado/100


			cuadro2.config(text=round(resultado1))
			cuadro3.config(text=round(resultado2)) 
			cuadro4.config(text=round(resultado3)) 
			cuadro5.config(text=round(resultado4)) 
			cuadro6.config(text=round(resultado5))
			cuadro7.config(text=round(resultado6))
		


	def guardar():

		#guardarCSV()

		if len(cuadro1.get()) == 0:
			messagebox.showwarning("Atención","Debe insertar la cantidad de producto a crear")
			root.mainloop()

		else:	
			num_ingresado=int(cuadro1.get())
			archivo_texto=open("Fórmula Enjuague Bucal de "+str(num_ingresado)+" Gr.txt","w")

			archivo_texto.write("Fórmula Enjuague Bucal\n"+"Cantidad de producto a realizar: "+str(num_ingresado)+" Gr.\n"+
				"Insumos:\n"+
				"Inf.Llantén: "+str(cuadro2.cget("text"))+" Gr.\n"+
				"Glicerina: "+str(cuadro3.cget("text"))+" Gr.\n"+
				"Coñac: "+str(cuadro4.cget("text"))+" Gr.\n"+
				"Eucalpito: "+str(cuadro5.cget("text"))+" Gr.\n"+
				"Menta: "+str(cuadro6.cget("text"))+" Gr.\n"+
				"Bergamota: "+str(cuadro7.cget("text"))+" Gr.\n"

				)
			
			archivo_texto.close()

			messagebox.showinfo("Mensaje","Archivo .txt creado con éxito")

			root.destroy()


	def Borrar():

		cuadro1.delete(0,END)
		cuadro2.config(text="")
		cuadro3.config(text="")
		cuadro4.config(text="")
		cuadro5.config(text="")
		cuadro6.config(text="")
		cuadro7.config(text="")


	def salir():
		root.destroy()
	#----------------------FRAME-----------------------------------

	
	
	
	miFrame=Frame(root)

	miFrame.config(bg="black")
	
	
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

	cuadro6=Label(miFrame)
	cuadro6.grid(row=5,column=1,padx=10,pady=10)
	cuadro6.config(borderwidth=2, relief="groove",bg="white",width=10,justify="right")

	cuadro7=Label(miFrame)
	cuadro7.grid(row=6,column=1,padx=10,pady=10)
	cuadro7.config(borderwidth=2, relief="groove",bg="white",width=10,justify="right")



	#----------------------LABEL---------------------------------------


	label1=Label(miFrame,text="Cantidad de producto a realizar:")
	label1.grid(row=0,column=0,sticky="e", padx=10,pady=10)

	label2=Label(miFrame,text="Inf. Llantén:")
	label2.grid(row=1,column=0,sticky="e", padx=10,pady=10)

	label3=Label(miFrame,text="Glicerina:")
	label3.grid(row=2,column=0,sticky="e", padx=10,pady=10)

	label4=Label(miFrame,text="Coñac:")
	label4.grid(row=3,column=0,sticky="e", padx=10,pady=10)

	label5=Label(miFrame,text="Eucalipto:")
	label5.grid(row=4,column=0,sticky="e", padx=10,pady=10)

	label6=Label(miFrame,text="Menta:")
	label6.grid(row=5,column=0,sticky="e", padx=10,pady=10)

	label7=Label(miFrame,text="Bergamota:")
	label7.grid(row=6,column=0,sticky="e", padx=10,pady=10)

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

	labelGr6=Label(miFrame,text="Gr.")
	labelGr6.grid(row=5,column=3,sticky="e", padx=5,pady=5)

	labelGr7=Label(miFrame,text="Gr.")
	labelGr7.grid(row=6,column=3,sticky="e", padx=5,pady=5)



	#--------------------------BOTONES-----------------------------

	miFrame2=Frame(root)
	miFrame2.config(bg="black")
	miFrame2.pack()

	botonBorrar=Button(miFrame2, text="Borrar Todo", command=Borrar)
	botonBorrar.grid(row=0, column=0,sticky="e", padx=10,pady=10)

	botonGuardar=Button(miFrame2, text="Guardar",command=guardar)
	botonGuardar.grid(row=0, column=2,sticky="e", padx=10,pady=10)

	botonEjecutar=Button(miFrame2, text="Ejecutar",command=calculo)
	botonEjecutar.grid(row=0, column=3,sticky="e", padx=10,pady=10)

	botonSalir=Button(miFrame2, text="Salir", command=salir)
	botonSalir.grid(row=0, column=4,sticky="e", padx=10,pady=10)




	




	root.mainloop()