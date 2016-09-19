# -*- coding:utf-8 -*-
# 2016/09/19
# pip install PyOpenGL PyOpenGL_accelerate
# python 2.7

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
def draw_func():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glEnd()
    
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.3, 0.3)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.6, 0.6)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.9, 0.9)
    glEnd()
    
    # yellow
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.2, 0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, 0.2)
    glEnd()
    
    glColor3f(0.0, 1.0, 1.0)
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.8, -0.3)
    glVertex2f(-0.8, -0.6)
    glVertex2f(-0.5, -0.8)
    glVertex2f(-0.2, -0.6)
    glVertex2f(-0.2, -0.3)
    glEnd()
    
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_POLYGON)
    glVertex2f(0.5, -0.1)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.2, -0.6)
    glVertex2f(0.5, -0.8)
    glVertex2f(0.8, -0.6)
    glVertex2f(0.8, -0.3)
    glEnd()
    
    glFlush()
def do_main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Graph Primitive")
    init()
    glutDisplayFunc(draw_func)
    #glutIdleFunc(draw_func)
    glutMainLoop()
if __name__ == "__main__":
    do_main()