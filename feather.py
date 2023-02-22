from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time

wsize = 1000
step = 1


def display():
    global step
    glClear(GL_COLOR_BUFFER_BIT)
    draw_mayil()
    glFlush()
    step += 1

    time.sleep(.5)


def draw_mayil():
    for i in range(step % 10 + 1):
        line(i * 10)
        line(-i * 10)


def line(angle):
    glColor3f(1, 0, 0)
    rad = 100
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    x, y = rad * math.cos(math.radians(90 - angle)), rad * math.sin(math.radians(90 - angle))
    glVertex2f(x / wsize, y / wsize)
    glEnd()
    ellipse(x, y)


def ellipse(xc, yc):
    glColor3f(0, 0, 1)
    for i in range(0, 361, 1):
        glBegin(GL_LINES)
        x, y = (10 * math.cos(math.radians(i)), 20 * math.sin(math.radians(i)))
        glVertex2f(xc / wsize, yc / wsize)
        glVertex2f((x + xc) / wsize, (y + yc) / wsize)
        glEnd()


def main():
    glutInit()
    glutInitWindowSize(wsize, wsize)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("ball")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    # gluOrtho2D(-wsize, wsize, -wsize, wsize)
    glutMainLoop()


main()
