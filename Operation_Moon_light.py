#Como primera cosa, se realizara la implementación de la primera pantalla, esta vendrá con un boton para salir del juego
#Otro para poder ver los creditos, los cuales serían la porrtada, la escogencia de los 3 niveles ademas de un boton de start
#Tendrá un Entry para poder ingresar el nombre del jugador.

from tkinter import*
from PIL import ImageTk,Image
import random

#----------------------------Se declaran variables globales para que se puedan configurar sus valores a lo largo del codigo--------------------------------

global M_Scores
M_Scores = ""
global nivel
nivel = 1
global Score
Score = 0
global Live_level_1
Live_level_1 = 50
global Live_level_2
Live_level_2 = 50
global Live_level_3
Live_level_3 = 50
global Enemigo_live_1
Enemigo_live_1 = 30
global Enemigo_live_2
Enemigo_live_2 = 40
global Enemigo_live_3
Enemigo_live_3 = 50

#-----------------Pantalla principal en donde se encuentra el menu de juego------------------------------------------------------------------------------

class pantalla_principal:
    def __init__(self,master):
        self.sec1 = 0
        self.min1 = 0
        self.sec2 = 0
        self.min2 = 0
        self.sec3 = 0
        self.min3 = 0

#-----------------------------Se definen las canvas, estas son los cuadrados en donde se acomodan objetos de la pantalla---------------------------------

        self.master = master
        self.canvas = Canvas(master, width=370, height=580,highlightthickness=0)
        self.canvas.place(x=0, y=0)

#-----------------------------Configuracion de la imagen para poder acomodarse en la ventana-------------------------------------------------------------

        Tamaño = Canvas(self.canvas,width = 370, height=580,highlightthickness=0)
        Tamaño.pack(fill = "both", expand = True)
        Tamaño.create_image(54,100, image= bg)
#----------------------------------------------Titulo del juego------------------------------------------------------------------------------------------

        self.titulo = Label(self.canvas, text="OPERATION MOON LIGHT", font=("Vermin Vibes V", 16), bg='magenta4', fg='black')
        self.titulo.place(x=27.5, y=60, width=315, height=20)

#---------------------------------Label el cual contiene la instruccion para ingresar el nombre del jugador----------------------------------------------

        self.write_name = Label(self.canvas, text="Write your name ➟", font=("Vermin Vibes V", 7), bg='magenta4', fg='black')
        self.write_name.place(x=45, y=120)

#---------------------------------Txtbox para que el usuario pudeda escribir su nombre-------------------------------------------------------------------

        self.textbox_name = Entry(self.canvas, bd= 5, bg= "Mediumpurple3")
        self.textbox_name.place(x=180, y=116, width=140, height=25)

#------------Boton jugar, este boton es comandado por la funcion que abre los niveles del juego, De lo contrario no haría nada----------------------------

        self.button_jugar = Button(self.canvas, text="Play", font=("Vermin Vibes V", 10,), bg = "magenta4", fg= "black",relief="raised",borderwidth=6,
                                   command= self.abrir_niveles)
        self.button_jugar.place(x= 135,y=400, width=100, height=30)

# ----------------------------------------------------------------Boton scores-----------------------------------------------------------------------

        self.button_score = Button(self.canvas, text="Best Scores", font=("Vermin Vibes V", 10,), bg="magenta4", fg="black",
                                   relief="raised", borderwidth=6,command= self.abrir_scores)
        self.button_score.place(x=85, y=350, width=200, height=30)

#-Boton de creditos, comandado por la funcion "abrir_credits", esta hace que los objetos de la pantalla cambien y se cambien los objetos dentro de ella---

        self.button_credits = Button(self.canvas, text="Credits", font=("Vermin Vibes V", 7,), bg="magenta4", fg="black",relief="raised", borderwidth=6,
                                     command = self.abrir_credits)
        self.button_credits.place(x=75, y=530, width=100, height=30)

#-------------------------------------Boton de instrucciones comandado "instructions"-------------------------------------------------------------------

        self.botton_instructions = Button(self.canvas, text="instructions", font=("Vermin Vibes V", 7,), bg="magenta4", fg="black",relief="raised",
                                          borderwidth=6, command=self.instrcutions)
        self.botton_instructions.place(x=195, y=530, width=100, height=30)

#------------------------ Radiobottons con diferentes valores, esto es para que se pueda tener la escogencia de 3 niveles--------------------------------

        self.level1 = Radiobutton(self.canvas, text= "Level 1", value=1, variable= var,font=("Vermin Vibes V", 10), bg='magenta4', fg='black')
        self.level1.place (x=17, y=200, width=100, height=20)
        self.level2 = Radiobutton(self.canvas, text= "Level 2", value=2,variable= var,font= ("Vermin Vibes V", 10), bg='magenta4', fg='black')
        self.level2.place(x=135, y=200, width=100, height=20)
        self.level3 = Radiobutton(self.canvas, text= "Level 3", value= 3, variable= var, font= ("Vermin Vibes V",10), bg= "magenta4", fg="black")
        self.level3.place(x=253,y=200, width=100, height=20)

#----------------------------------Funcion para abrir los creditos cuando se preciona el boton de los creditos-------------------------------------------

    def abrir_credits(self):
           self.creditos()

#----------------------------------Pantala de creditos, se recicla la pantalla principal y se modifican los objetos---------------------------------------

    def creditos(self):
        master = self.master
        self.canvas = Canvas(master, width=370, height=580, highlightthickness=0)
        self.canvas.place(x=0, y=0)

#--------------------------------Configuracion del bg de la pantalla de creditos--------------------------------------------------------------------------

        Tamaño = Canvas(self.canvas, width=370, height=580, highlightthickness=0)
        Tamaño.pack(fill="both", expand=True)
        Tamaño.create_image(54, 100, image=bg)

#------------------------------------------Titulo de la pantalla------------------------------------------------------------------------------------------

        self.titulo_credits = Label(self.canvas, text="CREDITS", font=("Vermin Vibes V", 16), bg='magenta4',fg='white')
        self.titulo_credits.place(x=120, y=60, width=130, height=30)

#---------------------------------------------------Protada-----------------------------------------------------------------------------------------------


        self.pais = Label(self.canvas, text="Costa    Rica", font=("Vermin Vibes V", 10),bg= "magenta4",fg='black')
        self.pais.place(x=130, y=125, width= 110, height= 20)
        self.universidad = Label(self.canvas, text="INSTITUTO TECNÓLIGICO DE COSTA RICA", font=("Vermin Vibes V", 10), bg="magenta4",fg='black')
        self.universidad.place(x=25, y=175, width=320, height=20)
        self.carrera= Label(self.canvas, text="INGENIERIA EN COMPUTADORES", font=("Vermin Vibes V", 10),bg="magenta4", fg='black')
        self.carrera.place(x=50, y=225, width=260, height=20)
        self.curso = Label(self.canvas, text="TALLER DE PROGRAMACIÓN", font=("Vermin Vibes V", 10),bg="magenta4", fg='black')
        self.curso.place(x=72.5, y=275, width=225, height=20)
        self.dios = Label(self.canvas, text="PROFESOR: LUIS BARBOZA ARTAVIA", font=("Vermin Vibes V", 10), bg="magenta4",fg='black')
        self.dios.place(x=40, y=325, width=290, height=20)
        self.su_dicipulo = Label(self.canvas, text="ESTUDIANTE: ISAC MARÍN SIRIAS", font=("Vermin Vibes V", 10), bg="magenta4",fg='black')
        self.su_dicipulo.place(x=55, y=375, width=260, height=20)
        self.version = Label(self.canvas, text="PYTHON 3.9", font=("Vermin Vibes V", 10),bg="magenta4", fg='black')
        self.version.place(x=135, y=440, width=100, height=20)
        self.year= Label(self.canvas, text="2021", font=("Vermin Vibes V", 10), bg="magenta4", fg='black')
        self.year.place(x=48, y=475, width=85, height=20)
        self.grupo = Label(self.canvas, text="Grupo 4", font=("Vermin Vibes V", 10), bg="magenta4", fg='black')
        self.grupo.place(x=237, y=475, width=85, height=20)

