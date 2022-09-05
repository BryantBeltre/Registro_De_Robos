from tkinter import *
from PIL import ImageTk, Image
import os
from peewee import *
from prettytable import PrettyTable
import time
from datetime import date
import folium
import webbrowser

#Base de datos para mantener informacion
db=SqliteDatabase ('Reporte_robos.db')

class reporte1(Model):
    Chasis= CharField(50)
    Placa= CharField(20)
    Marca= IntegerField()
    Modelo= IntegerField() 
    Color= CharField(20)
    Año= IntegerField()
    Dia_del_robo= IntegerField()
    Mes_del_robo= IntegerField()
    Año_del_robo= IntegerField()
    Nombre_del_denunciante= CharField(60)
    Cedula_del_denunciante= CharField(30)
    Descripcion_del_robo= CharField()
    Telefono=IntegerField()
    Provincia=IntegerField()
    Latitud=CharField(50)
    Longitud=CharField(50)
    Estado_del_vehiculo= CharField(40)
    Fecha_encuentro= TimeField()
    Comentario_de_encuentro= CharField()

    class Meta:
        database = db
db.connect()
db.create_tables([reporte1])




bd=SqliteDatabase ('Modelo.db')

class modelo (Model):
    Modelo_Vehiculo = CharField(30)

    class Meta:
        database = bd

bd.connect()
bd.create_tables([modelo])
#Mostrar Provincia
def Mostrar_Modelo():
    Mr=PrettyTable()
    Mr.field_names = ["Id", "Modelo" ]
    dat= modelo.select()
    for gen in dat:
        Mr.add_row([gen.id, gen.Modelo_Vehiculo])
    return (Mr)

#Eliminar Provincia
def Eliminar_modelo():

    def Elimiar_modelo_now():


        def Eliminar_Modelo():
            dat=modelo.select().where(modelo.id == My_id).get()
            dat.Modelo_Vehiculo= (D1.get())
            dat.delete_instance()



        My_id= ID.get()
        datos=modelo.select().where(modelo.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('270x100')
        T2.config(bg="light green")

        Label(T2, text= 'Modelo a eliminar →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Modelo_Vehiculo))
        D1.grid(row=0, column=2)
    
        button_elim_modelo= Button(T2, text= 'Eliminar',  bg="light blue", font=('Bodoni', '12'),command=lambda:
        (Eliminar_Modelo()))
        button_elim_modelo.place(x=40, y=65)


    T2 = Tk()
    T2.title ("B-SOFTWORLD")
    T2.geometry('500x500')
    T2.config(bg="light green")

    Id= Label(T2, text="Digite el Id", width=22, height=2, bg="light green", font=('Arial', '10'))
    Id.place(x=30, y=65)
    ID= Entry(T2, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=100)

    Tabla_prov= Label(T2, text= Mostrar_Modelo(), width= 30, height= 25, bg="pink", font=('Arial', '10'))
    Tabla_prov.place(x=215, y=90)

    button_guar_pro= Button(T2, text= 'Siguiente',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Elimiar_modelo_now()))
    button_guar_pro.place(x=40, y=350)

#Editar Provincia
def Editar_Modelo():

    def Editar_modelo_now():


        def guardar_modelo():
            dat=modelo.select().where(modelo.id == My_id).get()
            dat.Modelo_Vehiculo= (D1.get())
            dat.save()



        My_id= ID.get()
        datos=modelo.select().where(modelo.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('270x100')
        T2.config(bg="light green")

        Label(T2, text= 'Modelo actual →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Modelo_Vehiculo))
        D1.grid(row=0, column=2)
    
        button_guar_pro= Button(T2, text= 'Gruardar cambio',  bg="light blue", font=('Bodoni', '12'),command=lambda:
        (guardar_modelo()))
        button_guar_pro.place(x=40, y=65)


    T15 = Tk()
    T15.title ("B-SOFTWORLD")
    T15.geometry('500x500')
    T15.config(bg="light green")

    Id= Label(T15, text="Digite el Id", width=22, height=2, bg="light green", font=('Arial', '10'))
    Id.place(x=30, y=65)
    ID= Entry(T15, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=100)

    Tabla_marca= Label(T15, text=Mostrar_Modelo(), width= 30, height= 25, bg="pink", font=('Arial', '10'))
    Tabla_marca.place(x=215, y=90)

    button_guar_marca= Button(T15, text= 'Editar',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Editar_modelo_now()))
    button_guar_marca.place(x=40, y=350)


#Agregar Provincia
def Agregar_modelo():

    def guardar_modelo():
        midata=modelo()
        midata.Modelo_Vehiculo= (modelo_vehi.get())
        midata.save()



    T3 = Tk()
    T3.title ("B-SOFTWORLD")
    T3.geometry('300x300')
    T3.config(bg="light blue")

    Modelo_vehi= Label(T3, text="Digite la marca", width=22, height=2, bg="light green", font=('Arial', '10'))
    Modelo_vehi.place(x=80, y=65)
    modelo_vehi= Entry(T3, width=30, bg="white", fg= "blue")
    modelo_vehi.place(x=80, y=100)

    button_guar_modelo= Button(T3, text= 'Guardar Modelo',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (guardar_modelo()))
    button_guar_modelo.place(x=140, y=200)




    


#Provincia
def Gestionar_Modelo():
    T = Tk()
    T.title ("B-SOFTWORLD")
    T.geometry('500x400')
    T.config(bg="light green")

    titulo=Label(T, text= "SELECCIONE LA OPCION QUE DESEE", width=35, height=2, bg="gray", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=2)

    button_agr_caso= Button(T, text= 'Agregar Modelo',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Agregar_modelo()))
    button_agr_caso.place(x=190, y=55)

    button_mod_caso= Button(T, text= 'Editar Modelo',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Editar_Modelo()))
    button_mod_caso.place(x=190, y=150)

    button_eli_caso= Button(T, text= 'Eliminar Modelo',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Eliminar_modelo()))
    button_eli_caso.place(x=190, y=250)
    
    titulo=Label(T, text= "B-SOFTWORLD", width=35, height=2, bg="blue", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=350)






bd=SqliteDatabase ('Marca.db')

class marca (Model):
    Marca_Vehiculo = CharField(30)

    class Meta:
        database = bd

bd.connect()
bd.create_tables([marca])
#Mostrar denuncias
def Mostrar_casos():
    datos2 = PrettyTable()
    datos2.field_names = ["Chasis", "Placa", "Marca", "Modelo", "Color", "Año", "Dia del robo","Mes del robo","Año del robo","Nombre del denunciante", "Cedula del denunciante","Descripcion del robo", "Telefono", "Provincia", "Latitud","Longitud", "Estado del vehiculo", "Fecha encuentro", "Comentario"]
    dts2 =reporte1.select()
    for per in dts2:
        datos2.add_row([per.Chasis, per.Placa, per.Marca, per.Modelo, per.Color, per.Año, per.Dia_del_robo, per.Mes_del_robo, per.Año_del_robo, per.Nombre_del_denunciante, per.Cedula_del_denunciante, per.Descripcion_del_robo, per.Telefono, per.Provincia, per.Latitud, per.Longitud, per.Estado_del_vehiculo, per.Fecha_encuentro, per.
        Comentario_de_encuentro ])    
    return (datos2)
