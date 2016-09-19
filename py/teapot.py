# -*- coding:utf-8 -*-
# 2016/09/19
# pip install PyOpenGL PyOpenGL_accelerate
# python 2.7

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.5)
    glFlush()
def do_main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Teapot")
    glutDisplayFunc(draw_func)
    #glutIdleFunc(draw_func)
    glutMainLoop()
if __name__ == "__main__":
    do_main()