def left(event):
    x = -10
    y = 0
    self.canvas.move(self.nave, x, y)


def right(event):
    x = 10
    y = 0
    self.canvas.move(self.nave, x, y)


def up(event):
    x = 0
    y = -10
    self.canvas.move(self.nave, x, y)


def down(event):
    x = 0
    y = 10
    self.canvas.move(self.nave, x, y)


master.bind("<Left>", left)
master.bind("<Right>", right)
master.bind("<Up>", up)
master.bind("<Down>", down)

app = timer()
app = mainloop()
app = timer()

x = -10
y = 0
self.canvas.move(self.nave, x, y)
if self.coordenadas[0] >= 49:
    self.canvas.coords(self.nave, x + -10, y)
    self.canvas.move(self.nave, x, y)

