
from graphics import*
from Button import*


def main():

    win = GraphWin("Palindrome", 800, 600)

    Q = Button(win, Point(600, 500), Point(700, 575), "MistyRose3", "QUIT")
    Check = Button(win, Point(350, 350), Point(450, 425), "SteelBlue1", "Check")

    E = Entry(Point(400, 300), 30)
    E.draw(win)
    E.setSize(16)

    T = Text(Point(400, 250), "Write a potential Palindrome below!")
    T.draw(win)
    
    Tru = (Point(400, 230), "This is a Palindrome!")
    Fals = (Point(400, 230), "This is not a Palindrome...")
    

    while True:
        
        t = win.getMouse()
 
        if Q.isClicked(t):
            break
        
        if Check.isClicked(t):
            pal = E.getText()
            length = len(pal)
            for i in range(length):
                if pal[i] != pal[length - 1 - i]:
                    
                    Tru.undraw()
                    Fals.undraw()
                    Fals.draw(win)
                    Fals.setSize(20)
                    break
 
                else:
 
                    Tru.undraw()
                    Fals.undraw()
                    Tru.draw(win)
                    Tru.setSize(20)
                    break
 
 
    win.close()

            
    pal = E.getText()
    print(pal)

        


if __name__ == "__main__":
    main()
    
