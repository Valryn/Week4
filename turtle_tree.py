import turtle
red = 50
green = 75

def tree(branchLen,t):
    if branchLen > 5:
        t.width(branchLen//5)
        t.color(red + branchLen//3, green - branchLen//2, 10)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.screen.colormode(255)
    tree(75,t)
    myWin.exitonclick()

main()
