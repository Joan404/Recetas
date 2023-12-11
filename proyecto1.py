from tkinter import *
from tkinter import ttk


main= Tk()

main.title("Raku")
main.config(bg="Tan1")
main.minsize(450,500)
main.maxsize(450,500)





top_frame = Frame(main,bd=2,relief=FLAT)
left_frame = Frame(main,bd=1,relief=FLAT)
right_frame = Frame(main,bd=1,relief=FLAT)


top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)


top_frame_lbl = Label(top_frame,font=("Verdana",40),text="Recetas",fg="Black",bg="Tan1",relief=FLAT)
top_frame_lbl.pack()

caracteristicas_frame = Frame(left_frame,bd=1,relief=RAISED,bg="burlywood2")
caracteristicas_frame.pack()

caracteristicas_frame_lbl = Label(caracteristicas_frame,font=("Verdana",30),text="Caracteristicas",bg="burlywood",fg="Black",relief=FLAT)
caracteristicas_frame_lbl.pack(side=TOP)

# dias_frame=Frame(right_frame,bd=1,relief=RAISED)
# dias_frame.pack()


# # dias_lbl= Label(dias_frame,font=("Verdana",30),text="Dias",fg="Black")
# # dias_lbl.pack()


#BOTON GENERADOR


def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Receta semanal")
    ventana_secundaria.config(width=300, height=200)
    
generador= Button(caracteristicas_frame,bg="Tan1",fg="Black",text="Generar menú semanal",font=("Verdana",28),command=abrir_ventana_secundaria,state= DISABLED)
generador.pack(side=BOTTOM)

def activar_boton():
    generador.config(state=ACTIVE,bg="Tan1",fg="Black")
    
#BOTONES DE CARACTERISTICAS


value=0

option = IntVar()



boton1=Radiobutton(caracteristicas_frame, text="Vegano", variable=option,command=activar_boton,bg="burlywood2",
            value=1,font=("Verdana",28)).pack(anchor=W)
boton2=Radiobutton(caracteristicas_frame, text="Vegetariano", variable=option,command=activar_boton,bg="burlywood2",
            value=2,font=("Verdana",28)).pack(anchor=W)
boton3=Radiobutton(caracteristicas_frame, text="Sin Lactosa", variable=option,command=activar_boton,bg="burlywood2",
            value=3,font=("Verdana",28)).pack(anchor=W)
boton4=Radiobutton(caracteristicas_frame, text="Gluten-Free", variable=option,command=activar_boton,bg="burlywood2",
            value=4,font=("Verdana",28)).pack(anchor=W)
boton5=Radiobutton(caracteristicas_frame, text="Todo", variable=option,command=activar_boton,bg="burlywood2",
            value=5,font=("Verdana",28)).pack(anchor=W)



main.mainloop()


