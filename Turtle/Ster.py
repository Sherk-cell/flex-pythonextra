Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> bgcolor("black")
color("yellow")
speed(0)

begin_fill()
points = 1
while points < 5:
    forward(250)
    left(145)
    points = points + 1
end_fill()
SyntaxError: multiple statements found while compiling a single statement
>>> bgcolor("black")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    bgcolor("black")
NameError: name 'bgcolor' is not defined
>>> turtle.bgcolor("black")
>>> turtle.color("yellow")
>>> turtle.speed(0)
>>> turtle.begin_fill()
>>> points = 1
>>> while points <5
SyntaxError: invalid syntax
>>> while points<5
SyntaxError: invalid syntax
>>> forward(250)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    forward(250)
NameError: name 'forward' is not defined
>>> turtle.fd(250)
>>> turtle.lt(145)
>>> turtle.fd(250)
>>> turtle.lt(145)
>>> turtle.fd(250)
>>> turtle.lt(145)
>>> turtle.fd(250)
>>> turtle.lt(145)
>>> turtle.fd(250
turtle.fd(250
	  
SyntaxError: invalid syntax
>>> turtle.fd(250)
>>> end_fill()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    end_fill()
NameError: name 'end_fill' is not defined
>>> turtle.end_fill()
>>> 