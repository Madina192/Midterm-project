from tkinter import *
from time import sleep
from random import randint, choice
from turtle import heading


class Field:
    def __init__(self, c, n, m, width, height, walls=False):

        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(0)

        self.a[18][3] = 1
        self.a[19][3] = 1
        self.a[20][3] = 1
        self.a[17][4] = 1
        self.a[21][4] = 1
        self.a[16][5] = 1
        self.a[22][5] = 1
        self.a[15][6] = 1
        self.a[23][6] = 1
        self.a[14][7] = 1
        self.a[24][7] = 1
        self.a[13][8] = 1
        self.a[25][8] = 1
        self.a[13][9] = 1
        self.a[25][9] = 1
        self.a[14][10] = 1
        self.a[24][10] = 1
        self.a[15][11] = 1
        self.a[23][11] = 1
        self.a[16][12] = 1
        self.a[22][12] = 1
        self.a[17][13] = 1
        self.a[21][13] = 1
        self.a[18][14] = 1
        self.a[20][14] = 1
        self.a[19][14] = 1
        self.a[17][7] = 2
        self.a[21][7] = 2
        self.a[17][10] = 3
        self.a[18][11] = 3
        self.a[19][11] = 3
        self.a[20][11] = 3
        self.a[21][10] = 3
        self.draw()

    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)

        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                if self.a[i][j] == 3:
                    b[i][j] = 2
                elif self.a[i][j] == 2:
                    b[i][j] = 1
                elif self.a[i][j] == 1:
                    if self.a[i-1][j] == 3 or self.a[i+1][j] == 3 or self.a[i][j-1] == 3 or self.a[i][j+1]:
                        b[i][j] = 3
                    elif self.a[i-1][j-1] == 3 or self.a[i+1][j-1] == 3 or self.a[i-1][j+1] == 3 or self.a[i+1][j+1] == 3:
                        b[i][j] = 3
                    else:
                        b[i][j] = 1
                else:
                    b[i][j] = 0
        self.a = b

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        color = "grey"
        sizem = self.width // (self.m - 2)
        sizen = self.height // (self.n - 2)
        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                if (self.a[i][j]) == 1:
                    color = "yellow"
                elif (self.a[i][j] == 2):
                    color = "black"
                elif (self.a[i][j] == 3):
                    color = "red"
                else:
                    color = "white"
                self.c.create_rectangle(
                    (i-1) * sizem, (j-1) * sizen, (i) * sizem, (j) * sizen, fill=color)
        self.step()
        self.c.after(200, self.draw)


class Player:
    def __init__(self, c, x, y, size, color="RED"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.c = c
        self.body = self.c.create_oval(self.x - self.size / 2,
                                       self.y - self.size / 2,
                                       self.x + self.size / 2,
                                       self.y + self.size / 2,
                                       fill=self.color)

    def moveto(self, x, y):
        self.mx = x
        self.my = y
        self.dx = (self.mx - self.x) / 50
        self.dy = (self.my - self.y) / 50
        self.draw()

    def draw(self):

        self.x += self.dx
        self.y += self.dy
        self.c.move(self.body, self.dx, self.dy)

        print(abs(self.x))
        if abs(self.mx - self.x) > 2:
            self.c.after(200, self.draw)

    def distance(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5


root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()

f = Field(c, 40, 40, 800, 800)
f.print_field()

root.mainloop()
