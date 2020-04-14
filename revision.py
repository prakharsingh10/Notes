from tkinter import *
import random
import time

root = Tk()
root.resizable(0, 0)
paddlecolor = input("choose your paddle color>")
ballcolor = input("choose your ball color>")
mode = input(
    "Please select mode \n 'a' for rainbow \n 'b' for dotted rainbow \n 'c' for only dotted.>"
)
gamecanvas = Canvas(width=500, height=500)
gamecanvas.config(bg="black")
gamecanvas.pack()
score = Label(root, text="Score")
score.pack()
scorevalue = Label(root, text="")
scorevalue.pack()
listx = [-1, -2, -3, 1, 2, 3]
listy = [-2]
count = 0
if mode == "a" or mode == "b":
    gamecanvas.create_oval(0, 0, 500, 500, fill="violet")
    gamecanvas.create_oval(0, 0, 400, 400, fill="indigo")
    gamecanvas.create_oval(0, 0, 300, 300, fill="green")
    gamecanvas.create_oval(0, 0, 200, 200, fill="yellow")
    gamecanvas.create_oval(0, 0, 115, 115, fill="orange")
    gamecanvas.create_oval(0, 0, 50, 50, fill="red")
    gamecanvas.create_rectangle(430, 430, 500, 500, fill="white")
    gamecanvas.create_rectangle(440, 440, 500, 500, fill="pink")
    gamecanvas.create_rectangle(450, 450, 500, 500, fill="orange")
    gamecanvas.create_rectangle(460, 460, 500, 500, fill="yellow")
    gamecanvas.create_rectangle(470, 470, 500, 500, fill="green")
    gamecanvas.create_rectangle(480, 480, 500, 500, fill="indigo")
    gamecanvas.create_rectangle(490, 490, 500, 500, fill="violet")
    gamecanvas.create_line(0, 0, 500, 500)
y = 0
x = 0
if mode == "b" or mode == "c":
    for i in range(84):
        gamecanvas.create_rectangle(0, y, 500, y + 4, fill="white")
        gamecanvas.create_rectangle(x, 0, x + 4, 500, fill="white")
        x += 8
        y += 8


class Ball:
    def __init__(self, color, canvas, paddle):
        global listx
        global listy
        self.paddle = paddle
        self.canvas = canvas
        self.id = self.canvas.create_oval(220, 200, 290, 270, fill=color)
        """self.x = random.choice(listx)
        self.y = random.choice(listy)"""
        self.x = self.paddle.x
        self.y = random.choice(listy)

    def ballmotion(self):
        global count
        self.canvas.move(self.id, self.x, self.y)
        self.canvas.update()
        a = self.canvas.coords(self.paddle.id)
        time.sleep(0.01)
        ballcoords = self.canvas.coords(self.id)
        b = ballcoords
        if ballcoords[0] <= 0 or ballcoords[2] >= 500:
            self.x = -self.x
        if ballcoords[1] <= 0:
            self.y = -self.y
            count += 1
            scorevalue.configure(text=str(count))

        if ballcoords[3] >= 500:
            self.y = -self.y
            self.x = 0
            self.y = 0
            self.paddle.x = 0
            self.paddle.y = 0
            self.canvas.create_text(
                int((a[0] + a[2]) / 2),
                int((a[1] + a[3]) / 2),
                text=f" GAME OVER \n     Score : {count}",
            )
            self.canvas.create_text(
                int((b[0] + b[2]) / 2),
                int((b[1] + b[3]) / 2),
                text=f" o     o \n    _______",
            )

        if (
            self.y > 0
            and ballcoords[2] > a[0]
            and ballcoords[0] < a[2]
            and ballcoords[3] > a[1]
            and ballcoords[3] < a[3]
        ):
            self.y = -self.y


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(220, 430, 290, 460, fill=color)
        self.y = -1
        self.x = 2

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

    def up(self, event):
        self.y = -1

    def down(self, event):
        self.y = 1

    def paddlemotion(self):
        paddlecoords = self.canvas.coords(self.id)
        if paddlecoords[0] <= 0 or paddlecoords[2] >= 500:
            self.x = -self.x
        if paddlecoords[1] <= 190 or paddlecoords[3] >= 500:
            self.y = -self.y
        self.canvas.bind_all("<Left>", self.left)
        self.canvas.bind_all("<Right>", self.right)
        self.canvas.bind_all("<Up>", self.up)
        self.canvas.bind_all("<Down>", self.down)
        self.canvas.move(self.id, self.x, self.y)
        self.canvas.update()
        time.sleep(0.01)


paddle = Paddle(gamecanvas, paddlecolor)
ball = Ball(ballcolor, gamecanvas, paddle)
while 1:
    ball.ballmotion()
    paddle.paddlemotion()

root.mainloop()
