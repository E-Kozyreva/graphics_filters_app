import math
import random
from progress.bar import IncrementalBar
from PIL import Image

class Filters:
    def __init__(self, image):
        self.image = image
        self.pixels = image.load()
        self.width, self.height = image.size
        self.pixels = list(image.getdata())


class SpotFilters(Filters):
    def inversion(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")
           
        new_pixels = []

        bar = IncrementalBar('Inversion filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((255 - pixel[0], 255 - pixel[1], 255 - pixel[2]))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/inversion.jpg', 'JPEG')
        bar.finish()

    
    def grayscale(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Grayscale filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((int((pixel[0] + pixel[1] + pixel[2]) / 3), 
                               int((pixel[0] + pixel[1] + pixel[2]) / 3), 
                               int((pixel[0] + pixel[1] + pixel[2]) / 3)))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/grayscale.jpg', 'JPEG')
        bar.finish()


    def blackwhite(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Black and white filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            if (pixel[0] + pixel[1] + pixel[2]) / 3 > 128:
                new_pixels.append((255, 255, 255))
            else:
                new_pixels.append((0, 0, 0))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/blackwhite.jpg', 'JPEG')
        bar.finish()


    def sepia(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Sepia filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((int((pixel[0] * 0.393) + (pixel[1] * 0.769) + (pixel[2] * 0.189)),
                               int((pixel[0] * 0.349) + (pixel[1] * 0.686) + (pixel[2] * 0.168)),
                               int((pixel[0] * 0.272) + (pixel[1] * 0.534) + (pixel[2] * 0.131))))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/sepia.jpg', 'JPEG')
        bar.finish()

    
    def brightness(self, value=2):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Brightness filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((int(pixel[0] + value), int(pixel[1] + value), int(pixel[2] + value)))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/brightness.jpg', 'JPEG')
        bar.finish()


    def contrast(self, value=2):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Contrast filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((int(pixel[0] * value), int(pixel[1] * value), int(pixel[2] * value)))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/contrast.jpg', 'JPEG')
        bar.finish()


    def gamma(self, value=2):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Gamma filter', 
                             max = len(self.pixels),
                                suffix = '%(percent)d%%',
                                fill = '#',
                                empty = ' ',
                                width = 50,
                                max_refresh_rate = 0.1,
                                poll = 0.1,
                                bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((int(pixel[0] ** value), int(pixel[1] ** value), int(pixel[2] ** value)))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/gamma.jpg', 'JPEG')
        bar.finish()


    def blur(self, value=2):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Blur filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((int(pixel[0] / value), int(pixel[1] / value), int(pixel[2] / value)))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/blur.jpg', 'JPEG')
        bar.finish()    


    def green(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Green filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((0, pixel[1], 0))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/green.jpg', 'JPEG')
        bar.finish()

    
    def red(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Red filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((pixel[0], 0, 0))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/red.jpg', 'JPEG')
        bar.finish()


    def blue(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        new_pixels = []

        bar = IncrementalBar('Blue filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for pixel in self.pixels:
            new_pixels.append((0, 0, pixel[2]))
            bar.next()

        newimg.putdata(new_pixels)
        newimg.save('results/output/spot/blue.jpg', 'JPEG')
        bar.finish()


class MatrixFilters(Filters):
    def sobel(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        sobelx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]                                  
        sobely = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]                             

        bar = IncrementalBar('Sobel filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(1, self.width - 1):                                           
            for y in range(1, self.height - 1):                                      
                sumx = 0                                                           
                sumy = 0                                                  
                for i in range(3):                                                
                    for j in range(3):                                 
                        sumx += self.image.getpixel((x + i - 1, y + j - 1))[0] * sobelx[i][j] 
                        sumy += self.image.getpixel((x + i - 1, y + j - 1))[0] * sobely[i][j] 
                sumx = math.sqrt(sumx ** 2)                                      
                sumy = math.sqrt(sumy ** 2)                                         

                length = sumx + sumy                                                  
                length = length / 2164 * 255                                                     
                length = int(length)                                                   

                newimg.putpixel((x, y), (length, length, length))  
                bar.next()

        newimg.save('results/output/matrix/sobel.jpg', 'JPEG')   
        bar.finish()


    def sharpen(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        sharpen = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]   

        bar = IncrementalBar('Sharpen filter', 
                             max = len(self.pixels), 
                             suffix = '%(percent)d%%', 
                             fill = '#', 
                             empty = ' ', 
                             width = 50, 
                             max_refresh_rate = 0.1, 
                             poll = 0.1, 
                             bar_template = '%(bar)s %(percent)3d%%')
        

        for x in range(1, self.width - 1):                          
            for y in range(1, self.height - 1):                      
                new_r, new_g, new_b = 0, 0, 0                   
                for a in range(3):                             
                    for b in range(3):

                        p = self.image.getpixel((x + a - 1, y + b - 1)) 
                        r, g, b_channel = p[0], p[1], p[2]       
                        new_r += r * sharpen[a][b]                  
                        new_g += g * sharpen[a][b]                  
                        new_b += b_channel * sharpen[a][b]

                new_r = 0 if new_r < 0 else new_r               
                new_g = 0 if new_g < 0 else new_g
                new_b = 0 if new_b < 0 else new_b

                new_r = 255 if new_r > 255 else new_r
                new_g = 255 if new_g > 255 else new_g
                new_b = 255 if new_b > 255 else new_b

                newimg.putpixel((x, y), (new_r, new_g, new_b))     
                bar.next()

        newimg.save('results/output/matrix/sharpen.jpg', 'JPEG')   
        bar.finish()


    def operator_scharra(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        operator_x = [[3, 0, -3], [10, 0, -10], [3, 0, -3]]
        operator_y = [[3, 10, 3], [0, 0, 0], [-3, -10, -3]]

        bar = IncrementalBar('Scharra filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                sum_x = 0
                sum_y = 0
                for i in range(3):
                    for j in range(3):
                        sum_x += self.image.getpixel((x + i - 1, y + j - 1))[0] * operator_x[i][j]
                        sum_y += self.image.getpixel((x + i - 1, y + j - 1))[0] * operator_y[i][j]
                sum_x = math.sqrt(sum_x ** 2)
                sum_y = math.sqrt(sum_y ** 2)

                length = sum_x + sum_y
                length = length / 4328 * 255
                length = int(length)

                newimg.putpixel((x, y), (length, length, length))
                bar.next()

        newimg.save('results/output/matrix/operator_scharra.jpg', 'JPEG')
        bar.finish()

    
    def operator_pruitt(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        operator_x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
        operator_y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]

        bar = IncrementalBar('Pruitt filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                sum_x = 0
                sum_y = 0
                for i in range(3):
                    for j in range(3):
                        sum_x += self.image.getpixel((x + i - 1, y + j - 1))[0] * operator_x[i][j]
                        sum_y += self.image.getpixel((x + i - 1, y + j - 1))[0] * operator_y[i][j]
                sum_x = math.sqrt(sum_x ** 2)
                sum_y = math.sqrt(sum_y ** 2)

                length = sum_x + sum_y
                length = length / 4328 * 255
                length = int(length)

                newimg.putpixel((x, y), (length, length, length))
                bar.next()

        newimg.save('results/output/matrix/operator_pruitt.jpg', 'JPEG')
        bar.finish()


    def waves_1(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        bar = IncrementalBar('Waves filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                new_x = x
                new_y = y + 20 * math.sin(2 * math.pi * x / 128)
                if new_y < 0:
                    new_y = 0
                if new_y > self.height - 1:
                    new_y = self.height - 1
                newimg.putpixel((x, y), self.image.getpixel((new_x, new_y)))
                bar.next()

        newimg.save('results/output/matrix/waves_1.jpg', 'JPEG')
        bar.finish()
    

    def waves_2(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   

        bar = IncrementalBar('Waves filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                new_x = x + 20 * math.sin(2 * math.pi * y / 128)
                new_y = y
                if new_x < 0:
                    new_x = 0
                if new_x > self.width - 1:
                    new_x = self.width - 1
                newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y))))
                bar.next()

        newimg.save('results/output/matrix/waves_2.jpg', 'JPEG')
        bar.finish()

    
    def mirror(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")

        bar = IncrementalBar('Mirror filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                new_x = x + (random.random() - 0.5) * 10
                new_y = y + (random.random() - 0.5) * 10

                if new_x < 0:
                    new_x = 0
                if new_x > self.width - 1:
                    new_x = self.width - 1
                if new_y < 0:
                    new_y = 0
                if new_y > self.height - 1:
                    new_y = self.height - 1

                newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y))))
                bar.next()


        newimg.save('results/output/matrix/mirror.jpg', 'JPEG')
        bar.finish()


    def motion_blur(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")

        bar = IncrementalBar('Motion blur filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        kernel_size = 10
        kernel = []
        for i in range(kernel_size):
            kernel.append(1 / kernel_size)

        for x in range(self.width):
            for y in range(self.height):
                r = 0
                g = 0
                b = 0
                for i in range(kernel_size):
                    pixel = self.image.getpixel((x, (y - i) % self.height))
                    r += pixel[0] * kernel[i]
                    g += pixel[1] * kernel[i]
                    b += pixel[2] * kernel[i]
                newimg.putpixel((x, y), (int(r), int(g), int(b)))
                bar.next()

        newimg.save('results/output/matrix/motion_blur.jpg', 'JPEG')
        bar.finish()


    def shift(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")

        bar = IncrementalBar('Shift filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                new_x = x + 50
                new_y = y
                if new_x < 0:
                    new_x = 0
                if new_x > self.width - 1:
                    new_x = self.width - 1
                if new_y < 0:
                    new_y = 0
                if new_y > self.height - 1:
                    new_y = self.height - 1
                newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y))))
                bar.next()

        newimg.save('results/output/matrix/shift.jpg', 'JPEG')
        bar.finish()


    def rotate(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")

        bar = IncrementalBar('Rotate filter',
                            max = len(self.pixels),
                            suffix = '%(percent)d%%',
                            fill = '#',
                            empty = ' ',
                            width = 50,
                            max_refresh_rate = 0.1,
                            poll = 0.1,
                            bar_template = '%(bar)s %(percent)3d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                new_x = (x - self.width / 2) * math.cos(math.pi / 6) - (y - self.height / 2) * math.sin(math.pi / 6) + self.width / 2
                new_y = (x - self.width / 2) * math.sin(math.pi / 6) + (y - self.height / 2) * math.cos(math.pi / 6) + self.height / 2
                if new_x < 0:
                    new_x = 0
                if new_x > self.width - 1:
                    new_x = self.width - 1
                if new_y < 0:
                    new_y = 0
                if new_y > self.height - 1:
                    new_y = self.height - 1

                newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y))))
                bar.next()

        newimg.save('results/output/matrix/rotate.jpg', 'JPEG')
        bar.finish()