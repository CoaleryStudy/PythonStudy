from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()

n, line = map(int, input().split())
turtle.shape('turtle')
turtle.speed('fastest')

for i in range(n):
    turtle.forward(line)
    turtle.right((360 / n) * 2)
    turtle.forward(line)
    turtle.left(360 / n)

screen.mainloop()

'''
import turtle as t
 
n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.forward(line)
    t.right((360 / n) * 2)
    t.forward(line)
    t.left(360 / n)

t.mainloop()

# Error occurred 'Module 'turtle' has no '~' member'
# Anyway It worked.
'''

# https://stackoverflow.com/questions/52902627/e1101module-turtle-has-no-forward-member