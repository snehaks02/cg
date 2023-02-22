import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

wsize = 700
step = 0
theta=0
inc=-400

coordinate = [[0, 0], [100, 100]]


def display():
    global coordinate
    global step,inc
    global x,y,r
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    #coordinate[0][0]=inc
    #coordinate[0][0]=inc

    glVertex2f(coordinate[0][0] / wsize, coordinate[0][1] / wsize)
    glVertex2f(coordinate[1][0] / wsize, coordinate[1][1] / wsize)
    # coordinate[0][0]+=1
    coordinate[1][1] = math.sin((math.radians(step))) * 100

    inc+=1
    step += 1

    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-(coordinate[0][0] / wsize), coordinate[0][1] / wsize)
    glVertex2f(-(coordinate[1][0] / wsize), coordinate[1][1] / wsize)
    # coordinate[0][0]+=1
    coordinate[1][1] = math.sin((math.radians(step))) * 100
    glEnd()
    circle(0,60,50)
    body()
    leg()

    glFlush()
    time.sleep(0.02)

def circle(x,y,r,):
    glPointSize(1)
    glColor3f(1,0,0)
    glBegin(GL_POINTS)
    for theta in range(0,361,1):
        glVertex2f((r*math.cos(math.radians(theta))+x )/wsize,(r*math.sin(math.radians(theta))+y)/wsize)
    glEnd()
    glFlush()

def body():
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(0,-100/wsize)
    #coordinate[0][0]+=1
    glEnd()

def leg():
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(0,-90/wsize)
    glVertex2f(-30/wsize,-250/wsize)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, -90 / wsize)
    glVertex2f(30 / wsize, -250 / wsize)
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
