from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math
wsize=700
x=0
y=0
tx=1
size=100

dir=0

def draw():
    global x,y
    glColor3f(1,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    star(x,y)
    glutSwapBuffers()

def star(x,y):
    glBegin(GL_POLYGON)
    glVertex2f((x-100)*tx,(y+100)*tx)
    glVertex2f(x*tx,(y+400)*tx)
    glVertex2f((x+100)*tx,(y+100)*tx)
    glVertex2f((x+400)*tx,y*tx)
    glVertex2f((x+100)*tx,(x-100)*tx)
    glVertex2f(x*tx,(y-400)*tx)
    glVertex2f((x-100)*tx,(y-100)*tx)
    glVertex2f((x-400)*tx,y*tx)
    glEnd()
    glFlush()

def animate(temp):
    global x,y,tx,dir
    glutPostRedisplay()
    glutTimerFunc(int(10000/60),animate,int(0))
    if (dir==0):
        tx-=1
        if(tx<=0):
            dir=1
    elif(dir==1):
        tx+=1
        if(tx>=1):
            dir=0

def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow("star")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()
main()



