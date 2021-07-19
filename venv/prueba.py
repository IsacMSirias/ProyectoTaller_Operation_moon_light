from tkinter import*


class pantalla:
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width=370, height=580, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        x = 20
        y = 20
        self.circulo = self.canvas.create_oval(x,y,1,1, fill = "red" )



window = Tk()
ventana = pantalla(window)
window.minsize(370,580)
window.mainloop()


def vida_enemy2():
    global Enemigo_live_2
    if Live_level_2 != 0:
        Enemigo_live_2 -= 2
        self.label_liveE2.config(text="Enemy: " + str(Enemigo_live_2))
    if Live_level_2 == 0:
        self.game_over.config(text="GAME OVER")


def vida_player2():
    global Live_level_2
    if Live_level_2 != 0:
        Live_level_2 -= 5
        self.label_liveE2.config(text="live: " + str(Live_level_2))


def score2():
    global Score
    if Live_level_1 and Live_level_2 != 0:
        Score += 3
        self.label_score2.config(text="Score: " + str(Score))


def siguiente_nivel3():
    if Enemigo_live_2 == 0:
        self.pantalla_nivel3()





        ############################


        def movd3():
            self.coords_enemigo = self.canvas.coords(
                self.enemiga3)  # Coordenadas del enemigo, estas sirven para poder saber en donde limitar el mov
            mx = 1  # el numero positivo es para que vaya hacia la derecha.
            my = 1
            rannnndom = random.randint(1, 10)
            # print(rannnndom)
            # print(self.flag_embestida)
            if self.flag_embestida3 == False:
                if self.coords_enemigo[0] == 319:
                    self.flag3 = True  # el flag cambia a ser verdadero
                if self.flag3:  # ¿y que significa que sea verdadero?
                    mx = -1  # Que su valor va a cambiar de un numero positivo, a un numero negativo para que pueda ir hacia la izquierda
                if self.coords_enemigo[0] == 49:
                    self.flag3 = False
                if self.sec1 % 2 == 0 and rannnndom % 3 == 1:
                    self.flag_embestida3 = True
                    embestida3()
                    self.canvas.after(10, movd3)

                else:
                    # print("si me ejecuté")

                    self.canvas.move(self.enemiga3, mx,
                                     0)  # "move" permita que se mueva la imagen enemiga con el movimiento del eje x
                    self.canvas.after(10, movd3)  # La funcion se ejecuta cada milisegundo

        def embestida3():
            self.bbox_nave = self.canvas.bbox(self.nave3)
            self.bbox_enemy = self.canvas.bbox((self.enemiga3))
            self.coords_enemigo = self.canvas.coords(self.enemiga3)
            if self.coords_enemigo[1] >= 490 and self.estoy_harto3 == False:
                # print("Sigo estando harto")
                self.estoy_harto3 = True

                self.movey3 = -10
                self.canvas.move(self.enemiga3, 0, self.movey3)
                self.canvas.after(10, embestida3)
                if (self.bbox_enemy[2] > self.bbox_nave[0] > self.bbox_enemy[0]) and \
                        (self.bbox_enemy[1] < self.bbox_nave[3] < self.bbox_enemy[
                            3]):  # Colision entre la nave enemiga y la nave del jugador
                    print("hello world")
            elif self.coords_enemigo[1] <= 100 and self.estoy_harto3 == True:
                self.movey3 = 10
                self.estoy_harto3 = False
                self.flag_embestida3 = False
                return movd3()
            else:
                self.canvas.move(self.enemiga3, 0, self.movey3)
                self.canvas.after(10, embestida3)




     self.flag_embestida = True

        def movd2 ():
            self.coords_enemigo = self.canvas.coords(self.enemiga2)
            mx2 = 1
            #print(self.sec1)
            if self.coords_enemigo[0] == 319:
                self.flag2 = True
            if self.flag2:
                mx2 = -1
            if self.coords_enemigo[0] == 49:
                self.flag2 = False
            if self.sec1 % 2 == 0 and self.sec1 > 0:

                self.coords_enemigo[0] = random.randint(49,319)
            self.canvas.move(self.enemiga2, mx2, 0)
            self.canvas.after(10, movd2)


def movd3():
    global nivel
    if nivel == 3:

        self.coords_enemigo = self.canvas.coords(self.enemiga3)
        mx3 = -1
        if self.coords_enemigo[0] == 49:
            self.flag3 = True
        if self.flag3:
            mx3 = 1
        if self.coords_enemigo[0] == 319:
            self.flag3 = False
        self.canvas.move(self.enemiga3, mx3, 0)
        self.canvas.after(10, movd3)





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