#----------------------------------------Boton para poder devolverse al menu de inicio---------------------------------------------------------------------

        self.bo_exit_cre = Button(self.canvas, text= "EXIT", font=("Vermin Vibes V", 10,), bg = "magenta4", fg= "black",relief="raised",borderwidth=6,
                                  command= self.volver)
        self.bo_exit_cre.place(x=135, y=530, width=100, height=30)

#------------------------Funcion que hace que todos los botones de exit y menu, se devuelvan a la ventana principal----------------------------------------

    def volver(self):
        self.__init__(self.master)

#------------------------------------------Funcion para abrir los creditos---------------------------------------------------------------------------------

    def abrir_instructions(self):
        self.instrcutions()

#-----------------------------------------Pantalla con las intrucciones de juego--------------------------------------------------------------------------

    def instrcutions(self):
        master = self.master
        self.canvas = Canvas(master, width=370, height=580, highlightthickness=0)
        self.canvas.place(x=0, y=0)

# -----------------------------Configuracion de la imagen para poder acomodarse en la ventana------------------------------------------------------------

        Tamaño = Canvas(self.canvas, width=370, height=580, highlightthickness=0)
        Tamaño.pack(fill="both", expand=True)
        Tamaño.create_image(54, 100, image=bg)

#-------------------------------Titulo de la ventana---------------------------------------------------------------------------------------------------

        self.titulo_instructions= Label(self.canvas, text="INSTRUCTIONS", font=("Vermin Vibes V", 16), bg='magenta4',fg='white')
        self.titulo_instructions.place(x=85, y=60, width=200, height=20)