#Mostrar Provincia
def Mostrar_Marca():
    Mr=PrettyTable()
    Mr.field_names = ["Id", "Marca" ]
    dat= marca.select()
    for gen in dat:
        Mr.add_row([gen.id, gen.Marca_Vehiculo])
    return (Mr)

#Eliminar Provincia
def Elimiar_marca():

    def Elimiar_marca_now():


        def Eliminar_marca():
            dat=marca.select().where(marca.id == My_id).get()
            dat.Marca_Vehiculo= (D1.get())
            dat.delete_instance()



        My_id= ID.get()
        datos=marca.select().where(marca.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('270x100')
        T2.config(bg="light green")

        Label(T2, text= 'Provincia a eliminar →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Marca_Vehiculo))
        D1.grid(row=0, column=2)
    
        button_elim_marca= Button(T2, text= 'Eliminar',  bg="light blue", font=('Bodoni', '12'),command=lambda:
        (Eliminar_marca()))
        button_elim_marca.place(x=40, y=65)


    T2 = Tk()
    T2.title ("B-SOFTWORLD")
    T2.geometry('500x500')
    T2.config(bg="light green")

    Id= Label(T2, text="Digite el Id", width=22, height=2, bg="light green", font=('Arial', '10'))
    Id.place(x=30, y=65)
    ID= Entry(T2, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=100)

    Tabla_prov= Label(T2, text= Mostrar_Marca(), width= 30, height= 25, bg="pink", font=('Arial', '10'))
    Tabla_prov.place(x=215, y=90)

    button_guar_pro= Button(T2, text= 'Siguiente',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Elimiar_marca_now()))
    button_guar_pro.place(x=40, y=350)

#Editar Provincia
def Editar_Marca():

    def Editar_marca_now():


        def guardar_marca():
            dat=marca.select().where(marca.id == My_id).get()
            dat.Marca_Vehiculo= (D1.get())
            dat.save()



        My_id= ID.get()
        datos=marca.select().where(marca.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('270x100')
        T2.config(bg="light green")

        Label(T2, text= 'Provincia actual →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Marca_Vehiculo))
        D1.grid(row=0, column=2)
    
        button_guar_pro= Button(T2, text= 'Gruardar cambio',  bg="light blue", font=('Bodoni', '12'),command=lambda:
        (guardar_marca()))
        button_guar_pro.place(x=40, y=65)


    T15 = Tk()
    T15.title ("B-SOFTWORLD")
    T15.geometry('500x500')
    T15.config(bg="light green")

    Id= Label(T15, text="Digite el Id", width=22, height=2, bg="light green", font=('Arial', '10'))
    Id.place(x=30, y=65)
    ID= Entry(T15, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=100)

    Tabla_marca= Label(T15, text=Mostrar_Marca(), width= 30, height= 25, bg="pink", font=('Arial', '10'))
    Tabla_marca.place(x=215, y=90)

    button_guar_marca= Button(T15, text= 'Editar',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Editar_marca_now()))
    button_guar_marca.place(x=40, y=350)


#Agregar Provincia
def Agregar_marca():

    def guardar_marca():
        midata=marca()
        midata.Marca_Vehiculo= (marca_vehi.get())
        midata.save()



    T3 = Tk()
    T3.title ("B-SOFTWORLD")
    T3.geometry('300x300')
    T3.config(bg="light blue")

    Marca_vehi= Label(T3, text="Digite la marca", width=22, height=2, bg="light green", font=('Arial', '10'))
    Marca_vehi.place(x=80, y=65)
    marca_vehi= Entry(T3, width=30, bg="white", fg= "blue")
    marca_vehi.place(x=80, y=100)

    button_guar_marca= Button(T3, text= 'GuardarMArca',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (guardar_marca()))
    button_guar_marca.place(x=140, y=200)




    


#Provincia
def Gestionar_Marca():
    T = Tk()
    T.title ("B-SOFTWORLD")
    T.geometry('500x400')
    T.config(bg="light green")

    titulo=Label(T, text= "SELECCIONE LA OPCION QUE DESEE", width=35, height=2, bg="gray", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=2)

    button_agr_caso= Button(T, text= 'Agregar Marca',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Agregar_marca()))
    button_agr_caso.place(x=190, y=55)

    button_mod_caso= Button(T, text= 'Editar Marca',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Editar_Marca()))
    button_mod_caso.place(x=190, y=150)

    button_eli_caso= Button(T, text= 'Eliminar Marca',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Elimiar_marca()))
    button_eli_caso.place(x=190, y=250)
    
    titulo=Label(T, text= "B-SOFTWORLD", width=35, height=2, bg="blue", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=350)









bd = SqliteDatabase ('Provincias2.db')

class provincia (Model):
    Nombre_provincia = CharField(30)

    class Meta:
        database = bd

bd.connect()
bd.create_tables([provincia])
#Mostrar Provincia
def Mostrar_prov2():
    Mr=PrettyTable()
    Mr.field_names = ["Id", "Provincia", "Numero de casos" ]
    dat= provincia.select()

    for gen in dat:
        dats=reporte1.select()
        for gen2 in dats:
            X= gen2.Provincia

        Casos_prov=0
        if X == gen.id:
            Casos_prov= + 1
        Mr.add_row([gen.id, gen.Nombre_provincia, Casos_prov])
    return (Mr)
def Mostrar_prov():
    Mr=PrettyTable()
    Mr.field_names = ["Id", "Provincia", ]
    dat= provincia.select()
    for gen in dat:
        Mr.add_row([gen.id, gen.Nombre_provincia])
    return (Mr)

