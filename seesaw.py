from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import math
import time

wsize=700
theta=0
step=0
coordinate=[[0,0],[300,300]]


def display():
    global coordinate,step
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(4)
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex2f((coordinate[0][0])/wsize,(coordinate[0][1]/wsize))
    glVertex2f((coordinate[1][0])/wsize,(coordinate[1][1])/wsize)
    coordinate[1][1] = math.sin((math.radians(step))) * 100
    step+=1
    glEnd()
    glBegin(GL_LINES)
    glVertex2f((-coordinate[0][0]) / wsize, (coordinate[0][1] / wsize))
    glVertex2f((-coordinate[1][0]) / wsize, (coordinate[1][1]) / wsize)
    coordinate[1][1] = -math.sin((math.radians(step))) * 100
    glEnd()
    triangle()
    glFlush()
    time.sleep(0.02)

def triangle():
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(-60/wsize,-60/wsize)
    glVertex2f(60/wsize,-60/wsize)
    glEnd()


def main():
    glutInit()
    glutInitWindowSize(wsize, wsize)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("star")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()


main()