import math
from Modelo import *
import glm

class Carros2(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0,0.0,0.0)
        self.posicion.x = posicion_x
        self.posicion.y = posicion_y
        self.posicion.z = posicion_z
        self.velocidad = velocidad
        self.direcion = direccion
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior =0.05
        self.vertices = np.array([],dtype="float32")
        self.vertices = np.append(self.vertices, np.array(
            [
                #Carro rojo
                #Chasis
                #Cola
                0.1,0.04,0.0,1.0,  198/255,27/255,0/255,1.0,  #izquierda arriba # 
                0.1,-0.04,0.0,1.0, 198/255,27/255,0/255,1.0,  #izquierda abajo #
                0.08,0.04,0.0,1.0,  198/255,27/255,0/255,1.0, #derecha arriba #
                0.08,-0.04,0.0,1.0, 198/255,27/255,0/255,1.0, # derecha abajo #
                
                #Despues cola
                0.06,0.01,0.0,1.0,  198/255,27/255,0/255,1.0,  #izquierda arriba # 
                0.06,-0.01,0.0,1.0, 198/255,27/255,0/255,1.0,  #izquierda abajo #
                0.08,0.01,0.0,1.0,  198/255,27/255,0/255,1.0, #derecha arriba #
                0.08,-0.01,0.0,1.0, 198/255,27/255,0/255,1.0, # derecha abajo #

                #cuadrado grande
                0,0.03,0.0,1.0,  198/255,27/255,0/255,1.0,  #izquierda arriba #
                0,-0.03,0.0,1.0, 198/255,27/255,0/255,1.0,  #izquierda abajo #
                0.06,0.03,0.0,1.0,  198/255,27/255,0/255,1.0, #derecha arriba #
                0.06,-0.03,0.0,1.0, 198/255,27/255,0/255,1.0, # derecha abajo #

                #Despues cuadrado
                -0.015,0.015,0.0,1.0,  198/255,27/255,0/255,1.0,  #izquierda arriba #
                -0.015,-0.015,0.0,1.0, 198/255,27/255,0/255,1.0,  #izquierda abajo #
                0,0.015,0.0,1.0,  198/255,27/255,0/255,1.0, #derecha arriba #
                0,-0.015,0.0,1.0, 198/255,27/255,0/255,1.0, # derecha abajo #

                #tubo enmedio
                -0.05,0.01,0.0,1.0,  198/255,27/255,0/255,1.0,  #izquierda arriba #
                -0.05,-0.01,0.0,1.0, 198/255,27/255,0/255,1.0,  #izquierda abajo #
                0,0.01,0.0,1.0,  198/255,27/255,0/255,1.0, #derecha arriba #
                0,-0.01,0.0,1.0, 198/255,27/255,0/255,1.0, # derecha abajo #

                #vidrio
                0.02,0.01,0.0,1.0,  99/255,156/255,247/255,1.0,  #izquierda arriba #
                0.02,-0.01,0.0,1.0, 99/255,156/255,247/255,1.0,  #izquierda abajo #
                0.055,0.01,0.0,1.0,  99/255,156/255,247/255,1.0, #derecha arriba #
                0.055,-0.01,0.0,1.0, 99/255,156/255,247/255,1.0, # derecha abajo #

                #Llanta arriba trasera
                0.035,0.04,0.0,1.0,  0,0,0,1.0,  #izquierda arriba #
                0.035,0.03,0.0,1.0, 0,0,0,1.0,  #izquierda abajo #
                0.06,0.04,0.0,1.0,  0,0,0,1.0, #derecha arriba #
                0.06,0.03,0.0,1.0, 0,0,0,1.0, # derecha abajo #

                #Llanta abajo trasera
                0.035,-0.041,0.0,1.0,  0,0,0,1.0,  #izquierda arriba #
                0.035,-0.03,0.0,1.0,   0,0,0,1.0,  #izquierda abajo #
                0.06,-0.041,0.0,1.0,  0,0,0,1.0, #derecha arriba #
                0.06,-0.03,0.0,1.0,   0,0,0,1.0, # derecha abajo #

                #tubo llanta superior
                -0.04,0.03,0.0,1.0,  207/255,209/255,212/255,1.0,  #izquierda arriba
                -0.04,0.01,0.0,1.0,   207/255,209/255,212/255,1.0,  #izquierda abajo
                -0.03,0.03,0.0,1.0,  207/255,209/255,212/255,1.0, #derecha arriba
                -0.03,0.01,0.0,1.0,   207/255,209/255,212/255,1.0, # derecha abajo

                #tubo llanta inferior
                -0.04,-0.01,0.0,1.0,  207/255,209/255,212/255,1.0,  #izquierda arriba
                -0.04,-0.03,0.0,1.0,   207/255,209/255,212/255,1.0,  #izquierda abajo
                -0.03,-0.01,0.0,1.0,  207/255,209/255,212/255,1.0, #derecha arriba
                -0.03,-0.03,0.0,1.0,   207/255,209/255,212/255,1.0, # derecha abajo

                #Llanta abajo frontal
                -0.05,-0.041,0.0,1.0,  0,0,0,1.0,  #izquierda arriba #
                -0.05,-0.03,0.0,1.0,   0,0,0,1.0,  #izquierda abajo #
                -0.02,-0.041,0.0,1.0,  0,0,0,1.0, #derecha arriba #
                -0.02,-0.03,0.0,1.0,   0,0,0,1.0, # derecha abajo #

                #Llanta arriba frontal
                -0.05,0.04,0.0,1.0,  0,0,0,1.0,  #izquierda arriba #
                -0.05,0.03,0.0,1.0,   0,0,0,1.0,  #izquierda abajo #
                -0.02,0.04,0.0,1.0,  0,0,0,1.0, #derecha arriba #
                -0.02,0.03,0.0,1.0,   0,0,0,1.0, # derecha abajo #

            ], dtype="float32"
        ))


        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion)

    def actualizar(self, tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        if self.direccion == 2:
            self.posicion.x = self.posicion.x - cantidad_movimiento
            if self.posicion.x <= -1:
                self.posicion.x = 1
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


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

