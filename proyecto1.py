from tkinter import *
from tkinter import ttk
import connection, re
import translators as ts


main= Tk()

main.title("Raku")
main.config(bg="Tan1")
main.minsize(450,500)
main.maxsize(450,500)


top_frame = Frame(main,bd=2,relief=FLAT,bg="Tan1")
left_frame = Frame(main,bd=1,relief=FLAT,bg="burlywood2")
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
    ventana_secundaria.config(width=300, height=200, bg="Tan1")
    
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
    dict_name_dishes = {}
    main_course_contador= 0
    for day in listDays:
        for dish in listDishes:
            cur.execute(f'SELECT id FROM `bbdd` WHERE type = "{dish}" {condition} ORDER BY RAND() LIMIT 1')
            id = cur.fetchall()[0][0]
            if dicIds.get(f'{day}_{dish}'):
                dicIds[f'{day}_{dish}2'] = id
            else:
                dicIds[f'{day}_{dish}'] = id

            cur.execute(f'SELECT name FROM `bbdd` WHERE id = {id}')
            name = cur.fetchall()[0][0]
            name = ts.translate_text(name, to_language='es')
            # print (name)

            clave_plato=""
            if dish =='main course' and main_course_contador == 0:
                main_course_contador = 1
                clave_plato= day + "_" + dish + "_1"
            elif dish =='main course' and main_course_contador == 1:
                main_course_contador = 0
                clave_plato= day + "_" + dish + "_2"
            else:
                clave_plato= day + "_" + dish

            dict_name_dishes[clave_plato]= name
            

    def details(button):
        print(dicIds[button])
        ventana_detalles = Toplevel()
        ventana_detalles.title("Details")
        ventana_detalles.config(width=1100, height=200, bg="Tan1")
        ventana_detalles.maxsize(width=1100, height=800)


        cur.execute(f'SELECT name FROM `bbdd` WHERE id = {dicIds[button]}')
        name = cur.fetchall()[0][0]
        name = ts.translate_text(name, to_language='es')
        label_name = Label(ventana_detalles, text=name,bg='Tan1',font=40, anchor=CENTER)
        label_name.grid(row=0, column=0)
        
        cur.execute(f'SELECT ingredients FROM `bbdd` WHERE id = {dicIds[button]}')
        ingredients = cur.fetchall()[0][0]
        ingredients = re.sub(r'^ / ', '', ingredients)
        ingredients = ts.translate_text(ingredients, to_language='es')
        label_ings = Label(ventana_detalles, text='Ingredientes:', bg='burlywood2', justify=LEFT, font='bold', width=96, anchor=W)
        label_ings.grid(row=1, column=0, padx=20)
        label_ingredients = Label(ventana_detalles, text=ingredients, wraplength=1000, justify=LEFT, width=151, anchor=W,bg="burlywood2")
        label_ingredients.grid(row=2, column=0, pady=(0,10))

        cur.execute(f'SELECT id_recipe FROM `bbdd` WHERE id = {dicIds[button]}')
        recipe_id = cur.fetchall()[0][0]
        cur.execute(f'SELECT instruction FROM `recipe_steps` WHERE recipe_id = {recipe_id}')
        instruction = ''
        for ins in cur.fetchall():
            # print(ins[0])
            instruction = instruction + '\n' + ins[0]
        instruction = re.sub(r'(\n)+', '\n', instruction)
        instruction = re.sub(r'^\n', '', instruction)
        instruction = re.sub(r'\n$', '', instruction)
        instruction = ts.translate_text(instruction, to_language='es')
        label_ins = Label(ventana_detalles, text='Instrucciones:', bg='burlywood2', justify=LEFT, font='bold', width=96, anchor=W)
        label_ins.grid(row=3, column=0, padx=20)
        label_instructions = Label(ventana_detalles, text=instruction, wraplength=1000, justify='left', width=151, anchor=W,bg="burlywood2")
        label_instructions.grid(row=4, column=0, pady=(0,10))

        cur.execute(f'SELECT minutes FROM `bbdd` WHERE id = {dicIds[button]}')
        mins = cur.fetchall()[0][0]
        mins = mins, 'minutos'
        label_time = Label(ventana_detalles, text='Tiempo:', bg='burlywood2', justify=LEFT, font='bold', width=96, anchor=W)
        label_time.grid(row=5, column=0, padx=20)
        label_mins = Label(ventana_detalles, text=mins, width=151, justify=LEFT, anchor=W,bg="burlywood2")
        label_mins.grid(row=6, column=0, padx=20, pady=(0,10))

        # cur.execute(f'SELECT servings FROM `bbdd` WHERE id = {dicIds[button]}')
        # servs = cur.fetchall()[0][0]
        # servs = servs, 'personas'
        # label_servings = Label(ventana_detalles, text='Porciones:', bg='burlywood2', justify=LEFT, font='bold', width=96, anchor=W)
        # label_servings.grid(row=7, column=0, padx=20)
        # label_servs = Label(ventana_detalles, text=servs, width=151, justify=LEFT, anchor=W,bg="burlywood2")
        # label_servs.grid(row=8, column=0, pady=(0,10))

        # cur.execute(f'SELECT servings FROM `bbdd` WHERE id = {dicIds[button]}')
        # servs = cur.fetchall()[0][0]
        # label_servs = Label(ventana_detalles, text=servs, width=200, justify=LEFT, anchor=W)
        # label_servs.grid(row=4, column=0)

    fuente=("Verdana",13) 
    ancho=15
    altura=5    
    button_lunes_main1 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["lunes_main course_1"],bg="burlywood2", command=lambda:details('lunes_main course'),wraplength=170, font=fuente)
    button_martes_main1 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["martes_main course_1"],bg="burlywood2",command=lambda:details('martes_main course'),wraplength=170,font=fuente)
    button_miercoles_main1 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["miercoles_main course_1"],bg="burlywood2", command=lambda:details('miercoles_main course'),wraplength=170,font=fuente)
    button_jueves_main1 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["jueves_main course_1"],bg="burlywood2", command=lambda:details('jueves_main course'),wraplength=170,font=fuente)
    button_viernes_main1 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["viernes_main course_1"],bg="burlywood2",command=lambda:details('viernes_main course'),wraplength=170,font=fuente)
    button_sabado_main1 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["sabado_main course_1"],bg="burlywood2", command=lambda:details('sabado_main course'),wraplength=170,font=fuente)
    button_domingo_main1 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["domingo_main course_1"],bg="burlywood2", command=lambda:details('domingo_main course'),wraplength=170,font=fuente)

    button_lunes_main2 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["lunes_main course_2"],bg="burlywood2", command=lambda:details('lunes_main course2'),wraplength=170,font=fuente)
    button_martes_main2 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["martes_main course_2"],bg="burlywood2", command=lambda:details('martes_main course2'),wraplength=170,font=fuente)
    button_miercoles_main2 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["miercoles_main course_2"],bg="burlywood2", command=lambda:details('miercoles_main course2'),wraplength=170,font=fuente)
    button_jueves_main2 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["jueves_main course_2"],bg="burlywood2", command=lambda:details('jueves_main course2'),wraplength=170,font=fuente)
    button_viernes_main2 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["viernes_main course_2"],bg="burlywood2", command=lambda:details('viernes_main course2'),wraplength=170,font=fuente)
    button_sabado_main2 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["sabado_main course_2"],bg="burlywood2", command=lambda:details('sabado_main course'),wraplength=170,font=fuente)
    button_domingo_main2 = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["domingo_main course_2"],bg="burlywood2", command=lambda:details('domingo_main course'),wraplength=170,font=fuente)

    button_lunes_breakfast = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["lunes_breakfast"],bg="burlywood2", command=lambda:details('lunes_breakfast'),wraplength=170,font=fuente)
    button_martes_breakfast = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["martes_breakfast"],bg="burlywood2", command=lambda:details('martes_breakfast'),wraplength=170,font=fuente)
    button_miercoles_breakfast = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["miercoles_breakfast"],bg="burlywood2", command=lambda:details('miercoles_breakfast'),wraplength=100,font=fuente)
    button_jueves_breakfast = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["jueves_breakfast"],bg="burlywood2", command=lambda:details('jueves_breakfast'),wraplength=170,font=fuente)
    button_viernes_breakfast = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["viernes_breakfast"],bg="burlywood2", command=lambda:details('viernes_breakfast'),wraplength=170,font=fuente)
    button_sabado_breakfast = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["sabado_breakfast"],bg="burlywood2", command=lambda:details('sabado_breakfast'),wraplength=170,font=fuente)
    button_domingo_breakfast = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["domingo_breakfast"],bg="burlywood2", command=lambda:details('domingo_breakfast'),wraplength=170,font=fuente)

    button_lunes_snack = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["lunes_snack"],bg="burlywood2", command=lambda:details('lunes_snack'),wraplength=170,font=fuente)
    button_martes_snack = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["martes_snack"],bg="burlywood2", command=lambda:details('martes_snack'),wraplength=170,font=fuente)
    button_miercoles_snack = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["miercoles_snack"],bg="burlywood2", command=lambda:details('miercoles_snack'),wraplength=170,font=fuente)
    button_jueves_snack = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["jueves_snack"],bg="burlywood2", command=lambda:details('jueves_snack'),wraplength=170,font=fuente)
    button_viernes_snack = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["viernes_snack"],bg="burlywood2", command=lambda:details('viernes_snack'),wraplength=170,font=fuente)
    button_sabado_snack = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["sabado_snack"],bg="burlywood2", command=lambda:details('sabado_snack'),wraplength=170,font=fuente)
    button_domingo_snack = Button(ventana_secundaria,height=altura, width=ancho, text=dict_name_dishes["domingo_snack"],bg="burlywood2", command=lambda:details('domingo_snack'),wraplength=170,font=fuente)

    button_lunes_breakfast.grid(row=1, column=1,padx=10,pady=5)
    button_martes_breakfast.grid(row=1, column=2,padx=10,pady=5)
    button_miercoles_breakfast.grid(row=1, column=3,padx=10,pady=5)
    button_jueves_breakfast.grid(row=1, column=4,padx=10,pady=5)
    button_viernes_breakfast.grid(row=1, column=5,padx=10,pady=5)
    button_sabado_breakfast.grid(row=1, column=6,padx=10,pady=5)
    button_domingo_breakfast.grid(row=1, column=7,padx=10,pady=5)

    button_lunes_main1.grid(row=2, column=1,padx=10,pady=5)
    button_martes_main1.grid(row=2, column=2,padx=10,pady=5)
    button_miercoles_main1.grid(row=2, column=3,padx=10,pady=5)
    button_jueves_main1.grid(row=2, column=4,padx=10,pady=5)
    button_viernes_main1.grid(row=2, column=5,padx=10,pady=5)
    button_sabado_main1.grid(row=2, column=6,padx=10,pady=5)
    button_domingo_main1.grid(row=2, column=7,padx=10,pady=5)

    button_lunes_snack.grid(row=3, column=1,padx=10,pady=5)
    button_martes_snack.grid(row=3, column=2,padx=10,pady=5)
    button_miercoles_snack.grid(row=3, column=3,padx=10,pady=5)
    button_jueves_snack.grid(row=3, column=4,padx=10,pady=5)
    button_viernes_snack.grid(row=3, column=5,padx=10,pady=5)
    button_sabado_snack.grid(row=3, column=6,padx=10,pady=5)
    button_domingo_snack.grid(row=3, column=7,padx=10,pady=5)

    button_lunes_main2.grid(row=4, column=1,padx=10,pady=5)
    button_martes_main2.grid(row=4, column=2,padx=10,pady=5)
    button_miercoles_main2.grid(row=4, column=3,padx=10,pady=5)
    button_jueves_main2.grid(row=4, column=4,padx=10,pady=5)
    button_viernes_main2.grid(row=4, column=5,padx=10,pady=5)
    button_sabado_main2.grid(row=4, column=6,padx=10,pady=5)
    button_domingo_main2.grid(row=4, column=7,padx=10,pady=5)

    label_lunes = Label(ventana_secundaria, text='Lunes', bg="Tan1",font=20)
    label_martes = Label(ventana_secundaria, text='Martes', bg="Tan1",font=20)
    label_miercoles = Label(ventana_secundaria, text='Miercoles', bg="Tan1",font=20)
    label_jueves = Label(ventana_secundaria, text='Jueves', bg="Tan1",font=20)
    label_viernes = Label(ventana_secundaria, text='Viernes', bg="Tan1",font=20)
    label_sabado = Label(ventana_secundaria, text='Sabado', bg="Tan1",font=20)
    label_domingo = Label(ventana_secundaria, text='Domingo', bg="Tan1",font=20)

    label_desayuno = Label(ventana_secundaria, text='Desayuno', bg="Tan1",font=20)
    label_almuerzo = Label(ventana_secundaria, text='Almuerzo', bg="Tan1",font=20)
    label_snack = Label(ventana_secundaria, text='Merienda', bg="Tan1",font=20)
    label_cena = Label(ventana_secundaria, text='Cena', bg="Tan1",font=20)

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