#--------------------Para evitar usar muchos labels, se utiliza el "Message" para poder escribir con mas libertad--------------------------------------
        #---------------------------------al final si use labels porque se veia muy feo--------------------------------

        self.bienvenida = Label(self.canvas, text= "Welcome  " + self.textbox_name.get(), font=("Vermin Vibes V", 7),bg = "magenta4")
        self.bienvenida.place(x=115, y=130, width=140, height=20)
        self.intructions1 = Label(self.canvas, text= "Operation Moon Light is a shooting game.",font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions1.place(x=50, y=170, width=270, height=20)
        self.intructions2 = Label(self.canvas, text= "Whit it you can enjoy three different levels,"
                                                     "\n which as you progress,"
                                  ,font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions2.place(x=35, y=210, width=300, height=20)
        self.intructions3 = Label(self.canvas, text = "you will have a greater degree of difficulty.",
                                  font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions3.place(x=35, y=250, width=300, height=20)
        self.intructions4 = Label(self.canvas, text = "To control your spaceship.",
                                  font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions4.place(x=85, y=290, width=200, height=20)
        self.intructions5 = Label(self.canvas, text = "You must use the keys: ←,→ ,↓  and ↑ .",
                                  font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions5.place(x=60, y=330, width=250, height=20)
        self.intructions6 = Label(self.canvas, text = "In addition to this, use the space key \n"
                                                      "to fire all your projectiles."
                                  ,font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions6.place(x=60, y=370, width=250, height=20)
        self.intructions7 = Label(self.canvas, text = "Defeat all the bosses and get the victory.",
                                  font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions7.place(x=35, y=410, width=300, height=20)
        self.intructions8 = Label(self.canvas, text = "I wish you luck soldier  " + self.textbox_name.get(),
                                  font=("Vermin Vibes V", 7), bg="magenta4", fg='black')
        self.intructions8.place(x=60, y=450, width=250, height=20)

#------------------------------------------------Boton para volver al menú de incio---------------------------------------------------------------------
        self.bo_exit_isntructions = Button(self.canvas, text= "EXIT", font=("Vermin Vibes V", 10,),
                                           bg = "magenta4", fg= "black",relief="raised",borderwidth=6,command= self.volver)
        self.bo_exit_isntructions.place(x=135, y=530, width=100, height=30)

#---------------------------------------------------------------Tabla de puntuacion----------------------------------------------------------------------
    def abrir_scores(self):
        self.best_scores()

    def best_scores(self):
        master = self.master
        self.canvas = Canvas(master, width=370, height=580, highlightthickness=0)
        self.canvas.place(x=0, y=0)

# -----------------------------Configuracion de la imagen para poder acomodarse en la ventana------------------------------------------------------------

        self.background = self.canvas.create_image(45, 286, image=bg)

        self.Nave_player_score = ImageTk.PhotoImage(Image.open("Nave_player_1.png"))
        self.nave_score = self.canvas.create_image(240, 480, image=self.Nave_player_score)

        self.Nave_enemiga_score = ImageTk.PhotoImage(Image.open("Nave_enemiga.png")) # Se declara la imagen en el canvas
        self.enemiga_score = self.canvas.create_image(130, 480, image= self.Nave_enemiga_score)

        self.barra_superior = LabelFrame(self.canvas, width=370, height=30, highlightthickness=0, bg="magenta4",
                                         relief="raised", borderwidth=2)
        self.barra_superior.place(x=0, y=0)

        self.scores_txt = Message(self.canvas,text = str(M_Scores), font=("Vermin Vibes V", 10), bg="magenta4", fg="black")
        self.scores_txt.place(x= 85, y= 100, width = 200, height= 300)

        # Boton Menú
        self.bo_menu = Button(self.canvas, text="Menu", font=("Vermin Vibes V", 7), bg="magenta4", fg="black",
                              relief="raised", borderwidth=5,
                              command=self.volver)
        self.bo_menu.place(x=152.5, y=2.5, width=65, height=25)

        self.barra_de_info = LabelFrame(self.canvas, width=370, height=50, highlightthickness=0, bg="magenta4",
                                        relief="raised", borderwidth=6)
        self.barra_de_info.place(x=0, y=530)

        self.texto = Label(text=  "You are a winner?" ,  font=("Vermin Vibes V", 12), bg="magenta4", fg="black")
        self.texto.place(x=50, y=540, width=270, height=30)


    #-----------------------Aquí empezamos con lo divertido y lo que muy seguramente me quitará el sueño por lo menos esta semana------------------------------
    #---------------------------Actualizo la informacion, esta parte me ha quitado las dos semanas de sueño  :3--------------------------------------------


#-----------------------------Esta funcion permite abrir los niveles, funciona por los valores enteros de la variable--------------------------------------
    def abrir_niveles(self):
        global nivel

        if self.textbox_name.get() != "" and var.get() == 1:
           #print(var.get())
           nivel = 1
           self.pantalla_nivel1()

        elif self.textbox_name.get() != "" and var.get() == 2:
            #print(var.get())
            nivel = 2
            self.pantalla_nivel2()

        elif self.textbox_name.get() != "" and var.get() == 3:
            #print(var.get())
            nivel = 3
            self.pantalla_nivel3()

        elif self.textbox_name.get() != "":
            self.pantalla_nivel1()

#---------------------------------------------------------Flags de pantallas de juego----------------------------------------------------------------------
        self.flag_pantalla = False
#----------------------------------------------------------Pantalla de juego con el nivel 1---------------------------------------------------------------

    def pantalla_nivel1(self):
        self.flag_pantalla = False
        self.canvas = Canvas(self.master, width=370, height=580, highlightthickness=0)
        self.canvas.place(x=0, y=0)

#---------------------------------------------------Imagen de la pantalla de juego o background------------------------------------------------------------

        self.background = self.canvas.create_image(45, 286, image=bg)

#----------------------------------------------------------Imagen con la nave del jugador------------------------------------------------------------------

        self.Nave_player = ImageTk.PhotoImage(Image.open("Nave_player_1.png")) # Se declara la imagen dentro del canvas
        self.nave = self.canvas.create_image(186, 490, image=self.Nave_player) # Se acomoda la imagen

#------------------------------------------------------------Bala del jugador------------------------------------------------------------------------------

        self.Bala_jugador = PhotoImage(file="Bala.png")# Se declara la imagen dentro del canvas
        self.Bala = self.canvas.create_image(350, 780, image=self.Bala_jugador)# Se acomoda la imagen

#-----------------------------------------------------Imagen con la nave del enemigo-----------------------------------------------------------------------

        self.Nave_enemiga = ImageTk.PhotoImage(Image.open("Nave_enemiga.png")) # Se declara la imagen en el canvas
        self.enemiga = self.canvas.create_image(185, 100, image= self.Nave_enemiga) # Se acomoda la imagen dentro de la pantalla
        self.coordenadas = self.canvas.coords(self.nave)
        #print(self.coordenadas)

        #Las dos lineas anteriores, sacan he imprimen las coordenadas de la nave, esto me ayudó mucho para poder delimitar los espacios en donde
        #la nave se va a mover

#------------------los Flags, sirven para poder dar una pausa en las acciones y darle paso a los condicionales que están abajo-----------------------------

        self.flag= False
        self.flag_disparo = False
        self.flag_embestida = False
        self.flag_sec = False
        self.movey = 10
        self.Subir = False
#---------------------------------------------Esta funcion hace que el jefe se pueda mover a hacia los lados ----------------------------------------------

        def movd():
            global nivel
            self.coords_enemigo = self.canvas.coords(self.enemiga) #Coordenadas del enemigo, estas sirven para poder saber en donde limitar el mov
            mx = 1    # el numero positivo es para que vaya hacia la derecha.
            my = 1
            rannnndom =  random.randint(1,10)
            print(rannnndom)
            #print(rannnndom)
            #print(self.flag_embestida)
            if self.flag_embestida == False and nivel == 1:
                if self.coords_enemigo[0] == 319:
                    self.flag = True #el flag cambia a ser verdadero
                if self.flag:  # ¿y que significa que sea verdadero?
                    mx = -1  # Que su valor va a cambiar de un numero positivo, a un numero negativo para que pueda ir hacia la izquierda
                if self.coords_enemigo[0] == 49:
                    self.flag = False
                if self.sec1 % 2 == 0 and self.sec1 > 0 and rannnndom % 3 == 0:
                    self.flag_embestida = True
                    embestida()
                    self.canvas.after(10, movd)

                else:
               # print("si me ejecuté")

                    self.canvas.move(self.enemiga, mx, 0) #"move" permita que se mueva la imagen enemiga con el movimiento del eje x
                    self.canvas.after(10, movd) #La funcion se ejecuta cada milisegundo

        def embestida():
            self.bbox_nave = self.canvas.bbox(self.nave)
            self.bbox_enemy = self.canvas.bbox((self.enemiga))
            self.coords_enemigo = self.canvas.coords(self.enemiga)
            if self.coords_enemigo[1] >= 490 and self.Subir == False:
                #print("Sigo estando harto")
                self.Subir= True
                vida_enemy()
                self.movey = -10
                self.canvas.move(self.enemiga, 0, self.movey)
                self.canvas.after(10, embestida)
                if (self.bbox_enemy[2] > self.bbox_nave[0] > self.bbox_enemy[0]) and \
                        (self.bbox_enemy[1] < self.bbox_nave[3] < self.bbox_enemy[3]):  # Colision entre la nave enemiga y la nave del jugador
                    vida_player()
                    siguiente_nivel2()
            elif self.coords_enemigo[1] <= 100 and self.Subir == True:
                self.movey = 10
                self.Subir= False
                self.flag_embestida = False
                return movd()
            else:
                self.canvas.move(self.enemiga, 0,self.movey)
                self.canvas.after(10, embestida)

#-------------------------------Se realiza la funcion para que cuando se preciona la tecla left, la nave player, se mueva---------------------------------

        def left(event):
            #print(self.coordenadas)
            x,y = self.canvas.coords(self.nave) # x and y == coordenadas[0] y [1]
            if event.keysym == "Left" and x >= 36:
                self.canvas.coords(self.nave, x -10, y)
                self.coordenadas = self.canvas.coords(self.nave)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla Right, la nave player, se mueva---------------------------------

        def right(event):
            #print(self.coordenadas)
            x, y = self.canvas.coords(self.nave)

            if event.keysym == "Right" and x <= 335:
                self.canvas.coords(self.nave, x + 10, y)
                self.coordenadas = self.canvas.coords(self.nave)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla Up, la nave player, se mueva---------------------------------
        def up(event):
            # print(self.coordenadas)
            x, y = self.canvas.coords(self.nave)

            if event.keysym == "Up" and y >= 175:
                self.canvas.coords(self.nave, x, y - 10)
                self.coordenadas = self.canvas.coords(self.nave)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla down, la nave player, se mueva---------------------------------

        def down(event):
            x, y = self.canvas.coords(self.nave)
            if event.keysym == "Down" and y <= 490:
                self.canvas.coords(self.nave, x, y + 10)
                self.coordenadas = self.canvas.coords(self.nave)

        def disparo():
            global nivel
            if nivel == 1:
                self.colicion_enemicoords = self.canvas.bbox(self.enemiga)
                self.colicion_bala_coords = self.canvas.bbox(self.Bala)
               # print(self.colicion_enemicoords)
                self.coords_enemigo = self.canvas.coords(self.enemiga)
                self.coords_bala = self.canvas.coords(self.Bala)
                movimiento_de_disparo = 10
                if self.coords_bala[1] <= 0:
                    self.flag_disparo = False
                if (self.colicion_enemicoords[2]> self.colicion_bala_coords[0]>self.colicion_enemicoords[0]) and \
                        (self.colicion_enemicoords[1]<self.colicion_bala_coords[3]<self.colicion_enemicoords[3]):
                    self.canvas.move(self.Bala, -1000000, -10)
                    score()
                    vida_enemy()
                    siguiente_nivel2()
                    self.flag_disparo = False

                else:
                    if self.coords_bala[1] >= movimiento_de_disparo:
                        self.flag_disparo = True

                    if self.flag_disparo:
                        movimiento_de_disparo= -10
                    self.canvas.move(self.Bala, 0, movimiento_de_disparo)
                    self.canvas.after(10, disparo)

        def vida_enemy():
            global Enemigo_live_1
            if Live_level_1 != 0:
                Enemigo_live_1 -= 1
                self.label_liveE.config(text= "Enemy: " + str(Enemigo_live_1))
            if Live_level_1 == 0:
                score_guardar()
                self.game_over.config(text= "GAME OVER")

        def vida_player():
            global Live_level_1
            if Live_level_1 != 0:
                Live_level_1 -= 10
                self.label_live_jugador.config(text= "live: " + str(Live_level_1))


        def score():
            global Score
            if Live_level_1 != 0:
                Score += 3
                self.label_score.config(text="Score: " + str(Score))
                if Live_level_1 == 50:
                    Score += 10
                    self.label_score.config(text="Score: " + str(Score))
                    score_guardar()


        def siguiente_nivel2():
            global nivel
            if Enemigo_live_1 == 0:
                nivel += 1
                self.pantalla_nivel2()

        def score_guardar():
            global M_Scores
            if Live_level_1 or Live_level_2 or Live_level_3 == 0:
                Best_scores = (str(self.textbox_name.get()) + ":" + str(Score) + "\n")
                guardar = open("Scorest.txt", "a")
                guardar.write(Best_scores)
                M_Scores = Best_scores
                guardar.close()
#------------------------------------------------------Validación para poder disparar---------------------------------------------------------------------

        def accion_disparo(event):
            if event.keysym == 'space':
                x, y = self.canvas.coords(self.nave)
                self.canvas.coords(self.Bala, x, y + 25)
                return disparo()

#----------------------- Los .bind, sirven para indicar cuando una teca se preciona, ademas de que llama a las funciones de movimeinto--------------------

        self.master.bind("<Left>", left)
        self.master.bind("<Right>", right)
        self.master.bind("<Up>", up)
        self.master.bind("<Down>", down)
        self.master.bind("<space>", accion_disparo)
        movd()
        #embestida()



#--------------------------------------------------barra superior, en donde se encuentra el boton del menu-------------------------------------------------

        self.barra_superior = LabelFrame(self.canvas, width=370, height=30, highlightthickness=0, bg="magenta4",
                                 relief="raised", borderwidth=2)
        self.barra_superior.place(x=0, y=0)

#-------------------------------------------------Barra de informacion en donde está la informacion de juego-----------------------------------------------

        self.barra_de_info = LabelFrame(self.canvas, width=370, height=50, highlightthickness=0, bg="magenta4",
                                 relief="raised", borderwidth=6)
        self.barra_de_info.place(x=0, y=530)

#----------------------------------------------------------Label con el puntaje del jugador----------------------------------------------------------------

        self.label_score = Label(self.canvas, text="Score: " + str(Score), font=("Vermin Vibes V", 6), bg='magenta4',
                                 fg='white')
        self.label_score.place(x=5, y=550)

# ----------------------------------------------------------Label con la vida del jugador----------------------------------------------------------------

        self.label_live_jugador = Label(self.canvas, text="Live:50", font=("Vermin Vibes V", 6), bg='magenta4',
                                 fg='white')
        self.label_live_jugador.place(x=60, y=550)

# ----------------------------------------------------------Label con la vida del enemigo----------------------------------------------------------------
        self.label_liveE = Label(self.canvas, text="Enemy: 30", font=("Vermin Vibes V", 6),
                                 bg='magenta4',
                                 fg='white')
        self.label_liveE.place(x=110, y=550)

# ---------------------------------------------------Label con el nombre del jugador actual----------------------------------------------------------------
        self.label_name_player = Label(self.canvas, text="Player: " + self.textbox_name.get(), font=("Vermin Vibes V", 6),
                                bg='magenta4',
                                 fg='white')
        self.label_name_player.place(x=175, y=550)

#-------------------------------------------------Forma del enemigo en la barra de progreso-----------------------------------------------------------------


        #-------------------------------------------------Se abre la imgaen del enemigo---------------------------------------------------------------
        self.i_enemigo = Image.open("Nave_enemiga.png")

        # -------------------------------------------Se redimenziona las imagen con el atributo resize----------------------------------------

        self.redimension = self.i_enemigo.resize((25, 25), Image.ANTIALIAS)

        self.new_i_enemigo = ImageTk.PhotoImage(self.redimension)

        #---------------------------------------Se declara la imagen dentro del canvas como un label-------------------------------------------

        self.i_enemigo = ImageTk.PhotoImage(file=r"C:\Users\User\PycharmProjects\ProyectoTaller_Operation_moon_light\Nave_enemiga.png")
        self.label_i_enemigo = Label(image=self.new_i_enemigo, bg="magenta4")
        self.label_i_enemigo.place(x=330, y=540)
#-----------------------------------------------------Boton para volver al menú de inicio------------------------------------------------------------

        self.bo_menu = Button(self.canvas, text="Menu", font=("Vermin Vibes V", 7), bg="magenta4", fg="black",
                              relief="raised", borderwidth=5,
                              command=self.volver)
        self.bo_menu.place(x=152.5, y=2.5, width=65, height=25)

#--------------------------------------------------------Tiempo de juego transcurrido--------------------------------------------------------------------

        #--------------------------------------------------------------label time---------------------------------------------------------------

        self.label_time = Label(self.canvas, text="Time", font=("Vermin Vibes V", 6),
                                bg='magenta4',
                                fg='white')
        self.label_time.place(x=260, y=550)

        #---------------------------------------------------------label minutos------------------------------------------------------------------

        self.minutos1 = Label(self.canvas, text=int("0"), font=("Vermin Vibes V", 6),
                             bg='magenta4',
                             fg='white')
        self.minutos1.place(x=290, y=550)

        #-----------------------------------------------------------label ":"------------------------------------------------------------------------

        self.label_divi = Label(self.canvas, text=":", font=("Vermin Vibes V", 6),
                                bg='magenta4',
                                fg='white')
        self.label_divi.place(x=300, y=550)

        #---------------------------------------------------------label segundos---------------------------------------------------------------------

        self.segundos1 = Label(self.canvas, text="Level 1", font=("Vermin Vibes V", 6),
                              bg='magenta4',
                              fg='white')
        self.segundos1.place(x=305, y=550)
        self.level_l1 = Label(text="Level 1", font=("Vermin Vibes V", 7), bg="magenta4", fg="black")
        self.level_l1.place(x=45, y=2.5, width=80, height=25)
        self.game_over  = Label(text = "", font=("Vermin Vibes V", 7), bg="magenta4", fg="black")
        self.game_over.place(x=270, y=2.5, width=80, height=25)

#-------------------------Variables en las cuales se van a guardar los datos que se van configurando o sumando---------------------------------


        self.contar_segundos1()

#------------------------------------------------Funcion para contar segundos y minutos-------------------------------------------------------------------
    def contar_segundos1(self):
        if self.sec1 != 60:
            self.sec1 += 1
            self.zero1 = ""
            if 0 <= self.sec1 < 10:
                self.zero1 = "0" + str(self.sec1)
            else:
                self.zero1 = str(self.sec1)
            self.segundos1.configure(text=self.zero1)
            self.canvas.after(1000, self.contar_segundos1)
        if self.sec1 == 60:
            self.sec1 = 0
            self.min1 += 1
            self.minutos1.configure(text=self.min1)

    #Esta funcion trabajda de la siguiente manera:
    # Cuando la variable segundos es diferente de 60, este se configurará sumando 1, ademas de esto para poder poner un cero al principio
    #se valida que si segundos en menor a diez y mayor o igua a cero, este pondrá un cero al principio
    #De lo contrario se seguirá sumando 1 para poder dar digitos como el 11,26,54, por dar un ejemplo
    #Una vez que los segundos llegan a 60, la variable de los minutos sumará +1 y se configurará el label de los minutos



#Pantalla de juego 2
    def pantalla_nivel2(self):

        master = self.master
        self.canvas = Canvas(master, width=370, height=580, highlightthickness=0)
        self.canvas.place(x=0, y=0)

# ---------------------------------------------------Imagen de la pantalla de juego o background------------------------------------------------------------

        self.background2 = self.canvas.create_image(45, 286, image=bg)

# ----------------------------------------------------------Imagen con la nave del jugador------------------------------------------------------------------

        self.Nave_player2 = ImageTk.PhotoImage(Image.open("Nave_player_1.png"))  # Se declara la imagen dentro del canvas
        self.nave2 = self.canvas.create_image(186, 490, image=self.Nave_player2)  # Se acomoda la imagen

# ------------------------------------------------------------Bala del jugador------------------------------------------------------------------------------

        self.Bala_jugador2 = PhotoImage(file="Bala.png")  # Se declara la imagen dentro del canvas
        self.Bala2 = self.canvas.create_image(350, 780, image=self.Bala_jugador2)  # Se acomoda la imagen

# -----------------------------------------------------Imagen con la nave del enemigo-----------------------------------------------------------------------

        self.Nave_enemiga2 = ImageTk.PhotoImage(Image.open("Nave_enemiga.png"))  # Se declara la imagen en el canvas
        self.enemiga2 = self.canvas.create_image(185, 100,
                                                image=self.Nave_enemiga2)  # Se acomoda la imagen dentro de la pantalla
        self.coordenadas2 = self.canvas.coords(self.nave2)
        # print(self.coordenadas)

# Las dos lineas anteriores, sacan he imprimen las coordenadas de la nave, esto me ayudó mucho para poder delimitar los espacios en donde
# la nave se va a mover

        self.bala_enemy_image = PhotoImage(file="bala_enemy.png")  # Se declara la imagen dentro del canvas
        self.bala_enemy = self.canvas.create_image(10, 10, image=self.bala_enemy_image)

# ------------------los Flags, sirven para poder dar una pausa en las acciones y darle paso a los condicionales que están abajo-----------------------------

        self.flag2 = False
        self.flag_disparo2 = False
        self.flag_enemy_shot = False

# ---------------------------------------------Esta funcion hace que el jefe se pueda mover a hacia los lados ----------------------------------------------
#-----------------------------Estas dos funciones dependen una de la otra, la primera gernera a que velodidad y cada tanto tiempo se va a mover -------------------
        def teletransporte():
            movimiento()
            xe2, ye2 = self.canvas.coords(self.enemiga2)
            self.canvas.coords(self.bala_enemy, xe2, ye2-100)
            self.canvas.coords(self.enemiga2, xe2, ye2)
#-------------------------------------------------------------- 3 disparos por segundo--------------------------------------------------------------
            self.canvas.after(500, disparo_ememy)
            self.canvas.after(500, disparo_ememy)
            self.canvas.after(500, disparo_ememy)
            self.canvas.after(2000, teletransporte)

#--------------------------------------------------------------funcion que genera el numero random--------------------------------------------------------

        def movimiento():
            self.movex = random.randint(49,319)
            self.canvas.coords(self.enemiga2, self.movex,100)

#------------------------------------------------------------------disparo por parte de la nave enemiga.--------------------------------------------------------
        def disparo_ememy():
            self.colicion_enemicoords2 = self.canvas.bbox(self.nave2)
            self.colicion_bala_coords2 = self.canvas.bbox(self.bala_enemy)
            self.coords_enemigo2 = self.canvas.coords(self.nave2)
            self.coords_bala2 = self.canvas.coords(self.bala_enemy)
            #print(self.coords_bala2)
            m_shot_enemy= 10
            if self.coords_bala2[1] >= 580:
                xe2, ye2 = self.canvas.coords(self.enemiga2)

                self.canvas.coords(self.bala_enemy, xe2, ye2 )
                self.flag_enemy_shot = False
                return
            if (self.colicion_enemicoords2[2] > self.colicion_bala_coords2[0] > self.colicion_enemicoords2[0]) and (
                    self.colicion_enemicoords2[1] < self.colicion_bala_coords2[3] < self.colicion_enemicoords2[3]):
                self.canvas.move(self.bala_enemy, -1000000,-10)
                vida_player2()
                self.flag_enemy_shot= False
                return

            else:
                if self.coords_bala2[1] >= m_shot_enemy:
                    self.flag_enemy_shot = True

                if self.flag_disparo2:
                    m_shot_enemy = 10
                self.canvas.move(self.bala_enemy, 0, m_shot_enemy)
                self.canvas.after(10, disparo_ememy)



# -------------------------------Se realiza la funcion para que cuando se preciona la tecla left, la nave player, se mueva---------------------------------

        def left2(event):
            # print(self.coordenadas)
            x2,y2 = self.canvas.coords(self.nave2)  # x and y == coordenadas[0] y [1]
            if event.keysym == "Left" and x2 >= 36:
                self.canvas.coords(self.nave2, x2 - 10, y2)
                self.coordenadas2 = self.canvas.coords(self.nave2)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla Right, la nave player, se mueva---------------------------------

        def right2(event):
            # print(self.coordenadas)
            x2, y2 = self.canvas.coords(self.nave2)

            if event.keysym == "Right" and x2 <= 335:
                self.canvas.coords(self.nave2, x2 + 10, y2)
                self.coordenadas2 = self.canvas.coords(self.nave2)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla Up, la nave player, se mueva---------------------------------
        def up2(event):
            # print(self.coordenadas)
            x2, y2 = self.canvas.coords(self.nave2)

            if event.keysym == "Up" and y2 >= 175:
                self.canvas.coords(self.nave2, x2, y2 - 10)
                self.coordenadas2 = self.canvas.coords(self.nave2)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla down, la nave player, se mueva---------------------------------

        def down2(event):
            x2, y2 = self.canvas.coords(self.nave2)
            if event.keysym == "Down" and y2 <= 490:
                self.canvas.coords(self.nave2, x2, y2 + 10)
                self.coordenadas2 = self.canvas.coords(self.nave2)

#---------------------------------------funcion para que la nave pueda diasparar proyectiles a la nave enemiga------------------------------

        def disparo2():
            global nivel
            if nivel == 2:
                self.colicion_enemicoords2 = self.canvas.bbox(self.enemiga2)
                self.colicion_bala_coords2 = self.canvas.bbox(self.Bala2)
                self.coords_enemigo2 = self.canvas.coords(self.enemiga2)
                self.coords_bala2 = self.canvas.coords(self.Bala2)
                movimiento_de_disparo2 = 10
                if self.coords_bala2[1] <= 0:
                    print(self.colicion_bala_coords2)
                    self.flag_disparo2 = False
                    return
                if (self.colicion_enemicoords2[2] > self.colicion_bala_coords2[0] > self.colicion_enemicoords2[0]) and \
                        (self.colicion_enemicoords2[1] < self.colicion_bala_coords2[3] < self.colicion_enemicoords2[3]):
                    self.canvas.move(self.Bala2, -10000, -10)
                    vida_enemy2()
                    score2()
                    siguiente_nivel3()
                    self.flag_disparo2 = False
                    return

                else:
                    if self.coords_bala2[1] >= movimiento_de_disparo2:
                        self.flag_disparo2 = True

                    if self.flag_disparo2:
                        movimiento_de_disparo2 = -10
                    self.canvas.move(self.Bala2, 0, movimiento_de_disparo2)
                    self.canvas.after(10, disparo2)


# ------------------------------------------------------Validación para poder disparar---------------------------------------------------------------------

        def accion_disparo2(event):
            global nivel
            if nivel ==2:
                if event.keysym == 'space':
                    x2, y2 = self.canvas.coords(self.nave2)
                    self.canvas.coords(self.Bala2, x2, y2 + 25)
                    return disparo2()

#-------------------------------funcion para bajar la vida del enemigo en el nivel dos y que se vea reflejado en el contador de vida enemiga-----------------------------

        def vida_enemy2():
            global Enemigo_live_2
            if Live_level_2 != 0:
                Enemigo_live_2 -= 1
                self.label_liveE2.config(text="Enemy: " + str(Enemigo_live_2))

        def vida_player2():
            global Live_level_2
            if Live_level_2 != 0:
                Live_level_2 -= 3
                self.label_live_jugador2.config(text="live: " + str(Live_level_2))
                if Live_level_2 <= 0:
                    score_guardar2()
                    self.game_over2.config(text="GAME OVER")

        def score2():
            global Score
            if Live_level_2 != 0:
                Score += 3
                self.label_score2.config(text="Score: " + str(Score))
                if Live_level_2 == 50:
                    Score += 10
                    self.label_score2.config(text="Score: " + str(Score))
                    score_guardar2()

        def siguiente_nivel3():
            global nivel
            if Enemigo_live_2 == 0:
                nivel += 1
                self.pantalla_nivel3()

        def score_guardar2():
            global M_Scores
            if Live_level_1 or Live_level_2 or Live_level_3 == 0:
                Best_scores = (str(self.textbox_name.get()) + ":" + str(Score) + "\n")
                guardar = open("Scorest.txt", "a")
                guardar.write(Best_scores)
                M_Scores = Best_scores
                guardar.close()

# ----------------------- Los .bind, sirven para indicar cuando una teca se preciona, ademas de que llama a las funciones de movimeinto--------------------

        self.master.bind("<Left>", left2)
        self.master.bind("<Right>", right2)
        self.master.bind("<Up>", up2)
        self.master.bind("<Down>", down2)
        self.master.bind("<space>", accion_disparo2)
        teletransporte()
# --------------------------------------------------barra superior, en donde se encuentra el boton del menu-------------------------------------------------

        self.barra2_superior = LabelFrame(self.canvas, width=370, height=30, highlightthickness=0, bg="magenta4",
                                         relief="raised", borderwidth=2)
        self.barra2_superior.place(x=0, y=0)

# -------------------------------------------------Barra de informacion en donde está la informacion de juego-----------------------------------------------

        self.barra2_de_info = LabelFrame(self.canvas, width=370, height=50, highlightthickness=0, bg="magenta4",
                                        relief="raised", borderwidth=6)
        self.barra2_de_info.place(x=0, y=530)

# ----------------------------------------------------------Label con el puntaje del jugador----------------------------------------------------------------

        self.label_score2 = Label(self.canvas, text="Score:" + str(Score), font=("Vermin Vibes V", 6), bg='magenta4',
                                fg='white')
        self.label_score2.place(x=5, y=550)

# ----------------------------------------------------------Label con la vida del jugador----------------------------------------------------------------

        self.label_live_jugador2 = Label(self.canvas, text="Live: 50", font=("Vermin Vibes V", 6),
                                        bg='magenta4',
                                        fg='white')
        self.label_live_jugador2.place(x=60, y=550)

# ----------------------------------------------------------Label con la vida del enemigo----------------------------------------------------------------
        self.label_liveE2 = Label(self.canvas, text="Enemy: 40", font=("Vermin Vibes V", 6),
                                 bg='magenta4',
                                 fg='white')
        self.label_liveE2.place(x=110, y=550)

# ---------------------------------------------------Label con el nombre del jugador actual----------------------------------------------------------------
        self.label_name_player2 = Label(self.canvas, text="Player: " + self.textbox_name.get(),
                                       font=("Vermin Vibes V", 6),
                                       bg='magenta4',
                                       fg='white')
        self.label_name_player2.place(x=175, y=550)

# -------------------------------------------------Forma del enemigo en la barra de progreso-----------------------------------------------------------------

# -------------------------------------------------Se abre la imgaen del enemigo---------------------------------------------------------------
        self.i_enemigo2 = Image.open("Nave_enemiga.png")

# -------------------------------------------Se redimenziona las imagen con el atributo resize----------------------------------------

        self.redimension2 = self.i_enemigo2.resize((25, 25), Image.ANTIALIAS)

        self.new_i_enemigo2 = ImageTk.PhotoImage(self.redimension2)

# ---------------------------------------Se declara la imagen dentro del canvas como un label-------------------------------------------

        self.i_enemigo2 = ImageTk.PhotoImage(
            file=r"C:\Users\User\PycharmProjects\ProyectoTaller_Operation_moon_light\Nave_enemiga.png")
        self.label_i_enemigo2 = Label(image=self.new_i_enemigo2, bg="magenta4")
        self.label_i_enemigo2.place(x=330, y=540)
# -----------------------------------------------------Boton para volver al menú de inicio------------------------------------------------------------
        self.level_l2 = Label(text="Level 2", font=("Vermin Vibes V", 7), bg="magenta4", fg="black")
        self.level_l2.place(x=45, y=2.5, width=80, height=25)
        self.game_over2 = Label(text="", font=("Vermin Vibes V", 7), bg="magenta4", fg="black")
        self.game_over2.place(x=270, y=2.5, width=80, height=25)


        self.bo_menu2 = Button(self.canvas, text="Menu", font=("Vermin Vibes V", 7), bg="magenta4", fg="black",
                              relief="raised", borderwidth=5,
                              command=self.volver)
        self.bo_menu2.place(x=152.5, y=2.5, width=65, height=25)

# --------------------------------------------------------Tiempo de juego transcurrido--------------------------------------------------------------------

        # label time
        self.label_time2 = Label(self.canvas, text="Time", font=("Vermin Vibes V", 6),
                                bg='magenta4',
                                fg='white')
        self.label_time2.place(x=260, y=550)

        self.minutos2 = Label(self.canvas, text=int("0"), font=("Vermin Vibes V", 6),
                             bg='magenta4',
                             fg='white')
        self.minutos2.place(x=290, y=550)

        # label ":"
        self.label_divi2 = Label(self.canvas, text=":", font=("Vermin Vibes V", 6),
                                bg='magenta4',
                                fg='white')
        self.label_divi2.place(x=300, y=550)

        # segundos
        self.segundos2 = Label(self.canvas, text="", font=("Vermin Vibes V", 6),
                              bg='magenta4',
                              fg='white')
        self.segundos2.place(x=305, y=550)

# -------------------------Variables en las cuales se van a guardar los datos que se van configurando o sumando---------------------------------


        self.contar_segundos2()

# ------------------------------------------------Funcion para contar segundos y minutos-------------------------------------------------------------------
    def contar_segundos2(self):
        if self.sec2 != 60:
            self.sec2 += 1
            self.zero2 = ""
            if 0 <= self.sec2 < 10:
                self.zero2 = "0" + str(self.sec2)
            else:
                self.zero2 = str(self.sec2)
            self.segundos2.configure(text=self.zero2)
            self.canvas.after(1000, self.contar_segundos2)
        if self.sec2 == 60:
            self.sec2 = 0
            self.min2 += 1
            self.minutos2.configure(text=self.min2)

#-----------------------------------------------------------------Pantalla con el tercer nivel------------------------------------------------

    def pantalla_nivel3(self):
        W = 370
        H= 580
        master = self.master
        self.canvas = Canvas(master, width=W, height=H, highlightthickness=0, bg = "gray3")
        self.canvas.place(x=0, y=0)

#---------------------------------background------------------------------------------------------------
        self.background3 = self.canvas.create_image(45, 286, image=bg)

#-------------------------------imagen de la nave del jugador----------------------------------------------------------------------
        self.Nave_player3 = ImageTk.PhotoImage(Image.open("Nave_player_1.png"))
        self.nave3 = self.canvas.create_image(186, 490, image=self.Nave_player3)

#-------------------------------------------bala del jugador----------------------------------------------

        self.Bala_jugador3 = PhotoImage(file="Bala.png")
        self.Bala3 = self.canvas.create_image(350, 780, image=self.Bala_jugador3)

#----------------------------------------- Nave enemiga------------------------------------------
        self.Nave_enemiga3 = ImageTk.PhotoImage(Image.open("Nave_enemiga.png"))
        self.enemiga3 = self.canvas.create_image(185, 100, image= self.Nave_enemiga3)
        self.coordenadas = self.canvas.coords(self.nave3)

        self.bala_enemy_image3 = PhotoImage(file="bala_enemy.png")  # Se declara la imagen dentro del canvas
        self.bala_enemy3 = self.canvas.create_image(10, 10, image=self.bala_enemy_image3)

        # ------------------los Flags, sirven para poder dar una pausa en las acciones y darle paso a los condicionales que están abajo-----------------------------

        self.flag3 = False
        self.flag_embestida3 = False
        self.flag_sec3 = False
        self.movey3 = 10
        self.estoy_subir = False
        self.flag_enemy_shot3 = False
        self.flag_disparo3 = False
        self.disparont = True


        # ---------------------------------------------Esta funcion hace que el jefe se pueda mover a hacia los lados ----------------------------------------------

        def movd():
            rannnnndom3 = random.randint(1,2)
            global nivel
            self.coords_enemigo = self.canvas.coords(self.enemiga3)
            mx = 1
            my = 1
            rannnndom = random.randint(1, 10)
            # print(rannnndom)
            # print(self.flag_embestida)

            if self.flag_embestida3 == False and nivel == 3:
                if self.disparont == True:
                    self.canvas.after(1000, disparo_ememy3)
                if self.coords_enemigo[0] == 319:
                    self.flag3 = True
                if self.flag3:
                    mx = -1
                if self.coords_enemigo[0] == 49:
                    self.flag3 = False
                if self.sec3 % 6 == 0 and rannnndom % 3 == 0 and self.sec3 > 0:
                    self.flag_embestida3 = True
                    self.disparont = True
                    embestida()
                    if rannnnndom3 == 1:
                        print(rannnnndom3)
                        self.movex = random.randint(49, 319)
                        self.canvas.coords(self.enemiga3, self.movex, 100)

                        embestida()
                        print("ataca otra vez")
                    else:

                        self.canvas. coords(self.enemiga3, 185,100)

                    self.canvas.after(1000, movd)
                    self.disparont = True
                self.canvas.move(self.enemiga3, mx, 0)
                self.canvas.after(10, movd)


        def embestida():
            self.bbox_nave = self.canvas.bbox(self.nave3)
            self.bbox_enemy = self.canvas.bbox((self.enemiga3))
            self.coords_enemigo = self.canvas.coords(self.enemiga3)
            if self.flag_embestida3 == True:
              #  print(self.coords_enemigo)
                if self.coords_enemigo[1] >= 490 and self.estoy_subir == False:
                    # print("Sigo estando harto")
                    self.estoy_subir = True
                    #vida_enemy()
                    self.movey3 = -10
                    self.canvas.move(self.enemiga3, 0, self.movey3)
                    self.canvas.after(10, embestida)
                    if (self.bbox_enemy[2] > self.bbox_nave[0] > self.bbox_enemy[0]) and \
                            (self.bbox_enemy[1] < self.bbox_nave[3] < self.bbox_enemy[3]):
                        vida_player3()
                elif self.coords_enemigo[1] <= 100 and self.estoy_subir == True:
                    self.movey3 = 10
                    self.estoy_subir = False
                    self.flag_embestida3 = False
                    return movd()
                else:
                    self.canvas.move(self.enemiga3, 0, self.movey3)
                    self.canvas.after(10, embestida)

        def disparo_ememy3():
            self.colicion_enemicoords3 = self.canvas.bbox(self.nave3)
            self.colicion_bala_coords3 = self.canvas.bbox(self.bala_enemy3)
            self.coords_enemigo3 = self.canvas.coords(self.nave3)
            self.coords_bala3 = self.canvas.coords(self.bala_enemy3)
            # print(self.coords_bala2)
            m_shot_enemy3 = 10
            if self.coords_bala3[1] >= 580:
                xe3, ye3 = self.canvas.coords(self.enemiga3)

                self.canvas.coords(self.bala_enemy3, xe3, ye3)
                self.flag_enemy_shot3 = False
                return
            if (self.colicion_enemicoords3[2] > self.colicion_bala_coords3[0] > self.colicion_enemicoords3[0]) and (
                    self.colicion_enemicoords3[1] < self.colicion_bala_coords3[3] < self.colicion_enemicoords3[3]):
                self.canvas.move(self.bala_enemy3, -1000000, -10)
                vida_player3()
                self.flag_enemy_shot3 = False
                return

            else:
                if self.coords_bala3[1] >= m_shot_enemy3:
                    self.flag_enemy_shot3 = True

                if self.flag_disparo3:
                    m_shot_enemy3 = 10
                self.canvas.move(self.bala_enemy3, 0, m_shot_enemy3)
                self.canvas.after(1000, disparo_ememy3)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla left, la nave player, se mueva---------------------------------

        def left(event):
            # print(self.coordenadas)
            x, y = self.canvas.coords(self.nave3)  # x and y == coordenadas[0] y [1]
            if event.keysym == "Left" and x >= 36:
                self.canvas.coords(self.nave3, x - 10, y)
                self.coordenadas = self.canvas.coords(self.nave3)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla Right, la nave player, se mueva---------------------------------

        def right(event):
            # print(self.coordenadas)
            x, y = self.canvas.coords(self.nave3)

            if event.keysym == "Right" and x <= 335:
                self.canvas.coords(self.nave3, x + 10, y)
                self.coordenadas = self.canvas.coords(self.nave3)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla Up, la nave player, se mueva---------------------------------
        def up(event):
            # print(self.coordenadas)
            x, y = self.canvas.coords(self.nave3)

            if event.keysym == "Up" and y >= 175:
                self.canvas.coords(self.nave3, x, y - 10)
                self.coordenadas = self.canvas.coords(self.nave3)

# -------------------------------Se realiza la funcion para que cuando se preciona la tecla down, la nave player, se mueva---------------------------------

        def down(event):
            x, y = self.canvas.coords(self.nave3)
            if event.keysym == "Down" and y <= 490:
                self.canvas.coords(self.nave3, x, y + 10)
                self.coordenadas = self.canvas.coords(self.nave3)

        def disparo3():
            global nivel
            if nivel == 3:
                self.colicion_enemicoords = self.canvas.bbox(self.enemiga3)
                self.colicion_bala_coords = self.canvas.bbox(self.Bala3)
                # print(self.colicion_enemicoords)
                self.coords_enemigo = self.canvas.coords(self.enemiga3)
                self.coords_bala = self.canvas.coords(self.Bala3)
                movimiento_de_disparo = 10
                if self.coords_bala[1] <= 0:
                    self.flag_disparo3 = False
                if (self.colicion_enemicoords[2] > self.colicion_bala_coords[0] > self.colicion_enemicoords[0]) and \
                        (self.colicion_enemicoords[1] < self.colicion_bala_coords[3] < self.colicion_enemicoords[3]):
                    self.canvas.move(self.Bala3, -1000000, -10)
                    vida_enemy3()
                    score3()
                    self.flag_disparo3 = False

                else:
                    if self.coords_bala[1] >= movimiento_de_disparo:
                        self.flag_disparo3 = True

                    if self.flag_disparo3:
                        movimiento_de_disparo = -10
                    self.canvas.move(self.Bala3, 0, movimiento_de_disparo)
                    self.canvas.after(10, disparo3)

        def vida_enemy3():
            global Enemigo_live_3
            if Live_level_3 != 0:
                Enemigo_live_3 -= 1
                self.label_liveE3.config(text="Enemy: " + str(Enemigo_live_3))

        def vida_player3():
            global Live_level_3
            if Live_level_3 != 0:
                Live_level_3 -= 3
                self.label_livep3.config(text="live: " + str(Live_level_3))
                if Live_level_3 <= 0:
                    score_guardar3()
                    self.game_over3.config(text="GAME OVER")

        def score3():
            global Score
            if Live_level_3 != 0:
                Score += 3
                self.label_score3.config(text="Score: " + str(Score))
                if Live_level_3 == 50:
                    Score += 10
                    self.label_score3.config(text="Score: " + str(Score))
                    score_guardar3()


        def score_guardar3():
            global M_Scores
            if Live_level_1 or Live_level_2 or Live_level_3 == 0:
                Best_scores = (str(self.textbox_name.get()) + ":" + str(Score) + "\n")
                guardar = open("Scorest.txt", "a")
                guardar.write(Best_scores)
                M_Scores = Best_scores
                guardar.close()

# ------------------------------------------------------Validación para poder disparar---------------------------------------------------------------------

        def accion_disparo(event):
            if event.keysym == 'space':
                x, y = self.canvas.coords(self.nave3)
                self.canvas.coords(self.Bala3, x, y + 25)
                return disparo3()

# ----------------------- Los .bind, sirven para indicar cuando una teca se preciona, ademas de que llama a las funciones de movimeinto--------------------

        self.master.bind("<Left>", left)
        self.master.bind("<Right>", right)
        self.master.bind("<Up>", up)
        self.master.bind("<Down>", down)
        self.master.bind("<space>", accion_disparo)
        movd()
        # embestida()

#-------------------------------------------------------------barra Superior--------------------------------------------------------------------------

        self.b_info = LabelFrame (self.canvas, width= 370, height= 30, highlightthickness=0, bg = "magenta4",relief="raised",borderwidth=2)
        self.b_info.place (x= 0, y= 0)

#-------------------------------------------------------------barra  de información----------------------------------------------------------

        self.b_info = LabelFrame (self.canvas, width= 370, height= 50, highlightthickness=0, bg = "magenta4",relief="raised",borderwidth=6)
        self.b_info.place (x= 0, y= 530)

#-----------------------------------------------------------------Puntaje-----------------------------------------------------------

        self.label_score3 = Label(self.canvas, text="Score: " + str(Score), font=("Vermin Vibes V", 6), bg='magenta4',fg='white')
        self.label_score3.place(x=5, y = 550)

#----------------------------------------------------------Label con la vida del jugador-----------------------------------------

        self.label_livep3 = Label(self.canvas, text="Live: 50", font=("Vermin Vibes V", 6), bg='magenta4',fg='white')
        self.label_livep3.place(x=60, y = 550)

#------------------------------------------------------------------label Vida del enemigo-----------------------------------------

        self.label_liveE3 = Label(self.canvas, text="Enemy: 50" , font=("Vermin Vibes V", 6), bg='magenta4',
                                 fg='white')
        self.label_liveE3.place(x=110, y=550)

#--------------------------------------------------------Label Nombre del jugador--------------------------------------

        self.label_namep3 = Label(self.canvas, text="Player: " + self.textbox_name.get(), font=("Vermin Vibes V", 6),
                                 bg='magenta4',
                                 fg='white')
        self.label_namep3.place(x=175, y=550)



#-------------------------------------------------------Forma del enemigo-----------------------------------------------------
#-----------------------------------------------------------Abrir mi imagen------------------------------------------------

        self.i_enemigo = Image.open("Nave_enemiga.png")

#-----------------------------------------------------cambiar las dimensiones de la imagen----------------------------

        self.redimension = self.i_enemigo.resize((25,25), Image.ANTIALIAS)

        self.new_i_enemigo = ImageTk.PhotoImage(self.redimension)

#-------------------------------------------------------Imagen ya redimencionada-------------------------------------------

        self.i_enemigo= ImageTk.PhotoImage(file= r"C:\Users\User\PycharmProjects\ProyectoTaller_Operation_moon_light\Nave_enemiga.png")
        self.label_i_enemigo = Label(image= self.new_i_enemigo, bg = "magenta4")
        self.label_i_enemigo.place(x=330, y= 540)

#---------------------------------------------------------Boton Menú-----------------------------------------------------------
        self.level_l3 = Label(text="Level 3", font=("Vermin Vibes V", 7), bg="magenta4", fg="black")
        self.level_l3 .place(x=45, y=2.5, width=80, height=25)
        self.game_over3 = Label(text="", font=("Vermin Vibes V", 7), bg="magenta4", fg="black")
        self.game_over3.place(x=270, y=2.5, width=80, height=25)
        self.bo_menu = Button(self.canvas, text="Menu", font=("Vermin Vibes V", 7), bg="magenta4", fg="black",
                                  relief="raised", borderwidth=5,
                                  command=self.volver)
        self.bo_menu.place(x=152.5, y=2.5, width=65, height=25)



#-------------------------------------------------------------Timepo transcurrido-------------------------------------------

#-------------------------------------------------------label time--------------------------------------

        self.label_time= Label(self.canvas, text= "Time",font=("Vermin Vibes V", 6),
                                 bg='magenta4',
                                 fg='white')
        self.label_time.place(x=260, y=550)

#---------------------------------------------------------label minutos-----------------------------------------

        self.minutos3 = Label(self.canvas, text= int("0"), font=("Vermin Vibes V", 6),
                              bg='magenta4',
                              fg='white')
        self.minutos3.place(x=290, y=550)

#------------------------------------------------------label ":"----------------------------------------

        self.label_divi = Label(self.canvas, text= ":",font=("Vermin Vibes V", 6),
                                 bg='magenta4',
                                 fg='white')
        self.label_divi.place(x=300, y=550)

 #----------------------------------------segundos------------------------------------------------------

        self.segundos3 = Label(self.canvas, text="", font=("Vermin Vibes V", 6),
                                 bg='magenta4',
                                 fg='white')
        self.segundos3.place(x=305, y=550)

        self.contar_segundos3()
#---------------------------------------------Funcion para contar los segundos------------------------------

    def contar_segundos3(self):
            if self.sec3 != 60:
                self.sec3 += 1
                self.zero3 = ""
                if 0 <= self.sec3 < 10:
                    self.zero3 = "0" + str(self.sec3)
                else:
                    self.zero3 = str(self.sec3)
                self.segundos3.configure(text=self.zero3)
                self.canvas.after(1000, self.contar_segundos3)
            if self.sec3 == 60:
                self.sec3 = 0
                self.min3 += 1
                self.minutos3.configure(text=self.min3)
window = Tk()
var= IntVar()
window.iconbitmap("iluna.ico")
bg = PhotoImage(file= r"C:\Users\User\PycharmProjects\ProyectoTaller_Operation_moon_light\Fondo.png")
window.title("Operation moon light")
ventana_principal = pantalla_principal(window)
window.minsize(370,580)

window.mainloop()