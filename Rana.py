import math
import glfw
from Modelo import *
import glm

class Rana(Modelo):
    x = 0.0
    y = -0.95
    z = 0.0
    velocidad = 0.1
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.extremo_izquierdo = 0.05* 0.5
        self.extremo_derecho = 0.05* 0.5
        self.extremo_inferior = 0.04* 0.5
        self.extremo_superior =0.04* 0.5
        
        self.vertices = np.array(
            [
                (-0.80 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.80 * 0.5) + 0.4, (-0.11 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.76 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.76 * 0.5) + 0.4, (-0.11 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo

                (-0.82 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.82 * 0.5) + 0.4, (-0.25 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.74 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.74 * 0.5) + 0.4, (-0.25 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo

                (-0.84 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.84 * 0.5) + 0.4, (-0.18 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.72 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.72 * 0.5) + 0.4, (-0.18 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo

                (-0.84 * 0.5) + 0.4, (-0.25 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.84 * 0.5) + 0.4, (-0.22 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.72 * 0.5) + 0.4, (-0.25 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.72 * 0.5) + 0.4, (-0.22 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo
                
                (-0.74 * 0.5) + 0.4, (-0.22 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.74 * 0.5) + 0.4, (-0.27 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.72 * 0.5) + 0.4, (-0.22 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.72 * 0.5) + 0.4, (-0.27 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo

                (-0.84 * 0.5) + 0.4, (-0.22 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.84 * 0.5) + 0.4, (-0.27 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.82 * 0.5) + 0.4, (-0.22 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.82 * 0.5) + 0.4, (-0.27 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo

                (-0.84 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.84 * 0.5) + 0.4, (-0.13 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.82 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.82 * 0.5) + 0.4, (-0.13 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo

                (-0.74 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,  98/255,198/255,0/255,1.0,  #izquierda arriba
                (-0.74 * 0.5) + 0.4, (-0.13 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0,  #izquierda abajo
                (-0.72 * 0.5) + 0.4, (-0.15 * 0.5) + 0.1, 0.0,1.0,     98/255,198/255,0/255,1.0, #derecha arriba
                (-0.72 * 0.5) + 0.4, (-0.13 * 0.5) + 0.1, 0.0,1.0,    98/255,198/255,0/255,1.0, # derecha abajo

                
            ], dtype="float32"

        )


        #crear una matriz identidad
        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id, self.x, self.y, self.z, self.velocidad, 0.0)
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones, self.posicion)

    def actualizar(self,window, key, scancode, action, mods):

        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window,1)

        #Mover la rana
        #Izquierda
        if key == glfw.KEY_LEFT and (action == glfw.PRESS):
            self.mover(self.IZQUIERDA)
        #Derecha
        if key == glfw.KEY_RIGHT and (action == glfw.PRESS):
            self.mover(self.DERECHA)
        #Arriba
        if key == glfw.KEY_UP and (action == glfw.PRESS):
            self.mover(self.ARRIBA)
        #Abajo
        if key == glfw.KEY_DOWN and (action == glfw.PRESS):
            self.mover(self.ABAJO)

    def mover(self, direccion):
        cantidad_movimiento = glm.vec3(0,0,0)
        if direccion == self.ARRIBA:
            self.posicion.y =  self.posicion.y + self.velocidad
        elif direccion == self.ABAJO:
            self.posicion.y =  self.posicion.y - self.velocidad
        elif direccion == self.DERECHA:
            self.posicion.x =  self.posicion.x + self.velocidad
        elif direccion == self.IZQUIERDA:
            self.posicion.x =  self.posicion.x - self.velocidad

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

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

