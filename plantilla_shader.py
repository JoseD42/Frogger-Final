import OpenGL.GL as gl
import glfw
import numpy as np
from Fondo import *
from Shader import *
from Modelo import *
from Carros import *
from Carros2 import *
from Rana import *
from Mosca import *
tiempo_anterior = 0.0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

modelo = None
fondo = None
rana = None
carros = None
carros2 = None
window = None
mosca = None

carros = []
carros2 = []

posiciones_carros = [
     [0.8, -0.75, 0.0, 0.6, 3],
     [0.2, -0.55, 0.0, 0.5, 3],
     [-0.1, -0.55, 0.0, 0.9, 3],
     [-0.6, -0.15, 0.0, 0.6, 3],
     [0.5, 0.05, 0.0, 0.8, 3],
     [0.7, 0.25, 0.0, 0.5, 3],
     [-0.4, 0.55, 0.0, 0.9, 3],
     [0.5, 0.75, 0.0, 0.5, 3],
     [0.2, 0.85, 0.0, 0.7, 3],
     [0.5,-0.85, 0.0, 0.6, 3],
     [0.5, -0.75, 0.0, 0.9, 3],
     [-0.9, -0.65, 0.0, 0.8, 3],
     [0.8, -0.55, 0.0, 0.7, 3],
     [0.9, -0.45, 0.0, 0.8, 3],
     [-0.8, -0.85, 0.0, 0.9, 3],
     [-0.7, -0.25, 0.0, 0.8, 3],
     [-0.2, -0.15, 0.0, 0.8, 3],
     [-0.5, -0.05, 0.0, 0.9, 3],
     [0.9, 0.05, 0.0, 0.5, 3],
     [0.7, 0.15, 0.0, 0.6, 3],
     [0.2, 0.25, 0.0, 0.5, 3],
     [0.7, 0.65, 0.0, 0.7, 3],
     [0.5, 0.45, 0.0, 0.8, 3]
 ]

posiciones_carros2 = [
     [0.3,-0.85, 0.0, 0.5, 2],
     [-0.4, -0.65, 0.0, 0.7,2],
     [0.7, -0.45, 0.0, 0.8, 2],
     [-0.3, -0.25, 0.0, 0.5, 2],
     [-0.2, -0.05, 0.0, 0.5, 2],
     [0.3, 0.15, 0.0, 0.5, 2],
     [0.9, 0.75, 0.0, 0.6, 2],
     [0.2, 0.45, 0.0, 0.8, 2],
     [-0.2, 0.65, 0.0, 0.5, 2]
 ]
vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def inicializar_carros(shader,
            posicion_id, color_id, transformaciones_id):
    for i in range(23):
        posicion_x=posiciones_carros[i][0]
        posicion_y=posiciones_carros[i][1]
        posicion_z=posiciones_carros[i][2]
        velocidad=posiciones_carros[i][3]
        direccion=posiciones_carros[i][4]
        carros.append(Carros(shader,
            posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion))

def inicializar_carros2(shader,
            posicion_id, color_id, transformaciones_id):
    for i in range(9):
        posicion_x=posiciones_carros2[i][0]
        posicion_y=posiciones_carros2[i][1]
        posicion_z=posiciones_carros2[i][2]
        velocidad=posiciones_carros2[i][3]
        direccion=posiciones_carros2[i][4]
        carros2.append(Carros2(shader,
            posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion))

def actualizar():
    global window
    global mosca
    global tiempo_anterior
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    for carro in carros:
        carro.actualizar (tiempo_delta)
    for carro2 in carros2:
        carro2.actualizar (tiempo_delta)
    for carro in carros:
        if carro.colisionando(rana):
            glfw.set_window_should_close(window, 1)
    for carro2 in carros2:
        if carro2.colisionando(rana):
            glfw.set_window_should_close(window, 1)
    tiempo_anterior = tiempo_actual
    mosca.actualizar(tiempo_delta)

def dibujar():
    global modelo
    global fondo
    global rana
    global carros
    global mosca
    global carros2
    fondo.dibujar()
    for carro in carros:
        carro.dibujar()
    for carro2 in carros2:
        carro2.dibujar()
    rana.dibujar()
    mosca.dibujar()
    #modelo.dibujar()

def main():
    global modelo
    global fondo
    global rana
    global mosca
    global carros
    global carros2
    global window
    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")

    fondo = Fondo(shader, 
            posicion_id, color_id, transformaciones_id)

    rana = Rana(shader,
            posicion_id, color_id, transformaciones_id)

    mosca = Mosca(shader,
            posicion_id, color_id, transformaciones_id)

    #carros = Carros(shader,
            #posicion_id, color_id, transformaciones_id)

    inicializar_carros(shader,
            posicion_id, color_id, transformaciones_id)

    inicializar_carros2(shader,
            posicion_id, color_id, transformaciones_id)
    glfw.set_key_callback(window, rana.actualizar)

    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.3,0.3,0.3,1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    modelo.borrar()
    fondo.borrar()
    rana.borrar()
    carros.borrar()
    carros2.borrar()
    shader.borrar()
    mosca.borrar()
    

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()

