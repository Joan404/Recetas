from tkinter import *



main= Tk()

main.title("Proyecto")
main.config(bg="Brown1")



top_frame = Frame(main,bd=2,relief=FLAT)
left_frame = Frame(main,bd=1,relief=FLAT)
right_frame = Frame(main,bd=1,relief=FLAT)


top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)


top_frame_lbl = Label(top_frame,font=("Verdana",40),text="Recetas",fg="DarkSlateGray")
top_frame_lbl.pack()

caracteristicas_frame = Frame(left_frame,bd=1,relief=FLAT)
caracteristicas_frame.pack()

caracteristicas_frame_lbl = Label(caracteristicas_frame,font=("Verdana",30),text="Caracteristicas",fg="Black")
caracteristicas_frame_lbl.pack(side=TOP)

dias_frame=Frame(right_frame,bd=1,relief=FLAT)
dias_frame.pack()


dias_lbl= Label(dias_frame,font=("Verdana",30),text="Dias",fg="Black")
dias_lbl.pack()




#BOTONES DE CARACTERISTICAS


value=1



boton1=Radiobutton(caracteristicas_frame, text="Vegano", 
            value=1,font=("Verdana",28)).pack(anchor=W)
boton2=Radiobutton(caracteristicas_frame, text="Vegetariano", 
            value=2,font=("Verdana",28)).pack(anchor=W)
boton3=Radiobutton(caracteristicas_frame, text="Sin Lactosa",   
            value=3,font=("Verdana",28)).pack(anchor=W)
boton4=Radiobutton(caracteristicas_frame, text="Gluten-Free",
            value=4,font=("Verdana",28)).pack(anchor=W)
boton5=Radiobutton(caracteristicas_frame, text="Todo",   
            value=5,font=("Verdana",28)).pack(anchor=W)


#BOTONES DIAS


value=2

lunes= Radiobutton(dias_frame, text="Lunes", 
            value=1,font=("Verdana",28)).pack(anchor=W)
martes= Radiobutton(dias_frame, text="Martes", 
            value=2,font=("Verdana",28)).pack(anchor=W)
miercoles= Radiobutton(dias_frame, text="Miercoles",   
            value=3,font=("Verdana",28)).pack(anchor=W)
jueves= Radiobutton(dias_frame, text="Jueves",
            value=4,font=("Verdana",28)).pack(anchor=W)
viernes= Radiobutton(dias_frame, text="Viernes",   
            value=5,font=("Verdana",28)).pack(anchor=W)
sabado= Radiobutton(dias_frame, text="Sabado",   
            value=6,font=("Verdana",28)).pack(anchor=W)
domingo= Radiobutton(dias_frame, text="Domingo",   
            value=7,font=("Verdana",28)).pack(anchor=W)


main.mainloop()


