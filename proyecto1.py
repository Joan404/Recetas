from tkinter import *
from tkinter import ttk
import connection


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

#BOTON GENERADOR

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


# VENTANA SECUNDARIA

conn = connection.connect()
cur = conn.cursor(buffered=True)

def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Receta semanal")
    ventana_secundaria.config(width=300, height=200)

    if option.get() == 1:
        condition = 'AND vegan = 1'
    elif option.get() == 2:
        condition = 'AND vegetarian = 1'
    elif option.get() == 3:
        condition = 'AND diaryFree = 1'
    elif option.get() == 4:
        condition = 'AND glutenFree = 1'
    elif option.get() == 5:
        condition = ''


    listDishes = ['breakfast' ,'main course', 'snack', 'main course']
    listDays = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    dicIds = dict()

    for day in listDays:
        for dish in listDishes:
            cur.execute(f'SELECT id FROM `bbdd` WHERE type = "{dish}" {condition} ORDER BY RAND() LIMIT 1')
            id = cur.fetchall()[0][0]
            if dicIds.get(f'{day}_{dish}'):
                dicIds[f'{day}_{dish}2'] = id
            else:
                dicIds[f'{day}_{dish}'] = id
    # print(dicIds)

    def details(button):
        # print(dicIds[button])
        ventana_detalles = Toplevel()
        ventana_detalles.title("Details")
        ventana_detalles.config(width=300, height=200)

        cur.execute(f'SELECT name FROM `bbdd` WHERE id = {dicIds[button]}')
        name = cur.fetchall()[0][0]
        print(name)

        pass

    button_lunes_main1 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('lunes_main course'))
    button_martes_main1 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('martes_main course'))
    button_miercoles_main1 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('miercoles_main course'))
    button_jueves_main1 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('jueves_main course'))
    button_viernes_main1 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('viernes_main course'))
    button_sabado_main1 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('sabado_main course'))
    button_domingo_main1 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('domingo_main course'))

    button_lunes_main2 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('lunes_main course2'))
    button_martes_main2 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('martes_main course2'))
    button_miercoles_main2 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('miercoles_main course2'))
    button_jueves_main2 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('jueves_main course2'))
    button_viernes_main2 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('viernes_main course2'))
    button_sabado_main2 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('sabado_main course'))
    button_domingo_main2 = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('domingo_main course'))

    button_lunes_breakfast = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('lunes_breakfast'))
    button_martes_breakfast = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('martes_breakfast'))
    button_miercoles_breakfast = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('miercoles_breakfast'))
    button_jueves_breakfast = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('jueves_breakfast'))
    button_viernes_breakfast = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('viernes_breakfast'))
    button_sabado_breakfast = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('sabado_breakfast'))
    button_domingo_breakfast = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('domingo_breakfast'))

    button_lunes_snack = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('lunes_snack'))
    button_martes_snack = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('martes_snack'))
    button_miercoles_snack = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('miercoles_snack'))
    button_jueves_snack = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('jueves_snack'))
    button_viernes_snack = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('viernes_snack'))
    button_sabado_snack = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('sabado_snack'))
    button_domingo_snack = Button(ventana_secundaria, width=10, text='Detalles', command=lambda:details('domingo_snack'))

    button_lunes_breakfast.grid(row=1, column=1)
    button_martes_breakfast.grid(row=1, column=2)
    button_miercoles_breakfast.grid(row=1, column=3)
    button_jueves_breakfast.grid(row=1, column=4)
    button_viernes_breakfast.grid(row=1, column=5)
    button_sabado_breakfast.grid(row=1, column=6)
    button_domingo_breakfast.grid(row=1, column=7)

    button_lunes_main1.grid(row=2, column=1)
    button_martes_main1.grid(row=2, column=2)
    button_miercoles_main1.grid(row=2, column=3)
    button_jueves_main1.grid(row=2, column=4)
    button_viernes_main1.grid(row=2, column=5)
    button_sabado_main1.grid(row=2, column=6)
    button_domingo_main1.grid(row=2, column=7)

    button_lunes_snack.grid(row=3, column=1)
    button_martes_snack.grid(row=3, column=2)
    button_miercoles_snack.grid(row=3, column=3)
    button_jueves_snack.grid(row=3, column=4)
    button_viernes_snack.grid(row=3, column=5)
    button_sabado_snack.grid(row=3, column=6)
    button_domingo_snack.grid(row=3, column=7)

    button_lunes_main2.grid(row=4, column=1)
    button_martes_main2.grid(row=4, column=2)
    button_miercoles_main2.grid(row=4, column=3)
    button_jueves_main2.grid(row=4, column=4)
    button_viernes_main2.grid(row=4, column=5)
    button_sabado_main2.grid(row=4, column=6)
    button_domingo_main2.grid(row=4, column=7)

    label_lunes = Label(ventana_secundaria, text='Lunes')
    label_martes = Label(ventana_secundaria, text='Martes')
    label_miercoles = Label(ventana_secundaria, text='Miercoles')
    label_jueves = Label(ventana_secundaria, text='Jueves')
    label_viernes = Label(ventana_secundaria, text='Viernes')
    label_sabado = Label(ventana_secundaria, text='Sabado')
    label_domingo = Label(ventana_secundaria, text='Domingo')

    label_desayuno = Label(ventana_secundaria, text='Desayuno')
    label_almuerzo = Label(ventana_secundaria, text='Almuerzo')
    label_snack = Label(ventana_secundaria, text='Merienda')
    label_cena = Label(ventana_secundaria, text='Cena')

    label_lunes.grid(row=0, column=1)
    label_martes.grid(row=0, column=2)
    label_miercoles.grid(row=0, column=3)
    label_jueves.grid(row=0, column=4)
    label_viernes.grid(row=0, column=5)
    label_sabado.grid(row=0, column=6)
    label_domingo.grid(row=0, column=7)

    label_desayuno.grid(row=1, column=0)
    label_almuerzo.grid(row=2, column=0)
    label_snack.grid(row=3, column=0)
    label_cena.grid(row=4, column=0)


# BOTTON GENERADOR

generador= Button(caracteristicas_frame,bg="Tan1",fg="Black",text="Generar menú semanal",font=("Verdana",28),command=abrir_ventana_secundaria,state= DISABLED)
generador.pack(side=BOTTOM)


main.mainloop()

connection.disconnect(conn)

