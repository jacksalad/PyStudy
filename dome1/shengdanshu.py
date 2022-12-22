import turtle as t
import random

# 到达指定位置
def toPos(x,y):
    t.penup()
    t.goto((x,y))
    t.pendown()

# 绘制圣诞树
def tree(d,s):
    t.color("green")
    if d <=0:
        return
    t.forward(s)
    tree(d-1,s*.8)
    t.right(120)
    tree(d-3,s*.5)
    t.right(120)
    tree(d-3,s*.5)
    t.right(120)
    t.backward(s)

#绘制果实
def fruit(r):
    c=["pink","red","orange"][random.randint(0,2)]
    t.color(c)
    t.circle(r,360)

# 绘制果实群
def drawFruit(num):
    for i in range(num):
        y=random.randint(-300,200)
        x=(-0.4*y+40)*random.choice([-1,1])*random.random()
        toPos(x,y)
        fruit(5)

# 绘制五角星
def star(d):
    t.color("yellow","yellow")
    t.begin_fill()

# 绘制雪花
def snow(n,d):
    t.color("white")
    for i in range(n):
        t.forward(d)
        t.backward(d)
        t.right(360/n)

# 绘制雪花群
def drawSnows(num):
    for i in range(num):
        x=random.randint(-800,800)
        y=random.randint(-300,400)
        d=random.randint(10,20)
        n=random.randint(4,6)
        toPos(x,y)
        snow(n,d)

# 绘制文字
def drawwrite(str):
    t.color("dark red")
    t.write(str,align="center",font=("Comic Sana MS",40,"bold"))

# 基本参数
t.speed("fastest")
t.pensize(5)
t.screensize(bg="black")

#主程序
toPos(0,-350)
drawwrite("Mreey christmas!")
drawSnows(60)
toPos(0,250)
t.setheading(252)
star(30)
toPos(0,-300)
t.setheading(90)
tree(10,100)
drawFruit(80)

t.done()
