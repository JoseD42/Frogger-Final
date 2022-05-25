import math
from Modelo import *
import glm

class Fondo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0,0.0,0.0)
        self.vertices = np.array(
            [
                #Fondo
                -1.0,2.0,0.0,1.0,    30/255, 69/255, 34/255,1.0,  #izquierda arriba
                -1.0,-2.0,0.0,1.0,   30/255, 69/255, 34/255,1.0,  #izquierda abajo
                1.0,2.0,0.0,1.0,     30/255, 69/255, 34/255,1.0, #derecha arriba
                1.0,-2.0,0.0,1.0,    30/255, 69/255, 34/255,1.0, # derecha abajo

                #Calle
                -1.0,0.9,0.0,1.0,    92/255,92/255,92/255,1.0,  #izquierda arriba
                -1.0,-0.9,0.0,1.0,   92/255,92/255,92/255,1.0,  #izquierda abajo
                1.0,0.9,0.0,1.0,     92/255,92/255,92/255,1.0, #derecha arriba
                1.0,-0.9,0.0,1.0,    92/255,92/255,92/255,1.0, # derecha abajo

                #Banqueta
                -1.0,-0.30,0.0,1.0,   184/255, 186/255, 186/255,1.0,  #izquierda arriba
                -1.0,-0.40,0.0,1.0,   184/255, 186/255, 186/255,1.0,  #izquierda abajo
                1.0,-0.30,0.0,1.0,    184/255, 186/255, 186/255,1.0, #derecha arriba
                1.0,-0.40,0.0,1.0,    184/255, 186/255, 186/255,1.0, # derecha abajo

                -1.0,0.30,0.0,1.0,    184/255, 186/255, 186/255,1.0,  #izquierda arriba
                -1.0,0.40,0.0,1.0,    184/255, 186/255, 186/255,1.0,  #izquierda abajo
                1.0,0.30,0.0,1.0,     184/255, 186/255, 186/255,1.0, #derecha arriba
                1.0,0.40,0.0,1.0,     184/255, 186/255, 186/255,1.0, # derecha abajo

                #Lineas calle
                -1.0,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                -1.0,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                -0.8,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                -0.8,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                -0.5,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                -0.5,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                -0.3,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                -0.3,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                0.0,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                0.0,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                0.2,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                0.2,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                0.5,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                0.5,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                0.7,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                0.7,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                0.5,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                0.5,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                0.7,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                0.7,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                #Lineas calle abajo
                -1.0 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -0.5 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -0.5 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.3 +.1, 0.025 -.67 ,0.0,1.0,  255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.3 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.0 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.0 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.2 +.1, 0.025 -.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.2 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.5 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.5 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.7 +.1, 0.025 -.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.7 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                #Lineas calle arriba
                -1.0 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8 +.1, 0.025 +.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -0.5 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -0.5 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.3 +.1, 0.025 +.67 ,0.0,1.0,  255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.3 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.0 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.0 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.2 +.1, 0.025 +.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.2 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.5 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.5 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.7 +.1, 0.025 +.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.7 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                #Lineas peatonales arriba
                -1.0, 0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, 0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, 0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, 0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                #Lineas peatonales abajo
                -1.0, -0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, -0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, -0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, -0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                #Buzón azul
                0.65,-0.37,0.0, 1.0,   61/255, 0/255, 198/255,1.0,  #izquierda arriba
                0.65,-0.31,0.0, 1.0,   61/255, 0/255, 198/255,1.0,  #izquierda abajo
                0.75,-0.37,0.0, 1.0,   61/255, 0/255, 198/255,1.0, #derecha arriba
                0.75,-0.31,0.0, 1.0,  61/255, 0/255, 198/255,1.0, # derecha abajo
               
                #semaforo amarillo
                -0.83,0.37,0.0, 1.0,   236/255, 240/255, 12/255,1.0,  #izquierda arriba
                -0.83,0.31,0.0, 1.0,   236/255, 240/255, 12/255,1.0,  #izquierda abajo
                -0.79,0.37,0.0, 1.0,   236/255, 240/255, 12/255,1.0, #derecha arriba
                -0.79,0.31,0.0, 1.0,  236/255, 240/255, 12/255,1.0, # derecha abajo

                #Focos banqueta arriba:
                #Izquierdo
                #base
                -0.9,0.37,0.0, 1.0,   84/255, 88/255, 89/255,1.0,  #izquierda arriba
                -0.9,0.31,0.0, 1.0,   84/255, 88/255, 89/255,1.0,  #izquierda abajo
                -0.85,0.37,0.0, 1.0,  84/255, 88/255, 89/255,1.0, #derecha arriba
                -0.85,0.31,0.0, 1.0,  84/255, 88/255, 89/255,1.0, # derecha abajo

                #foco
                -0.895,0.30,0.0, 1.0,   240/255, 242/255, 131/255,1.0,  #izquierda arriba
                -0.895,0.265,0.0, 1.0,  240/255, 242/255, 131/255,1.0,  #izquierda abajo
                -0.853,0.30,0.0, 1.0,  240/255, 242/255, 131/255,1.0, #derecha arriba
                -0.853,0.265,0.0, 1.0,  240/255, 242/255, 131/255,1.0, # derecha abajo

                #tubo
                -0.89,0.39,0.0, 1.0,  43/255, 45/255, 46/255,1.0,  #izquierda arriba
                -0.89,0.27,0.0, 1.0,  43/255, 45/255, 46/255,1.0,  #izquierda abajo
                -0.86,0.39,0.0, 1.0,  43/255, 45/255, 46/255,1.0, #derecha arriba
                -0.86,0.27,0.0, 1.0,  43/255, 45/255, 46/255,1.0, # derecha abajo

                #Derecho
                #base
                0.9,0.37,0.0, 1.0,  236/255, 240/255, 12/255,1.0,  #izquierda arriba
                0.9,0.31,0.0, 1.0,  236/255, 240/255, 12/255,1.0,  #izquierda abajo
                0.85,0.37,0.0, 1.0,  236/255, 240/255, 12/255,1.0, #derecha arriba
                0.85,0.31,0.0, 1.0,  236/255, 240/255, 12/255,1.0, # derecha abajo

                #foco
                0.895,0.30,0.0, 1.0,   237/255, 237/255, 237/255,1.0,  #izquierda arriba
                0.895,0.265,0.0, 1.0,  237/255, 237/255, 237/255,1.0,  #izquierda abajo
                0.853,0.30,0.0, 1.0,  237/255, 237/255, 237/255,1.0, #derecha arriba
                0.853,0.265,0.0, 1.0,  237/255, 237/255, 237/255,1.0, # derecha abajo

                #tubo
                0.89,0.39,0.0, 1.0,  211/255, 214/255, 26/255,1.0,  #izquierda arriba
                0.89,0.27,0.0, 1.0,  211/255, 214/255, 26/255,1.0,  #izquierda abajo
                0.86,0.39,0.0, 1.0,  211/255, 214/255, 26/255,1.0, #derecha arriba
                0.86,0.27,0.0, 1.0,  211/255, 214/255, 26/255,1.0, # derecha abajo

                #Focos banqueta abajo:
                #Izquierdo
                #base
                -0.9,-0.39,0.0, 1.0,   236/255, 240/255, 12/255,1.0,  #izquierda arriba
                -0.9,-0.33,0.0, 1.0,   236/255, 240/255, 12/255,1.0,  #izquierda abajo
                -0.85,-0.39,0.0, 1.0,  236/255, 240/255, 12/255,1.0, #derecha arriba
                -0.85,-0.33,0.0, 1.0,  236/255, 240/255, 12/255,1.0, # derecha abajo

                #foco
                -0.895,-0.40,0.0, 1.0,   237/255, 237/255, 237/255,1.0,  #izquierda arriba
                -0.895,-0.445,0.0, 1.0,  237/255, 237/255, 237/255,1.0,  #izquierda abajo
                -0.853,-0.40,0.0, 1.0,  237/255, 237/255, 237/255,1.0, #derecha arriba
                -0.853,-0.445,0.0, 1.0,  237/255, 237/255, 237/255,1.0, # derecha abajo

                #tubo
                -0.89,-0.44,0.0, 1.0,  211/255, 214/255, 26/255,1.0,  #izquierda arriba
                -0.89,-0.31,0.0, 1.0,  211/255, 214/255, 26/255,1.0,  #izquierda abajo
                -0.86,-0.44,0.0, 1.0,  211/255, 214/255, 26/255,1.0, #derecha arriba
                -0.86,-0.31,0.0, 1.0,  211/255, 214/255, 26/255,1.0, # derecha abajo

                #Derecho
                #base
                0.9,-0.39,0.0, 1.0,  84/255, 88/255, 89/255,1.0,  #izquierda arriba
                0.9,-0.33,0.0, 1.0,  84/255, 88/255, 89/255,1.0,  #izquierda abajo
                0.85,-0.39,0.0, 1.0,  84/255, 88/255, 89/255,1.0, #derecha arriba
                0.85,-0.33,0.0, 1.0,  84/255, 88/255, 89/255,1.0, # derecha abajo

                #foco
                0.895,-0.40,0.0, 1.0,   240/255, 242/255, 131/255,1.0,  #izquierda arriba
                0.895,-0.445,0.0, 1.0,  240/255, 242/255, 131/255,1.0,  #izquierda abajo
                0.853,-0.40,0.0, 1.0,  240/255, 242/255, 131/255,1.0, #derecha arriba
                0.853,-0.445,0.0, 1.0,  240/255, 242/255, 131/255,1.0, # derecha abajo

                #tubo
                0.89,-0.44,0.0, 1.0,  43/255, 45/255, 46/255,1.0,  #izquierda arriba
                0.89,-0.31,0.0, 1.0,  43/255, 45/255, 46/255,1.0,  #izquierda abajo
                0.86,-0.44,0.0, 1.0,  43/255, 45/255, 46/255,1.0, #derecha arriba
                0.86,-0.31,0.0, 1.0,  43/255, 45/255, 46/255,1.0, # derecha abajo

                #buzón rojo
                -0.75,0.37,0.0, 1.0,  235/255, 64/255, 52/255,1.0,  #izquierda arriba
                -0.75,0.31,0.0, 1.0,  235/255, 64/255, 52/255,1.0,  #izquierda abajo
                -0.65,0.37,0.0, 1.0,  235/255, 64/255, 52/255,1.0, #derecha arriba
                -0.65,0.31,0.0, 1.0,  235/255, 64/255, 52/255,1.0, # derecha abajo

                
            ], dtype="float32"

        )
        #Arbol arriba:
        for angulo in range(0, 359, 5):
            componente_x = 0.1 * math.cos(angulo * math.pi / 180) +.3
            componente_y = 0.065 * math.sin(angulo * math.pi / 180) -.08 +.42 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            66/255, 193/255, 42/255, 1.0 ], dtype="float32"))   

        for angulo in range(0, 359, 5):
            componente_x = 0.065 * math.cos(angulo * math.pi / 180)  +.3
            componente_y = 0.09 * math.sin(angulo * math.pi / 180) -.08 +.42 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            66/255, 193/255, 42/255, 1.0 ], dtype="float32"))  

        #Arbol abajo
        for angulo in range(0, 359, 5):
            componente_x = 0.1 * math.cos(angulo * math.pi / 180)  -.29
            componente_y = 0.065 * math.sin(angulo * math.pi / 180) -.08 -.29 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            182/255, 204/255, 4/255, 1.0 ], dtype="float32")) 

        for angulo in range(0, 359, 5):
            componente_x = 0.065 * math.cos(angulo * math.pi / 180)  -.29
            componente_y = 0.09 * math.sin(angulo * math.pi / 180) -.08 -.29 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            182/255, 204/255, 4/255, 1.0 ], dtype="float32")) 

        #Alcantarillas
        for angulo in range(0, 359, 5):
            componente_x = 0.06 * math.cos(angulo * math.pi / 180)  - 0.3
            componente_y = 0.06 * math.sin(angulo * math.pi / 180) + 0.58 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            143/255, 145/255, 148/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.05 * math.cos(angulo * math.pi / 180)  - 0.3
            componente_y = 0.05 * math.sin(angulo * math.pi / 180) + 0.58 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            175/255, 176/255, 179/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.06 * math.cos(angulo * math.pi / 180)  + 0.3
            componente_y = 0.06 * math.sin(angulo * math.pi / 180) - 0.58 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            143/255, 145/255, 148/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.05 * math.cos(angulo * math.pi / 180)  + 0.3
            componente_y = 0.05 * math.sin(angulo * math.pi / 180) - 0.58 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            0/255, 0/255, 0/255, 1.0 ], dtype="float32"))

        #Buzon azul
        for angulo in range(0, 182, 5):
            componente_x = -0.045 * math.cos(angulo * math.pi / 180)  + 0.70
            componente_y = -0.045 * math.sin(angulo * math.pi / 180) - 0.31 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            138/255, 152/255, 161/255, 1.0 ], dtype="float32"))

        #Semaforo
        for angulo in range(0, 182, 5):
            componente_x = -0.021 * math.cos(angulo * math.pi / 180)  - 0.810
            componente_y = -0.021 * math.sin(angulo * math.pi / 180) + 0.31 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            38/255, 38/255, 36/255, 1.0 ], dtype="float32"))

        #pétalos
        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180)  + 0.15
            componente_y = 0.012 * math.sin(angulo * math.pi / 180) -0.95 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            214/255, 214/255, 214/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.012 * math.cos(angulo * math.pi / 180)  + 0.15
            componente_y = 0.04 * math.sin(angulo * math.pi / 180) -0.95 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            214/255, 214/255, 214/255, 1.0 ], dtype="float32"))

        #centro
        for angulo in range(0, 359, 5):
            componente_x = 0.012 * math.cos(angulo * math.pi / 180)  + 0.15
            componente_y = 0.012 * math.sin(angulo * math.pi / 180) -0.95 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            128/255, 112/255, 62/255, 1.0 ], dtype="float32"))

        #pétalos arriba
        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180)  - 0.3
            componente_y = 0.012 * math.sin(angulo * math.pi / 180) +0.95 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            214/255, 214/255, 214/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.012 * math.cos(angulo * math.pi / 180)  - 0.3
            componente_y = 0.04 * math.sin(angulo * math.pi / 180) +0.95 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            214/255, 214/255, 214/255, 1.0 ], dtype="float32"))

        #centro
        for angulo in range(0, 359, 5):
            componente_x = 0.012 * math.cos(angulo * math.pi / 180)  -0.3
            componente_y = 0.012 * math.sin(angulo * math.pi / 180) +0.95 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            128/255, 112/255, 62/255, 1.0 ], dtype="float32"))

        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, direccion):
        
        if direccion == self.ARRIBA:
           self.posicion.y  = self.posicion.y + 0.001
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - 0.001

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 60, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 64, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 68, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 72, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 76, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 80, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 84, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 88, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 92, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 96, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 100, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 104, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 108, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 112, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 116, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 120, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 124, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 128, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 132, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 136, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 140, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 144, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 148, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 152, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 156, 4)

        #Circulos:
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 160, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 232, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 304, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 376, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 448, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 520, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 592, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 664, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 736, 37)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 773, 37)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 810, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 882, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 954, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1026, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1098, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1170, 72)


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()