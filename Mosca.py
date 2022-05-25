import math
from Modelo import *
import glm

class Mosca(Modelo):
    angulo = 0
    fase= 90
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.vertices = np.array([],dtype="float32")
        self.vertices = np.append(self.vertices, np.array(
            [

            ], dtype="float32"
        ))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) 
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) -0.08

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 31/255, 31/255, 31/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) +0.03
            componente_y = 0.010 * math.sin(angulo * math.pi / 180) -.08

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 147/255, 234/255, 249/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) -0.03
            componente_y = 0.010 * math.sin(angulo * math.pi / 180) -.08

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 147/255, 234/255, 249/255, 1.0 ], dtype="float32"))

        #crear una matriz identidad
        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def actualizar(self, tiempo_delta):
        cantidad_movimiento = 0.6 * tiempo_delta
        self.posicion.x = self.posicion.x + (math.cos((self.angulo + self.fase) * math.pi/ 180)  * cantidad_movimiento )
        self.posicion.y = self.posicion.y + (math.sin((self.angulo + self.fase) * math.pi/ 180)  * cantidad_movimiento )

        self.angulo = self.angulo + 0.2

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones, self.posicion)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 0, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 72, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 144, 72)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

