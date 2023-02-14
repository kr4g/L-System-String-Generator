# BROKEN
# import pygame
# import math
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *

# def draw_cone(radius, height):
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex3f(0, 0, height)
#     angle = 0
#     while angle < 2 * math.pi:
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         glVertex3f(x, y, 0)
#         angle = angle + 0.1
#     glEnd()
#     base_center = [0, 0, 0]
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex3f(*base_center)
#     angle = 0
#     while angle < 2 * math.pi:
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         glVertex3f(x, y, 0)
#         angle = angle + 0.1
#     glEnd()
#     glBegin(GL_QUAD_STRIP)
#     angle = 0
#     while angle < 2 * math.pi:
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         glVertex3f(x, y, 0)
#         glVertex3f(x, y, height)
#         angle = angle + 0.1
#     glEnd()

# def main():
#     pygame.init()
#     display = (800, 600)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     height = 1.0  # initial height
#     radius = 1.0  # initial radius
#     gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
#     glTranslatef(0.0, 0.0, -5)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.unicode == 'w':
#                     height += 0.1  # increase height
#                 elif event.unicode == 's':
#                     height -= 0.1  # decrease height

#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         draw_cone(radius, height)
#         pygame.display.flip()
#         pygame.time.wait(10)

# main()