#Eliminar Provincia
def Elimiar_prov():

    def Elimiar_prov_now():


        def Eliminar_cam():
            dat=provincia.select().where(provincia.id == My_id).get()
            dat.Nombre_provincia= (D1.get())
            dat.delete_instance()



        My_id= ID.get()
        datos=provincia.select().where(provincia.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('270x100')
        T2.config(bg="light green")

        Label(T2, text= 'Provincia a eliminar →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Nombre_provincia))
        D1.grid(row=0, column=2)
    
        button_guar_pro= Button(T2, text= 'Eliminar',  bg="light blue", font=('Bodoni', '12'),command=lambda:
        (Eliminar_cam()))
        button_guar_pro.place(x=40, y=65)


    T2 = Tk()
    T2.title ("B-SOFTWORLD")
    T2.geometry('500x500')
    T2.config(bg="light green")

    Id= Label(T2, text="Digite el Id", width=22, height=2, bg="light green", font=('Arial', '10'))
    Id.place(x=30, y=65)
    ID= Entry(T2, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=100)

    Tabla_prov= Label(T2, text= Mostrar_prov(), width= 30, height= 25, bg="pink", font=('Arial', '10'))
    Tabla_prov.place(x=215, y=90)

    button_guar_pro= Button(T2, text= 'Siguiente',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Elimiar_prov_now()))
    button_guar_pro.place(x=40, y=350)

#Editar Provincia
def Editar_prov():

    def Editar_prov_now():


        def guardar_cam():
            dat=provincia.select().where(provincia.id == My_id).get()
            dat.Nombre_provincia= (D1.get())
            dat.save()



        My_id= ID.get()
        datos=provincia.select().where(provincia.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('270x100')
        T2.config(bg="light green")

        Label(T2, text= 'Provincia actual →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Nombre_provincia))
        D1.grid(row=0, column=2)
    
        button_guar_pro= Button(T2, text= 'Gruardar cambio',  bg="light blue", font=('Bodoni', '12'),command=lambda:
        (guardar_cam()))
        button_guar_pro.place(x=40, y=65)


    T2 = Tk()
    T2.title ("B-SOFTWORLD")
    T2.geometry('500x500')
    T2.config(bg="light green")

    Id= Label(T2, text="Digite el Id", width=22, height=2, bg="light green", font=('Arial', '10'))
    Id.place(x=30, y=65)
    ID= Entry(T2, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=100)

    Tabla_prov= Label(T2, text= Mostrar_prov(), width= 30, height= 25, bg="pink", font=('Arial', '10'))
    Tabla_prov.place(x=215, y=90)

    button_guar_pro= Button(T2, text= 'Editar',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Editar_prov_now()))
    button_guar_pro.place(x=40, y=350)


#Agregar Provincia
def Agregar_prov():

    def guardar_prov():
        midata=provincia()
        midata.Nombre_provincia= (nombre_pro.get())
        midata.save()



    T3 = Tk()
    T3.title ("B-SOFTWORLD")
    T3.geometry('300x300')
    T3.config(bg="light blue")

    Nombre_pro= Label(T3, text="Digite el nombre", width=22, height=2, bg="light green", font=('Arial', '10'))
    Nombre_pro.place(x=80, y=65)
    nombre_pro= Entry(T3, width=30, bg="white", fg= "blue")
    nombre_pro.place(x=80, y=100)

    button_guar_pro= Button(T3, text= 'Guardar provincia',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (guardar_prov()))
    button_guar_pro.place(x=140, y=200)




    


#Provincia
def Gestionar_prov():
    T = Tk()
    T.title ("B-SOFTWORLD")
    T.geometry('500x400')
    T.config(bg="light green")

    titulo=Label(T, text= "SELECCIONE LA OPCION QUE DESEE", width=35, height=2, bg="gray", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=2)

    button_agr_caso= Button(T, text= 'Agregar provincia',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Agregar_prov()))
    button_agr_caso.place(x=190, y=55)

    button_mod_caso= Button(T, text= 'Editar provincia',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Editar_prov()))
    button_mod_caso.place(x=190, y=150)

    button_eli_caso= Button(T, text= 'Eliminar provincia',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Elimiar_prov()))
    button_eli_caso.place(x=190, y=250)
    
    titulo=Label(T, text= "B-SOFTWORLD", width=35, height=2, bg="blue", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=350)






#Configuraciona
def Configurar():
    T = Tk()
    T.title ("B-SOFTWORLD")
    T.geometry('500x400')
    T.config(bg="light green")

    titulo=Label(T, text= "SELECCIONE LA OPCION QUE DESEE", width=35, height=2, bg="gray", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=2)

    button_agr_caso= Button(T, text= 'Gestionar Provincia',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Gestionar_prov()))
    button_agr_caso.place(x=200, y=55)

    button_mod_caso= Button(T, text= 'Gestionar Marca',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Gestionar_Marca()))
    button_mod_caso.place(x=195, y=150)

    button_eli_caso= Button(T, text= 'Gestionar Modelo',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Gestionar_Modelo()))
    button_eli_caso.place(x=202, y=250)
    
    titulo=Label(T, text= "B-SOFTWORLD", width=35, height=2, bg="blue", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=350)





