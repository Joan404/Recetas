from tkinter import *
from tkinter import ttk
import connection



main= Tk()

main.title("Proyecto")
main.config(bg="Brown1")
main.minsize(850,500)
main.maxsize(850,500)





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


# dias_lbl= Label(dias_frame,font=("Verdana",30),text="Dias",fg="Black")
# dias_lbl.pack()




#BOTONES DE CARACTERISTICAS


value=1

option = IntVar()



boton1=Radiobutton(caracteristicas_frame, text="Vegano", variable=option,
            value=1,font=("Verdana",28)).pack(anchor=W)
boton2=Radiobutton(caracteristicas_frame, text="Vegetariano", variable=option,
            value=2,font=("Verdana",28)).pack(anchor=W)
boton3=Radiobutton(caracteristicas_frame, text="Sin Lactosa", variable=option,
            value=3,font=("Verdana",28)).pack(anchor=W)
boton4=Radiobutton(caracteristicas_frame, text="Gluten-Free", variable=option,
            value=4,font=("Verdana",28)).pack(anchor=W)
boton5=Radiobutton(caracteristicas_frame, text="Todo", variable=option,
            value=5,font=("Verdana",28)).pack(anchor=W)


#BOTON GENERADOR


conn = connection.connect()
cur = conn.cursor(buffered=True)

def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Receta semanal")
    ventana_secundaria.config(width=300, height=200)

    if option.get() == 1:
        condition = 'WHERE vegan = 1'
    elif option.get() == 2:
        condition = 'WHERE vegetarian = 1'
    elif option.get() == 3:
        condition = 'WHERE diaryFree = 1'
    elif option.get() == 4:
        condition = 'WHERE glutenFree = 1'
    elif option.get() == 5:
        condition = ''

    listLunch = ['Almuerzo']
    listBreakfast = ['Desayuno']
    listDinner = ['Cena']
    listSnack = ['Merienda']

    ListDishes = ['breakfast' ,'main course', 'snack', 'main course']

    table = ttk.Treeview(ventana_secundaria, columns=('', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'), show='headings')
    table.heading('Lunes', text = 'Lunes')
    table.heading('Martes', text = 'Martes')
    table.heading('Miercoles', text = 'Miercoles')
    table.heading('Jueves', text = 'Jueves')
    table.heading('Viernes', text = 'Viernes')
    table.heading('Sabado', text = 'Sabado')
    table.heading('Domingo', text = 'Domingo')
    table.pack(fill = 'both', expand = True)

    for i in range(4):
        condition = condition + f' AND type = "{ListDishes[i]}"'
        print(condition)
        for j in range(8):
            cur.execute(f'SELECT id FROM `bbdd` {condition} ORDER BY RAND() LIMIT 1')
            id = cur.fetchall()[0][0]
            cur.execute(f'SELECT name FROM bbdd WHERE id = {id}')
            name = cur.fetchall()[0][0]
            print(name)
            listLunch.append(name)
            
        table.insert(parent='', index=i, values=(listLunch))

    
    

generador= Button(dias_frame, text="Generar menú semanal",font=("Verdana",28),command=abrir_ventana_secundaria)
generador.pack()



main.mainloop()

connection.disconnect(conn)

