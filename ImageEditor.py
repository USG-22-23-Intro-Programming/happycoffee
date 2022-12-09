

from graphics import*
from Button import*


def darken(I):
    x = I.getWidth()
    y = I.getHeight()

    for i in range(x):
        for j in range(y):
            pix = I.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red - 10
            green = green - 10
            blue = blue - 10

            #print([red, green, blue])
            c = color_rgb(abs(red), abs(green), abs(blue))
            I.setPixel(i, j, c)


def lighten(I):
    x = I.getWidth()
    y = I.getHeight()
    
    for i in range(x):
        for j in range(y):
            pix = I.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red + 50
            green = green + 50
            blue = blue + 50

            if blue > 255:
                blue = 255
            if green > 255:
                green = 255
            if red > 255:
                red = 255

            c = color_rgb(abs(red), abs(green), abs(blue))
            I.setPixel(i, j, c)


def greyscale(I):
    x = I.getWidth()
    y = I.getHeight() 
    for i in range(x):
        for j in range(y):
            pix = I.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if ((red == green) and (green == blue)):
                c = color_rgb(red, green, blue)
            else:
                x = (red+green+blue)/3
                c = color_rgb(int(x), int(x), int(x))
                I.setPixel(i, j, c)

def contrast(I):
    x = I.getWidth()
    y = I.getHeight()
    for i in range(x):
        for j in range(y):
            pix = I.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if red>125:
                red = red + 50
            else:
                red = red - 50
            if green>125:
                green = green + 50
            else:
                green = green - 50
            if blue>125:
                blue = blue + 50
            else:
                blue = blue - 50
            if red<0:
                red=0
            if green<0:
                green=0
            if blue<0:
                blue=0
            if red>255:
                red=255
            if green>255:
                green=255
            if blue>255:
                blue=255
            
            c = color_rgb(red, green, blue)
            I.setPixel(i, j, c)
    




def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("MistyRose3")

    I = Image(Point(300,300), "MUN.png")
    I.draw(win)
    
    B = Button(win, Point(600, 100), Point(700, 175), "PaleTurquoise4", "Darken")
    B2 = Button(win, Point(600, 200), Point(700, 275), "PaleTurquoise4", "Lighten")
    S = Button(win, Point(600, 300), Point(700, 375), "PaleTurquoise4", "Greyscale")
    S2 = Button(win, Point(600, 400), Point(700, 475), "PaleTurquoise4", "Contrast")
    Q = Button(win, Point(600, 500), Point(700, 575), "coral2", "QUIT")

    while True: 
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        if B2.isClicked(m):
            lighten(I)

        if S.isClicked(m):
            greyscale(I)

        if S2.isClicked(m):
            contrast(I)
    
        if Q.isClicked(m):
            break

    win.close()


if __name__ == "__main__":
    main()

