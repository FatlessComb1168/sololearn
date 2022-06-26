from PIL import Image, ImageFont, ImageDraw, ImageOps
from math import sin, cos
from random import randint, choice

# Letters
l = ([chr(i) for i in range(48, 58)] +
    [chr(i) for i in range(65, 91)] +
    [chr(i) for i in range(97, 120)])

# Fonts
fonts = ['arial.ttf', ]
func = choice(['sin', 'cos'])
mult = randint(10, 20)

def rc(): # Random color tuple
    return tuple([randint(0, 255) for i in range(3)])

def rp(n): # Random position
    return (5 + n * 20 + randint(-5, 10), randint(0, 20))

def rp2():
    x = randint(1, 100)
    return ((randint(1, 200), randint(1, x)),
        (randint(1, 200), randint(1, x)))

# https://medium.com/geekculture/deforming-images-in-python-66e0d0dcb17f
class WaveDeformer:
    def transform(self, x, y):
        y = eval(f'y + {mult} * {func}(x / 40)')
        return x, y

    def transform_rectangle(self, x0, y0, x1, y1):
        return (*self.transform(x0, y0),
                *self.transform(x0, y1),
                *self.transform(x1, y1),
                *self.transform(x1, y0),
                )

    def getmesh(self, img):
        self.w, self.h = img.size
        gridspace = 20

        target_grid = []
        for x in range(0, self.w, gridspace):
            for y in range(0, self.h, gridspace):
                target_grid.append((x, y, x + gridspace, y + gridspace))

        source_grid = [self.transform_rectangle(*rect) for rect in target_grid]

        return [t for t in zip(target_grid, source_grid)]

class captcha:
    def __init__(self):
        self.text = ''.join([choice(l) for i in range(5)])
        self.color = rc()
        self.textcolor = rc()
        self.strokecolor = tuple([randint(0, 100)] * 3)
        self.image = Image.new('RGB', (200, 100), self.color)

        idraw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arial.ttf', size = 48)

        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                self.image.putpixel((i, j), rc())

        '''
        for i in range(5):
            idraw.text(rp(i), self.text[i], font = font, fill = rc(),
                stroke_fill = rc(), stroke_width = randint(0, 2))
        '''
        
        idraw.text((randint(0, 40), randint(0, 40)),
            self.text, font = font, fill = self.textcolor,
            stroke_fill = self.strokecolor, stroke_width = randint(2, 3))

        for i in range(randint(1, 30)):
            idraw.line(rp2(), fill = rc())

        self.image = ImageOps.deform(self.image, WaveDeformer())
        
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                if self.image.getpixel((i, j)) == self.textcolor:
                    self.image.putpixel((i, j), rc())

        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                if self.image.getpixel((i, j)) == (0, 0, 0):
                    self.image.putpixel((i, j), rc())

def main():
    c = captcha()
    print(c.text)
    c.image.show()
    c.image.save(c.text + '.png')
    input()

if __name__ == "__main__":
    main()