#Html
def Exportar_html():

    def Tabln():
        My_id= ID.get()   
        datos2 = PrettyTable()
        datos2.header_style='upper'
        datos2.horizontal_char='_'
        datos2.vertical_char='!'
        datos2.field_names = ["Chasis", "Placa", "Marca", "Modelo", "Color", "Año", "Dia del robo","Mes del robo","Año del robo","Nombre del denunciante", "Cedula del denunciante","Descripcion del robo", "Telefono", "Provincia", "Latitud","Longitud", "Estado del vehiculo", "Fecha encuentro", "Comentario"]
        dts2 =reporte1.select()
        for per in dts2:
            datos2.add_row([per.Chasis, per.Placa, per.Marca, per.Modelo, per.Color, per.Año, per.Dia_del_robo, per.Mes_del_robo, per.Año_del_robo, per.Nombre_del_denunciante, per.Cedula_del_denunciante, per.Descripcion_del_robo, per.Telefono, per.Provincia, per.Latitud, per.Longitud, per.Estado_del_vehiculo, per.Fecha_encuentro, per.
            Comentario_de_encuentro ])    
        return (datos2)
        
        if My_id == "":
            return False

    def now():        
        My_id= ID.get()
        R=reporte1.select().where(reporte1.id == My_id).get()

        html = """
            <html>
            <head>
            <style>
                table{
                    margin-top:50px;
                    box-shadow: 5px 10px #00FF00;
                    width:200%;
                    position: relative;
                    animation-name: pos;
                    animation-duration: 2s;
                    animation-fill-mode:forwards;
                }
                @keyframes pos {
                    from {top: 200px;}
                    to {top: 0px; color: blue;}
                    0%   {color:deeppink;}
                    25%  {color:gold;}
                    50%  {color: blue;}
                    100% {color: green;}
                }
                td,th{
                    text-align:left;
                    padding: 12px;
                }
                h2{
                    text-align: center;
                    color: #FF0000;
                    position: relative;
                    animation-name: pus;
                    animation-duration: 6s;
                    animation-iteration-count: 2;

                }

                @keyframes pus {
                    0%   {color:deeppink;left:0px; top:0px;}
                    25%  {color:gold;left:200px; top:0px;}
                    50%  {color: blue;left:200px; top:20px;}
                    75%  {color:#1E90FF; left:0px; top:20px;}
                    100% {color: #7CFC00;left:0px; top:0px;}
                }
                h3{ 
                    margin-top:50px;
                    text-align:left;
                    color: aqua;
                    position: relative;
                    animation-name: pepas;
                    animation-duration: 3s;
                    animation-fill-mode: forwards;
                }

                @keyframes pepas {
                    from {top: 200px;}
                    to {top: 0px; color: blue;}
                    0%   {color:deeppink;}
                    25%  {color:gold;}
                    50%  {color: blue;}
                    100% {color: green;}
                }


                td{
                    border-bottom: 6px solid blue;
                    background-color: #FDF5E6;
                    animation-name: example;
                    animation-duration: 2s;
                    text-align: center;
                    animation-iteration-count: infinite;
                }
                @keyframes example {
                    0%   {color:crimson;}
                    25%  {color: red;}
                    50%  {color: blue;}
                    100% {color:white;}
                }

    
                th{
                    border:2px solid #FF6347;
                    background-color: light;
                    animation-name: lola;
                    animation-duration: 4s;
                    text-align: center;
                    animation-iteration-count:infinite;
                    animation-direction: alternate;  

                }
                @keyframes lola {
                    0%   {color:lawngreen;}
                    25%  {color:lightsalmon;}
                    50%  {color:orangered;}
                    100% {color: green;}
                }



                .row:after {
                    content: "";
                    display: table;
                    clear: both;
                }
                .column.side {
                    margin-top:30px;
                    width: 15%;

                }
                div.container{

                }


                body{
                    background-color:white;
                    background-image: url('https://cdn.pixabay.com/photo/2020/01/22/18/23/bridge-4785964_960_720.jpg');
                }
            </style>
            </head>
            <body>
                <div class="container">  
                    <h2>DATOS</h2>   
                    <table>
                        <tr>
                            <th>CHASIS</th>
                            <th>PLACA</th>
                            <th>MARCA</th>
                            <th>MODELO</th>
                            <th>COLOR</th>
                            <th>AÑO</th>
                            <th>DIA DEL ROBO</th>
                            <th>MES DEL ROBO</th>
                            <th>AÑO DEL ROBO</th>
                            <th>NOMBRE DENUNCIANTE</th>
                            <th>CEDULA DENUNCIANTE</th>
                            <th>DESCRIPCION ROBO</th>
                            <th>TELEFONO</th>
                            <th>PROVINCIA</th>
                            <th>LATITUD</th>
                            <th>LONGITUD</th>
                            <th>ESTADO DEL VEHICULO</th>
                            <th>FECHA ENCUENTRO</th>
                            <th>DESCRIPCION ENCUENTRO</th>
                            
                            </tr>
                            <tr>
                            <td>#chasis</td>
                            <td>#placa</td>
                            <td>#marca</td>
                            <td>#modelo</td>
                            <td>#color</td>
                            <td>#Año</td>
                            <td>#DiaRobo</td>
                            <td>#MesRobo</td>
                            <td>#AñoRobo</td>
                            <td>#NombreD</td>
                            <td>#CedulaD</td>
                            <td>#DescripRobo</td>
                            <td>#Telefono</td>
                            <td>#Provincia</td>
                            <td>#Latitud</td>
                            <td>#Longitud</td>
                            <td>#EstadoVehi</td>
                            <td>#FechaEncuentro</td>
                            <td>#DescripcionEncu</td>
                            
                        </tr>
                    </table>

            </body>
            </html>
        """
        html= html.replace('#chasis',str(R.Chasis))
        html= html.replace('#placa',str(R.Placa))
        html= html.replace('#marca',str(R.Marca))
        html= html.replace('#modelo',str(R.Modelo))
        html= html.replace('#color',str(R.Color))
        html= html.replace('#Año',str(R.Año))
        html= html.replace('#DiaRobo',str(R.Dia_del_robo))
        html= html.replace('#MesRobo',str(R.Mes_del_robo))
        html= html.replace('#AñoRobo',str(R.Año_del_robo))
        html= html.replace('#NombreD',str(R.Nombre_del_denunciante))
        html= html.replace('#CedulaD',str(R.Cedula_del_denunciante))
        html= html.replace('#DescripRobo',str(R.Descripcion_del_robo))
        html= html.replace('#Telefono',str(R.Telefono))
        html= html.replace('#Provincia',str(R.Provincia))
        html= html.replace('#Latitud',str(R.Latitud))
        html= html.replace('#Longitud',str(R.Longitud))
        html= html.replace('#EstadoVehi',str(R.Estado_del_vehiculo))
        html= html.replace('#FechaEncuentro',str(R.Fecha_encuentro))
        html= html.replace('#DescripcionEncu',str(R.Comentario_de_encuentro))
        
        f=open('datos.html','w')
        f.write(html)
        f.close()
        webbrowser.open('datos.html')



     
    


    T15 = Tk()
    T15.title ("B-SOFTWORLD")
    T15.geometry('1000x1000')
    T15.config(bg="light green")

    Id= Label(T15, text="Digite el Id", width=22, height=2, bg="light green", font=('Arial', '10'))
    Id.place(x=30, y=65)
    ID= Entry(T15, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=100)

    Tabla_marca= Label(T15, text=Mostrar_registro(), width= 100, height= 50, bg="pink", font=('Arial', '10'))
    Tabla_marca.place(x=215, y=90)

    button_guar_marca= Button(T15, text= 'Exportar',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (now()))
    button_guar_marca.place(x=40, y=350)






#Mapa
def Mapa():
    todos = reporte1.select()
    m=folium.Map(location=[19.1900018, -70.8080994], zoom_start=9)
    for gen in todos:
        folium.Marker([gen.Latitud, gen.Longitud], popup=f"<i>{gen.Descripcion_del_robo} {gen.Nombre_del_denunciante}</i>", tooltip="Haz click para mostrarte").add_to(m)
    m.save("Mapa.html")
    webbrowser.open("Mapa.html")









#Listado de carros robados
def list_robados():
    def Mostrar_robo():
        Mr=PrettyTable()
        Mr.field_names = ["Marca", "Modelo", "Color", "Año", "Provincia" ]
        dat= reporte1.select()
        for gen in dat:
            Mr.add_row([gen.Marca, gen.Modelo, gen.Color, gen.Año, gen.Provincia])
        return (Mr)


    principal3 = Tk()
    principal3.title ("B-SOFTWORLD")
    principal3.geometry('1350x700')
    principal3.config(bg="light blue")


    Tabla= Label(principal3, text=Mostrar_robo(), width=100, height=20, bg="pink", font=('Arial', '10'))
    Tabla.place(x=130, y=230)

#Robos por signo zodiacal

Capricornio=20
Acuario= 19
Piscis =20
Aries=20
Tauro=21
Geminis = 21
Canser=22
Leo=22
Virgo=22
Libra=22
Escorpio = 22
Saitario =21
def Zodiaco():



    def Zodiacal():
        principal5 = Tk()
        principal5.title ("B-SOFTWORLD")
        principal5.geometry('1350x700')
        principal5.config(bg="light blue")
        
        da=reporte1()

        Signo_Zodiacal=["Capricornio","Acuario","Piscis","Aries", "Tauro","Geminis","Canser","Leo","Virgo","Libra","Escorpio","Sagitario"]
        Fecha=[20 , 19 , 20 , 20 , 21 , 21 , 22 , 22 , 22 , 22 , 22 , 21]

        mes = mes-1
        if dia > Fecha[mes]:
            mes= mes + 1
        if mes == 12:
            mes=0
 

        



            

        dato=reporte1.select().where(reporte1.Dia_del_robo == Sig ).get()
        Tabla= Label(principal5, text=Mostrar_robo(), width=100, height=20, bg="pink", font=('Arial', '10'))
        Tabla.place(x=130, y=230)
             
    
    principal4 = Tk()
    principal4.title ("B-SOFTWORLD")
    principal4.geometry('300x300')
    principal4.config(bg="light blue")

    Signo= Label(principal4, text="Digite el signo zodiacal", width=30, height=2, bg="light green", font=('Arial', '10'))
    Signo.place(x=25, y=85)
    signo= Entry(principal4, width=30, bg="white", fg= "blue")
    signo.place(x=50, y=150)



    Boton_E = Button(principal4, text="Siguiente",  bg="light blue", font=('Bodoni', '12'), command=lambda:
    (Zodiacal()))
    Boton_E.place(x=190, y=210)


