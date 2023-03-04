import math
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

                newimg.putpixel((x,y),(length, length, length))  
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
                sumx = 0                                                                                                         
                for i in range(3):                                                
                    for j in range(3): 
                        sumx += self.pixels[x + i - 1, y + j - 1][0] * sharpen[i][j] 
                sumx = math.sqrt(sumx ** 2)                                      
                length = sumx / 9 * 255                                                     
                length = int(length)                                                   

                newimg.putpixel((x,y),(length, length, length))  
                bar.next()
        newimg.save('results/output/matrix/sharpen.jpg', 'JPEG')   
        bar.finish()


    def emboss(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   
        emboss = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]                                  
        bar = IncrementalBar('Emboss filter', 
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
                for i in range(3):                                                
                    for j in range(3): 
                        sumx += self.pixels[x + i - 1, y + j - 1][0] * emboss[i][j] 
                sumx = math.sqrt(sumx ** 2)                                      
                length = sumx / 9 * 255                                                     
                length = int(length)                                                   

                newimg.putpixel((x,y),(length, length, length))  
                bar.next()
        newimg.save('results/output/matrix/emboss.jpg', 'JPEG')   
        bar.finish()


    def edge(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   
        edge = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]                                  
        bar = IncrementalBar('Edge filter', 
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
                for i in range(3):                                                
                    for j in range(3): 
                        sumx += self.pixels[x + i - 1, y + j - 1][0] * edge[i][j] 
                sumx = math.sqrt(sumx ** 2)                                      
                length = sumx / 9 * 255                                                     
                length = int(length)                                                   

                newimg.putpixel((x,y),(length, length, length))  
                bar.next()
        newimg.save('results/output/matrix/edge.jpg', 'JPEG')   
        bar.finish()


    def gaussian(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   
        gaussian = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]                                  
        bar = IncrementalBar('Gaussian filter', 
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
                for i in range(3):                                                
                    for j in range(3): 
                        sumx += self.pixels[x + i - 1, y + j - 1][0] * gaussian[i][j] 
                sumx = math.sqrt(sumx ** 2)                                      
                length = sumx / 16 * 255                                                     
                length = int(length)                                                   

                newimg.putpixel((x,y),(length, length, length))  
                bar.next()
        newimg.save('results/output/matrix/gaussian.jpg', 'JPEG')   
        bar.finish()


    def median(self):
        newimg = Image.new("RGB", (self.width, self.height), "white")   
        median = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]                                  
        bar = IncrementalBar('Median filter', 
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
                for i in range(3):                                                
                    for j in range(3): 
                        sumx += self.pixels[x + i - 1, y + j - 1][0] * median[i][j] 
                sumx = math.sqrt(sumx ** 2)                                      
                length = sumx / 9 * 255                                                     
                length = int(length)                                                   

                newimg.putpixel((x,y),(length, length, length))  
                bar.next()
        newimg.save('results/output/matrix/median.jpg', 'JPEG')   
        bar.finish()
