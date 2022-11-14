from graphics import*
from Button import*



def main():

    win = GraphWin("character creator", 800, 600)
    win.setBackground("MistyRose3")

    C = Circle(Point(300,300), 150)
    C.draw(win)

    L = Line(Point(300, 325), Point(300, 225))
    
    BigEye1 = Circle(Point(200, 250), 50)
    BigEye2 = Circle(Point(400, 250), 50)

    smallEye1 = Circle(Point(250, 250), 20)
    smallEye2 = Circle(Point(350, 250), 20)

    T = Polygon(Point(300, 225), Point(245, 315), Point(355, 315))

    d = Line(Point(245, 415), Point(355, 415))

    e = Rectangle(Point(245, 345), Point(355, 335))

    B = Button(win, Point(600, 100), Point(700, 175), "PaleTurquoise4", "Big Eyes")
    B2 = Button(win, Point(600, 200), Point(700, 275), "PaleTurquoise4", "Small eyes")

    C = Button(win, Point(600, 300), Point(700, 375), "PaleTurquoise4", "Line Nose")
    t = Button(win, Point(600, 400), Point(700,475), "PaleTurquoise4", "Triangle Nose")

    Q = Button(win, Point(600, 500), Point(700, 575), "coral2", "QUIT")

    D = Button(win, Point(459, 500), Point(559, 575), "PaleTurquoise4", "Line Mouth")

    E = Button(win, Point(337, 500), Point(437, 575), "PaleTurquoise4", "Rectangle Mouth")

    while True: 
        m = win.getMouse()
        
        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            
            BigEye1.draw(win)
            BigEye2.draw(win)

        if B2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw() 
            
            smallEye1.draw(win)
            smallEye2.draw(win)

        if C.isClicked(m):
            T.undraw()
            L.undraw()

            L.draw(win)

        if t.isClicked(m):
            L.undraw()
            T.undraw()

            T.draw(win)

        if D.isClicked(m):
            d.undraw()
            e.undraw()

            d.draw(win)

        if E.isClicked(m):
            e.undraw()
            d.undraw()

            e.draw(win)
            
            
           
        if Q.isClicked(m):
            break

    win.close()


if __name__ == "__main__":
    main()