#Funcion datos
def repoite():
    datos3 = PrettyTable()
    datos3.field_names = ["Chasis", "Placa", "Marca", "Modelo", "Color", "Año", "Dia del robo","Mes del robo","Año del robo","Nombre del denunciante", "Cedula del denunciante","Descripcion del robo", "Telefono", "Provincia", "Latitud","Longitud", "Estado del vehiculo", "Fecha encuentro", "Comentario"]
    dats=reporte1.select()
    for per in dats:
        datos3.add_row([per.Chasis, per.Placa, per.Marca, per.Modelo, per.Color, per.Año, per.Dia_del_robo, per.Mes_del_robo, per.Año_del_robo, per.Nombre_del_denunciante, per.Cedula_del_denunciante, per.Descripcion_del_robo, per.Telefono, per.Provincia, per.Latitud, per.Longitud, per.Estado_del_vehiculo, per.Fecha_encuentro, per.
        Comentario_de_encuentro ])    
    return (datos3)

def Exportar_por_prov():

    def exportando():
        dats=reporte1.select().where(reporte1.Provincia)
        dts=provincia.select().where(provincia.id)
        Casos_prov=0
        if dats == dts:
            Casos_prov + 1

        



        
    principal20 = Tk()
    principal20.title ("B-SOFTWORLD")
    principal20.geometry('600x600')
    principal20.config(bg="light blue")

    Provins= Label(principal20, text="El Id provincia", width=30, height=2, bg="light green", font=('Arial', '10'))
    Provins.place(x=25, y=85)
    provins= Entry(principal20, width=30, bg="white", fg= "blue")
    provins.place(x=50, y=150)

    Tablita= Label(principal20, text=Mostrar_prov2() , width=50, height=15, bg="pink", font=('Arial', '10'))
    Tablita.place(x=130, y=230)

    button_expor_marca= Button(principal20, text= 'Exportar por provincia',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (exportando()))
    button_expor_marca.place(x=180, y=550)


    








#Menus para reportar casos
def Reporte_casos():
    T3 = Tk()
    T3.title ("B-SOFTWORLD")
    T3.geometry('500x700')
    T3.config(bg="light green")

    titulo=Label(T3, text= "SELECCIONE COMO DESEA EXPORTAR", width=35, height=2, bg="gray", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=2)

    button_expor_caso= Button(T3, text= 'Listado de carros robados',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (list_robados()))
    button_expor_caso.place(x=155, y=55)

    button_expor_Sig= Button(T3, text= 'Listado de casos por signo zodiacal',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Zodiaco()))
    button_expor_Sig.place(x=120, y=150)

    button_expor_mapa= Button(T3, text= 'Mapa de robos',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    ( Mapa()))
    button_expor_mapa.place(x=200, y=250)

    button_Exportar_html= Button(T3, text= 'Exportar HTML',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Exportar_html()))
    button_Exportar_html.place(x=202, y=350)

    button_Exportar_prov= Button(T3, text= 'Reporte por provincia',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Exportar_por_prov()))
    button_Exportar_prov.place(x=180, y=450)

    button_expor_marca= Button(T3, text= 'Exportar por marca',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (eliminar()))
    button_expor_marca.place(x=180, y=550)
    
    titulo=Label(T3, text= "B-SOFTWORLD", width=35, height=2, bg="blue", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=650)














#Funciones para registrar vehiculo encontrado
def vehiculo_en():

    def vehi_enco():

        def save_vhi():
            datoss=reporte1.select().where(reporte1.Placa == My_plac).get()
            datoss.Estado_del_vehiculo= (D15.get())
            datoss.Fecha_encuentro = (D16.get())
            datoss.Comentario_de_encuentro = (D17.get())
            datoss.save()



        My_plac= placa.get()
        datos=reporte1.select().where(reporte1.Placa == My_plac).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('300x300')
        T2.config(bg="light green")


        Label(T2, text= 'Estado del vehiculo→').grid(row=14, column=1)
        D15= Entry(T2, textvariable= StringVar(T2, value= datos.Estado_del_vehiculo))
        D15.grid(row=14, column=2)
        Label(T2, text= 'Fecha de encuentro→').grid(row=15, column=1)
        D16= Entry(T2, textvariable= StringVar(T2, value= datos.Fecha_encuentro))
        D16.grid(row=15, column=2)
        Label(T2, text= 'Comentario_de_encuentro→').grid(row=16, column=1)
        D17= Entry(T2, textvariable= StringVar(T2, value= datos.Comentario_de_encuentro))
        D17.grid(row=16, column=2)
        Boton_E = Button(T2, text="Guardar",  bg="light blue", font=('Bodoni', '12'), command=lambda:
        (save_vhi()))
        Boton_E.place(x=190, y=210)


    principal4 = Tk()
    principal4.title ("B-SOFTWORLD")
    principal4.geometry('300x300')
    principal4.config(bg="light blue")

    Placa= Label(principal4, text="Digite La placa del carro que encontro", width=30, height=2, bg="light green", font=('Arial', '10'))
    Placa.place(x=25, y=85)
    placa= Entry(principal4, width=30, bg="white", fg= "blue")
    placa.place(x=50, y=150)



    Boton_E = Button(principal4, text="Siguiente",  bg="light blue", font=('Bodoni', '12'), command=lambda:
    (vehi_enco()))
    Boton_E.place(x=190, y=210)








#Prettytable
def Mostrar_registro():
    Mr=PrettyTable()
    Mr.field_names = ["Id", "Cedula", "Nombres", "Dia denuncia", "Mes denuncia", "Año denuncia", "Placa" ]
    dat= reporte1.select()
    for persona in dat:
        Mr.add_row([persona.id, persona.Cedula_del_denunciante, persona.Nombre_del_denunciante, persona.Dia_del_robo, persona.Mes_del_robo, persona.Año_del_robo, persona.Placa])
    return (Mr)

#Eliminar denuncia

