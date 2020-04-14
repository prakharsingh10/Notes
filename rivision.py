from tkinter import *
import random
import time

root = Tk()
root.resizable(0, 0)

gamecanvas = Canvas(width=500, height=500)
gamecanvas.config(bg="pink")
gamecanvas.pack()
score = Label(root, text="Score")
score.pack()
scorevalue = Label(root, text="Score")
scorevalue.pack()
listx = [-1, -2, -3, 1, 2, 3]
listy = [-4]
count = 0


class Ball:
    def __init__(self, color, canvas, paddle):
        global listx
        global listy
        self.paddle = paddle
        self.canvas = canvas
        self.id = self.canvas.create_oval(250, 250, 290, 290, fill=color)
        self.x = random.choice(listx)
        self.y = random.choice(listy)

    def ballmotion(self):
        global count
        self.canvas.move(self.id, self.x, self.y)
        self.canvas.update()
        a = self.canvas.coords(self.paddle.id)
        time.sleep(0.01)
        ballcoords = self.canvas.coords(self.id)
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
                250, 250, text=f"GAME OVER !!! \n Your Score : {count}"
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
        self.id = self.canvas.create_rectangle(220, 490, 290, 499, fill=color)
        self.y = -2
        self.x = 0

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

    def up(self, event):
        self.y = -2

    def down(self, event):
        self.y = 2

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


paddle = Paddle(gamecanvas, "blue")
ball = Ball("red", gamecanvas, paddle)
while 1:
    ball.ballmotion()
    paddle.paddlemotion()

root.mainloop()
