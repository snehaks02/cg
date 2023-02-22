from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math
x=0
y=0
theta=0
wsize=600
size=100

def draw():
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    square(x,y)
    glutSwapBuffers()

def square(x,y):
    glBegin(GL_QUADS)
    glVertex2f((x-50)*math.cos(theta)-(y+50)*math.sin(theta),(y+50)*math.cos(theta)-(x-50)*math.sin(theta))
    glVertex2f((x+50)*math.cos(theta)-(y+50)*math.sin(theta),(y+50)*math.cos(theta)-(x+50)*math.sin(theta))
    glVertex2f((x+50)*math.cos(theta)-(y-50)*math.sin(theta),(y-50)*math.cos(theta)-(x+50)*math.sin(theta))
    glVertex2f((x-50)*math.cos(theta)-(y-50)*math.sin(theta),(y-50)*math.cos(theta)-(x-50)*math.sin(theta))
    glEnd()
    glFlush()

def animate(temp):
    global x,y,theta
    glutPostRedisplay()
    glutTimerFunc(int(100000/60),animate,int(0))
    if (theta>=360):
        theta=0
    theta+=1

def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow("square")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()
main()