def eliminar():

    def Elim():

        def eliminado():
            
            dat=reporte1.select().where(reporte1.id == My_id).get()
            dat.Chasis= (D1.get())
            dat.Placa=(D2.get())
            dat.Marca=(D3.get())
            dat.Modelo= (D4.get())
            dat.Color = (D5.get())
            dat.Año = (D6.get())
            dat.Dia_del_robo = (D7.get())
            dat.Mes_del_robo = (D8.get())
            dat.Año_del_robo = (D9.get())
            dat.Nombre_del_denunciante = (D10.get())
            dat.Cedula_del_denunciante= (D11.get())
            dat.Descripcion_del_robo= (D12.get())
            dat.Telefono= (D13.get())
            dat.Provincia= (D14.get())
            dat.Latitud= (D15.get())
            dat.Longitud= (D16.get())
            dat.Estado_del_vehiculo= (D17.get())
            dat.Fecha_encuentro= (D18.get())
            dat. Comentario_de_encuentro= (D19.get())
            dat.delete_instance()



        My_id= ID.get()
        datos=reporte1.select().where(reporte1.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('400x500')
        T2.config(bg="light green")

        Label(T2, text= 'Chasi actual →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Chasis))
        D1.grid(row=0, column=2)
        Label(T2, text= 'Placa Actual →').grid(row=1, column=1)
        D2 = Entry(T2, textvariable= StringVar(T2, value= datos.Placa ))
        D2.grid(row=1, column=2)
        Label(T2, text= 'Marca Actual→').grid(row=2, column=1)
        D3=Entry(T2, textvariable= StringVar(T2, value= datos.Marca ))
        D3.grid(row=2, column=2)
        Label(T2, text= 'Modelo Actual →').grid(row=3, column=1)
        D4= Entry(T2, textvariable= StringVar(T2, value= datos.Modelo ))
        D4.grid(row=3, column=2)
        Label(T2, text= 'Color Actual →').grid(row=4, column=1)
        D5= Entry(T2, textvariable= StringVar(T2, value= datos.Color ))
        D5.grid(row=4, column=2)
        Label(T2, text= 'Años Actual →').grid(row=5, column=1)
        D6= Entry(T2, textvariable= StringVar(T2, value= datos.Año))
        D6.grid(row=5, column=2)
        Label(T2, text= 'Dia de la denuncia Actual →').grid(row=6, column=1)
        D7=Entry(T2, textvariable= StringVar(T2, value= datos.Dia_del_robo))
        D7.grid(row=6, column=2)
        Label(T2, text= 'Mes de la denuncia Actual →').grid(row=7, column=1)
        D8=Entry(T2, textvariable= StringVar(T2, value= datos.Mes_del_robo))
        D8.grid(row=7, column=2)
        Label(T2, text= 'Año de la denuncia Actual →').grid(row=8, column=1)
        D9=Entry(T2, textvariable= StringVar(T2, value= datos.Año_del_robo))
        D9.grid(row=8, column=2)
        Label(T2, text= 'Nombre del denunciante actual →').grid(row=9, column=1)
        D10= Entry(T2, textvariable= StringVar(T2, value= datos.Nombre_del_denunciante ))
        D10.grid(row=9, column=2)
        Label(T2, text= 'Cedula del denunciante Actual →').grid(row=10, column=1)
        D11= Entry(T2, textvariable= StringVar(T2, value= datos.Cedula_del_denunciante))
        D11.grid(row=10, column=2)
        Label(T2, text= 'Descripcion del robo →').grid(row=11, column=1)
        D12= Entry(T2, textvariable= StringVar(T2, value= datos.Descripcion_del_robo))
        D12.grid(row=11, column=2)
        Label(T2, text= 'Telefono →').grid(row=12, column=1)
        D13= Entry(T2, textvariable= StringVar(T2, value= datos.Telefono))
        D13.grid(row=12, column=2)
        Label(T2, text= 'Provincia →').grid(row=13, column=1)
        D14= Entry(T2, textvariable= StringVar(T2, value= datos.Provincia))
        D14.grid(row=13, column=2)
        Label(T2, text= 'Latitud →').grid(row=14, column=1)
        D15= Entry(T2, textvariable= StringVar(T2, value= datos.Latitud))
        D15.grid(row=14, column=2)
        Label(T2, text= 'Longitud →').grid(row=15, column=1)
        D16= Entry(T2, textvariable= StringVar(T2, value= datos.Longitud))
        D16.grid(row=15, column=2)        
        Label(T2, text= 'Estado del vehiculo→').grid(row=16, column=1)
        D17= Entry(T2, textvariable= StringVar(T2, value= datos.Estado_del_vehiculo))
        D17.grid(row=16, column=2)
        Label(T2, text= 'Fecha de encuentro→').grid(row=17, column=1)
        D18= Entry(T2, textvariable= StringVar(T2, value= datos.Fecha_encuentro))
        D18.grid(row=17, column=2)
        Label(T2, text= 'Comentario_de_encuentro→').grid(row=18, column=1)
        D19= Entry(T2, textvariable= StringVar(T2, value= datos.Comentario_de_encuentro))
        D19.grid(row=18, column=2)




        Boton_G=Button(T2, text= "Eliminar instancia", bg="light blue", font=('Bodoni', '12'), command=lambda:
        (eliminado()))
        Boton_G.grid(row=35, column=1)


    




    principal3 = Tk()
    principal3.title ("B-SOFTWORLD")
    principal3.geometry('1350x700')
    principal3.config(bg="light blue")

    ID= Label(principal3, text="Digite el ID que desea eliminar", width=22, height=2, bg="light green", font=('Arial', '10'))
    ID.place(x=30, y=135)
    ID= Entry(principal3, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=190)

    Tabla= Label(principal3, text=Mostrar_registro(), width=100, height=20, bg="pink", font=('Arial', '10'))
    Tabla.place(x=130, y=230)

    Boton_E = Button(principal3, text="Eliminar",  bg="light blue", font=('Bodoni', '12'), command=lambda:
    (Elim()))
    Boton_E.place(x=70, y=590)




#Modificar denuncia
def editar():
    principal2 = Tk()
    principal2.title ("B-SOFTWORLD")
    principal2.geometry('1350x700')
    principal2.config(bg="light blue")

    def Editar_N():

        def guadar_e():
            
            dat=reporte1.select().where(reporte1.id == My_id).get()
            dat.Chasis= (D1.get())
            dat.Placa=(D2.get())
            dat.Marca=(D3.get())
            dat.Modelo= (D4.get())
            dat.Color = (D5.get())
            dat.Año = (D6.get())
            dat.Dia_del_robo = (D7.get())
            dat.Mes_del_robo = (D8.get())
            dat.Año_del_robo = (D9.get())
            dat.Nombre_del_denunciante = (D10.get())
            dat.Cedula_del_denunciante= (D11.get())
            dat.Descripcion_del_robo= (D12.get())
            dat.Telefono= (D13.get())
            dat.Provincia= (D14.get())
            dat.Latitud= (D15.get())
            dat.Longitud= (D16.get())
            dat.Estado_del_vehiculo= (D17.get())
            dat.Fecha_encuentro= (D18.get())
            dat. Comentario_de_encuentro= (D19.get())
            dat.save()


        My_id= ID.get()
        datos=reporte1.select().where(reporte1.id == My_id).get()
        T2 = Tk()
        T2.title ("B-SOFTWORLD")
        T2.geometry('400x500')
        T2.config(bg="light green")

        Label(T2, text= 'Chasi actual →').grid(row=0, column=1)
        D1 = Entry(T2, textvariable= StringVar(T2, value= datos.Chasis))
        D1.grid(row=0, column=2)
        Label(T2, text= 'Placa Actual →').grid(row=1, column=1)
        D2 = Entry(T2, textvariable= StringVar(T2, value= datos.Placa ))
        D2.grid(row=1, column=2)
        Label(T2, text= 'Marca Actual→').grid(row=2, column=1)
        D3=Entry(T2, textvariable= StringVar(T2, value= datos.Marca ))
        D3.grid(row=2, column=2)
        Label(T2, text= 'Modelo Actual →').grid(row=3, column=1)
        D4= Entry(T2, textvariable= StringVar(T2, value= datos.Modelo ))
        D4.grid(row=3, column=2)
        Label(T2, text= 'Color Actual →').grid(row=4, column=1)
        D5= Entry(T2, textvariable= StringVar(T2, value= datos.Color ))
        D5.grid(row=4, column=2)
        Label(T2, text= 'Años Actual →').grid(row=5, column=1)
        D6= Entry(T2, textvariable= StringVar(T2, value= datos.Año))
        D6.grid(row=5, column=2)
        Label(T2, text= 'Dia de la denuncia Actual →').grid(row=6, column=1)
        D7=Entry(T2, textvariable= StringVar(T2, value= datos.Dia_del_robo))
        D7.grid(row=6, column=2)
        Label(T2, text= 'Mes de la denuncia Actual →').grid(row=7, column=1)
        D8=Entry(T2, textvariable= StringVar(T2, value= datos.Mes_del_robo))
        D8.grid(row=7, column=2)
        Label(T2, text= 'Año de la denuncia Actual →').grid(row=8, column=1)
        D9=Entry(T2, textvariable= StringVar(T2, value= datos.Año_del_robo))
        D9.grid(row=8, column=2)
        Label(T2, text= 'Nombre del denunciante actual →').grid(row=9, column=1)
        D10= Entry(T2, textvariable= StringVar(T2, value= datos.Nombre_del_denunciante ))
        D10.grid(row=9, column=2)
        Label(T2, text= 'Cedula del denunciante Actual →').grid(row=10, column=1)
        D11= Entry(T2, textvariable= StringVar(T2, value= datos.Cedula_del_denunciante))
        D11.grid(row=10, column=2)
        Label(T2, text= 'Descripcion del robo →').grid(row=11, column=1)
        D12= Entry(T2, textvariable= StringVar(T2, value= datos.Descripcion_del_robo))
        D12.grid(row=11, column=2)
        Label(T2, text= 'Telefono →').grid(row=12, column=1)
        D13= Entry(T2, textvariable= StringVar(T2, value= datos.Telefono))
        D13.grid(row=12, column=2)
        Label(T2, text= 'Provincia →').grid(row=13, column=1)
        D14= Entry(T2, textvariable= StringVar(T2, value= datos.Provincia))
        D14.grid(row=13, column=2)
        Label(T2, text= 'Latitud →').grid(row=14, column=1)
        D15= Entry(T2, textvariable= StringVar(T2, value= datos.Latitud))
        D15.grid(row=14, column=2)
        Label(T2, text= 'Longitud →').grid(row=15, column=1)
        D16= Entry(T2, textvariable= StringVar(T2, value= datos.Longitud))
        D16.grid(row=15, column=2)        
        Label(T2, text= 'Estado del vehiculo→').grid(row=16, column=1)
        D17= Entry(T2, textvariable= StringVar(T2, value= datos.Estado_del_vehiculo))
        D17.grid(row=16, column=2)
        Label(T2, text= 'Fecha de encuentro→').grid(row=17, column=1)
        D18= Entry(T2, textvariable= StringVar(T2, value= datos.Fecha_encuentro))
        D18.grid(row=17, column=2)
        Label(T2, text= 'Comentario_de_encuentro→').grid(row=18, column=1)
        D19= Entry(T2, textvariable= StringVar(T2, value= datos.Comentario_de_encuentro))
        D19.grid(row=18, column=2)



        Boton_G=Button(T2, text= "Guardar cambio", bg="light blue", font=('Bodoni', '12'), command=lambda:
        (guadar_e()))
        Boton_G.grid(row=35, column=1)



    ID= Label(principal2, text="Digite el ID que desea editar", width=20, height=2, bg="light green", font=('Arial', '10'))
    ID.place(x=30, y=135)
    ID= Entry(principal2, width=30, bg="white", fg= "blue")
    ID.place(x=30, y=190)

    Tabla= Label(principal2, text=Mostrar_registro(), width=100, height=20, bg="pink", font=('Arial', '10'))
    Tabla.place(x=130, y=230)

    Boton_E = Button(principal2, text="Editar",  bg="light blue", font=('Bodoni', '12'), command=lambda:
    (Editar_N()))
    Boton_E.place(x=70, y=590)




#Agregar denuncias
def Agregar_caso():

    inter = Tk()
    inter.title ("B-SOFTWORLD")
    inter.geometry('1350x700')
    inter.config(bg="light blue")

    def guardar ():
        datos2= reporte1()
        datos2.Chasis= (chasis.get())
        datos2.Placa= (placa.get())
        datos2.Marca=(marca.get())
        datos2.Modelo= (modelo.get())
        datos2.Color= (color.get())
        datos2.Año= (año.get())
        datos2.Dia_del_robo= (dia.get())
        datos2.Mes_del_robo= (mes.get())
        datos2.Año_del_robo= (año_de.get())
        datos2.Nombre_del_denunciante= (nombre_del_denunciante.get())
        datos2.Cedula_del_denunciante= (cedula_del_denunciante.get())
        datos2.Descripcion_del_robo= (descripcion_del_robo.get())
        datos2.Telefono= (telefono.get())
        datos2.Provincia= (provincia.get())
        datos2.Latitud= (latitud.get())
        datos2.Longitud= (longitud.get())
        datos2.Estado_del_vehiculo= (estado_del_vehiculo.get())
        datos2.Fecha_encuentro= (fecha_encuentro.get())
        datos2.Comentario_de_encuentro= (comentario_de_encuentro.get())
        datos2.save()


    Chasis= Label(inter, text="Chasis:", width=6, height=2, bg="light blue", font=('Arial', '10'))
    Chasis.place(x=30, y=120)
    chasis= Entry(inter, width=30, bg="white", fg= "blue")
    chasis.place(x=30, y=150)

    Placa= Label(inter, text="No.Placa:", width=10, height=2, bg="light blue", font=('Arial', '10'))
    Placa.place(x=260, y=120)
    placa= Entry(inter, width=30, bg="white", fg= "blue")
    placa.place(x=260, y= 150)

    Marca= Label(inter, text="Id Marca:", width=8, height=2, bg="light blue", font=('Arial', '10'))
    Marca.place(x=490, y=120)
    marca= Entry(inter, width=30, bg="white", fg= "blue")
    marca.place(x=490, y=150)

    Modelo= Label(inter, text="Id Modelo:", width=8, height=2, bg="light blue", font=('Arial', '10'))
    Modelo.place(x=720, y=120)
    modelo= Entry(inter, width=30, bg="white", fg= "blue")
    modelo.place(x=720, y=150)

    Color= Label(inter, text="Color:", width=6, height=2, bg="light blue", font=('Arial', '10'))
    Color.place(x=950, y=120)
    color= Entry(inter, width=30, bg="white", fg= "blue")
    color.place(x=950, y=150)

    Año=Label(inter, text="Año:", width=5, height=2, bg="light blue", font=('Arial', '10'))
    Año.place(x=1160, y=120)
    año= Entry(inter, width=30, bg="white", fg= "blue")
    año.place(x=1160, y=150)

    Dia= Label(inter, text="Dia  de la denuncia:", width=15, height=2, bg="light blue", font=('Arial', '10'))
    Dia.place(x=30, y=205)
    dia= Entry(inter, width=30, bg="white", fg= "blue")
    dia.place(x=30, y=230)
    
    Mes= Label(inter, text="Mes  de la denuncia:", width=15, height=2, bg="light blue", font=('Arial', '10'))
    Mes.place(x=260, y=205)
    mes= Entry(inter, width=30, bg="white", fg= "blue")
    mes.place(x=260, y=230)

    Año_de= Label(inter, text="Año  de la denuncia:", width=15, height=2, bg="light blue", font=('Arial', '10'))
    Año_de.place(x=490, y=205)
    año_de= Entry(inter, width=30, bg="white", fg= "blue")
    año_de.place(x=490, y=230)
    

    Nombre_del_denunciante= Label(inter, text="Nombre de denunciante:", width=18, height=2, bg="light blue", font=('Arial', '10'))
    Nombre_del_denunciante.place(x=720, y=205)
    nombre_del_denunciante = Entry(inter, width=30, bg="white", fg= "blue")
    nombre_del_denunciante.place(x=720, y=230)

    Cedula_del_denunciante= Label(inter, text="Cedula del denunciante:", width=18, height=2, bg="light blue", font=('Arial', '10'))
    Cedula_del_denunciante.place(x=950, y=205)
    cedula_del_denunciante= Entry(inter, width=30, bg="white", fg= "blue")
    cedula_del_denunciante.place(x=950, y=230)

    Descripcion_del_robo= Label(inter, text="Descripcion del robo:", width=15, height=2, bg="light blue", font=('Arial', '10'))
    Descripcion_del_robo.place(x=1160, y=205)
    descripcion_del_robo= Entry(inter, width=30, bg="white", fg= "blue")
    descripcion_del_robo.place(x=1160, y=230)

    Telefono= Label(inter, text="Telefono:", width=8, height=2, bg="light blue", font=('Arial', '10'))
    Telefono.place(x=30, y=290)
    telefono= Entry(inter, width=30, bg="white", fg= "blue")
    telefono.place(x=30, y=315)

    Provincia= Label(inter, text="Id Provincia:", width=8, height=2, bg="light blue", font=('Arial', '10'))
    Provincia.place(x=260, y=290)
    provincia= Entry(inter, width=30, bg="white", fg= "blue")
    provincia.place(x=260, y=315)

    Latitud= Label(inter, text="Latitud:", width=8, height=2, bg="light blue", font=('Arial', '10'))
    Latitud.place(x=500, y=290)
    latitud= Entry(inter, width=30, bg="white", fg= "blue")
    latitud.place(x=500, y=315)

    Longitud= Label(inter, text="Longitud:", width=8, height=2, bg="light blue", font=('Arial', '10'))
    Longitud.place(x=740, y=290)
    longitud= Entry(inter, width=30, bg="white", fg= "blue")
    longitud.place(x=740, y=315)

    Estado_del_vehiculo= Label(inter, text="Robado o Encontrado:", width=15, height=2, bg="light blue", font=('Arial', '10'))
    Estado_del_vehiculo.place(x=970, y=290)
    estado_del_vehiculo= Entry(inter, width=30, bg="white", fg= "blue")
    estado_del_vehiculo.place(x=970, y=315)

    Fecha_encuentro= Label(inter, text="Fecha de encuentro:", width=15, height=2, bg="light blue", font=('Arial', '10'))
    Fecha_encuentro.place(x=1160, y=290)
    fecha_encuentro= Entry(inter, width=30, bg="white", fg= "blue")
    fecha_encuentro.place(x=1160, y=315)

    Comentario_de_encuentro= Label(inter, text="Comentario de encuentro:", width=18, height=2, bg="light blue", font=('Arial', '10'))
    Comentario_de_encuentro.place(x=30, y=370)
    comentario_de_encuentro= Entry(inter, width=30, bg="white", fg= "blue")
    comentario_de_encuentro.place(x=30, y=395)

    Tabla_prov= Label(inter, text=Mostrar_prov(), width=50, height=15, bg="light green", font=('Arial', '10'))
    Tabla_prov.place(x=10, y=425)
    Tabla_prov= Label(inter, text=Mostrar_Marca(), width=50, height=15, bg="light green", font=('Arial', '10'))
    Tabla_prov.place(x=350, y=425)
    Tabla_prov= Label(inter, text=Mostrar_Modelo(), width=50, height=15, bg="light green", font=('Arial', '10'))
    Tabla_prov.place(x=650, y=425)

    Boton = Button(inter, text="Guardar",  bg="light green", font=('Bodoni', '12'), command=lambda:
    (guardar ()))
    Boton.place(x=350, y=380)






#Menu De Gestionar
def Gestionar():
    T = Tk()
    T.title ("B-SOFTWORLD")
    T.geometry('500x400')
    T.config(bg="light green")

    titulo=Label(T, text= "SELECCIONE LA OPCION QUE DESEE", width=35, height=2, bg="gray", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=2)

    button_agr_caso= Button(T, text= 'Agregar caso',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (Agregar_caso()))
    button_agr_caso.place(x=200, y=55)

    button_mod_caso= Button(T, text= 'Modificar caso',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (editar()))
    button_mod_caso.place(x=195, y=150)

    button_eli_caso= Button(T, text= 'Eliminar caso',  bg="light blue", font=('Bodoni', '12'),command=lambda:
    (eliminar()))
    button_eli_caso.place(x=202, y=250)
    
    titulo=Label(T, text= "B-SOFTWORLD", width=35, height=2, bg="blue", fg= "white", font=('Arial', '12'))
    titulo.place(x=100, y=350)


def cerrar():
    principal.destroy()

def acerca():
    import os
    prom=os.system("start https://youtu.be/ITyYIfgjYmI ")


#Menu Principal
principal = Tk()
principal.title ("B-SOFTWORLD")
principal.geometry('1350x700')
principal.config(bg="light blue")


titulo=Label(principal, text= "B-SOFTWORLD", width=20, height=2, bg="gray", fg= "white", font=('Arial', '12'))
titulo.place(x=595, y=15) 
titulo2=Label(principal, text= "POLICIA NACIONAL", width=20, height=1, bg="gray", fg= "black", font=('Arial', '12'))
titulo2.place(x=595, y=60)

button_Gestionar= Button(principal, text= 'Gestionar Casos',  bg="light green", font=('Bodoni', '12'), command=lambda:
(Gestionar()))
button_Gestionar.place(x=125, y=100)

button_vehiculo= Button(principal, text= 'Registrar vehiculo encontrado',  bg="light green", font=('Bodoni', '12'),command=lambda:
(vehiculo_en()))
button_vehiculo.place(x=350, y=100)

button_reporte= Button(principal, text= 'Reportar o mostrar caso',  bg="light green", font=('Bodoni', '12'),command=lambda:
(Reporte_casos()))
button_reporte.place(x=650, y=100)

button_Configuracion= Button(principal, text= 'Configurar casos',  bg="light green", font=('Bodoni', '12'),command=lambda:
(Configurar()))
button_Configuracion.place(x=895, y=100)

button_informacion= Button(principal, text= 'Acerca de',  bg="light green", font=('Bodoni', '12'),command=lambda:
(acerca()))
button_informacion.place(x=1100, y=100)

button_Salir= Button(principal, text= 'Salir',  bg="light green", font=('Bodoni', '12'),command=lambda:
(cerrar()))
button_Salir.place(x=695, y=650)



Imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\Young King\Documents\Fundametos_P\Final\Policia.png').resize((800,200)))
la=Label(image=Imagen)
la.place(x=275, y=300)

principal.resizable(False,False)
principal.mainloop()

