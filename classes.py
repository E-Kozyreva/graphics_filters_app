import math
import random
from progress.bar import ChargingBar
from PIL import Image


class Filters:
    def __init__(self, image):
        self.image = image
        self.pixels = image.load()
        self.width, self.height = image.size
        self.pixels = list(image.getdata())
        self.new_pixels = []
        self.newimg = Image.new("RGB", (self.width, self.height), "white")


class SpotFilters(Filters):
    def inversion(self):
        bar = ChargingBar('Inversion filter', max = 3, fill = '▰', suffix='%(percent)d%%')
        
        for pixel in self.pixels:
            self.new_pixels.append((255 - pixel[0], 255 - pixel[1], 255 - pixel[2]))

        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/inversion.jpg', 'JPEG')
        bar.next()
        bar.finish()

    
    def grayscale(self):
        bar = ChargingBar('Grayscale filter', max = 3, fill = '▰', suffix='%(percent)d%%')      
        
        for pixel in self.pixels:
            self.new_pixels.append((int((pixel[0] + pixel[1] + pixel[2]) / 3), 
                                    int((pixel[0] + pixel[1] + pixel[2]) / 3), 
                                    int((pixel[0] + pixel[1] + pixel[2]) / 3)))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/grayscale.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def blackwhite(self):
        bar = ChargingBar('Black and white filter', max = 3, fill = '▰', suffix='%(percent)d%%')          
  
        for pixel in self.pixels:
            if (pixel[0] + pixel[1] + pixel[2]) / 3 > 128:
                self.new_pixels.append((255, 255, 255))
            else:
                self.new_pixels.append((0, 0, 0))

        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/blackwhite.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def sepia(self):
        bar = ChargingBar('Sepia filter', max = 3, fill = '▰', suffix='%(percent)d%%')
        
        for pixel in self.pixels:
            self.new_pixels.append((int((pixel[0] * 0.393) + (pixel[1] * 0.769) + (pixel[2] * 0.189)),
                                    int((pixel[0] * 0.349) + (pixel[1] * 0.686) + (pixel[2] * 0.168)),
                                    int((pixel[0] * 0.272) + (pixel[1] * 0.534) + (pixel[2] * 0.131))))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/sepia.jpg', 'JPEG')
        bar.next()
        bar.finish()

    
    def brightness(self, value=2):
        bar = ChargingBar('Brightness filter', max = 3, fill = '▰', suffix='%(percent)d%%')

        for pixel in self.pixels:
            self.new_pixels.append((int(pixel[0] + value), 
                                    int(pixel[1] + value), 
                                    int(pixel[2] + value)))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/brightness.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def contrast(self, value=2):
        bar = ChargingBar('Contrast filter', max = 3, fill = '▰', suffix='%(percent)d%%')

        for pixel in self.pixels:
            self.new_pixels.append((int(pixel[0] * value), 
                                    int(pixel[1] * value), 
                                    int(pixel[2] * value)))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/contrast.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def gamma(self, value=2):
        bar = ChargingBar('Gamma filter', max = 3, fill = '▰', suffix='%(percent)d%%') 

        for pixel in self.pixels:
            self.new_pixels.append((int(pixel[0] ** value), 
                                    int(pixel[1] ** value), 
                                    int(pixel[2] ** value)))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/gamma.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def blur(self, value=2):
        bar = ChargingBar('Blur filter', max = 3, fill = '▰', suffix='%(percent)d%%')
        
        for pixel in self.pixels:
            self.new_pixels.append((int(pixel[0] / value), 
                                    int(pixel[1] / value), 
                                    int(pixel[2] / value)))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/blur.jpg', 'JPEG')
        bar.next()
        bar.finish()    


    def green(self):
        bar = ChargingBar('Green filter', max = 3, fill = '▰', suffix='%(percent)d%%')
        
        for pixel in self.pixels:
            self.new_pixels.append((0, pixel[1], 0))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/green.jpg', 'JPEG')
        bar.next()
        bar.finish()

    
    def red(self):
        bar = ChargingBar('Red filter', max = 3, fill = '▰', suffix='%(percent)d%%')  

        for pixel in self.pixels:
            self.new_pixels.append((pixel[0], 0, 0))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/red.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def blue(self):
        bar = ChargingBar('Blue filter', max = 3, fill = '▰', suffix='%(percent)d%%')   
        
        for pixel in self.pixels:
            self.new_pixels.append((0, 0, pixel[2]))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('results/output/spot/blue.jpg', 'JPEG')
        bar.next()
        bar.finish()


class MatrixFilters(Filters):
    def sobel(self):
        bar = ChargingBar('Sobel filter', max = 2, fill = '▰', suffix='%(percent)d%%') 

        sobelx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]                                  
        sobely = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]                             

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
                                                
                length = (sumx + sumy) / 2164 * 255                                                     
                length = int(length)                                                   

                self.newimg.putpixel((x, y), (length, length, length))  

        bar.next()
        self.newimg.save('results/output/matrix/sobel.jpg', 'JPEG')  
        bar.next() 
        bar.finish()


    def sharpen(self):
        bar = ChargingBar('Sharpen filter', max = 2, fill = '▰', suffix='%(percent)d%%')        

        sharpen = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]   

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

                self.newimg.putpixel((x, y), (new_r, new_g, new_b))     
                
        bar.next()
        self.newimg.save('results/output/matrix/sharpen.jpg', 'JPEG')   
        bar.next()
        bar.finish()


    def operator_scharra(self):
        bar = ChargingBar('Scharra filter', max = 2, fill = '▰', suffix='%(percent)d%%')        

        operator_x = [[3, 0, -3], [10, 0, -10], [3, 0, -3]]
        operator_y = [[3, 10, 3], [0, 0, 0], [-3, -10, -3]]

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

                length = (sum_x + sum_y) / 4328 * 255
                length = int(length)

                self.newimg.putpixel((x, y), (length, length, length))
                
        bar.next()
        self.newimg.save('results/output/matrix/operator_scharra.jpg', 'JPEG')
        bar.next()
        bar.finish()

    
    def operator_pruitt(self):
        bar = ChargingBar('Pruitt filter', max = 2, fill = '▰', suffix='%(percent)d%%')

        operator_x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
        operator_y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
        
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

                length = (sum_x + sum_y) / 4328 * 255
                length = int(length)

                self.newimg.putpixel((x, y), (length, length, length))
                
        bar.next()
        self.newimg.save('results/output/matrix/operator_pruitt.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def waves_1(self):
        bar = ChargingBar('Waves filter', max = 2, fill = '▰', suffix='%(percent)d%%')        
        
        for x in range(self.width):
            for y in range(self.height):
                new_x = x
                new_y = y + 20 * math.sin(2 * math.pi * x / 128)
                if new_y < 0:
                    new_y = 0
                if new_y > self.height - 1:
                    new_y = self.height - 1
                self.newimg.putpixel((x, y), self.image.getpixel((new_x, new_y)))
                
        bar.next()
        self.newimg.save('results/output/matrix/waves_1.jpg', 'JPEG')
        bar.next()
        bar.finish()
    

    def waves_2(self):
        bar = ChargingBar('Waves filter', max = 2, fill = '▰', suffix='%(percent)d%%')        
        
        for x in range(self.width):
            for y in range(self.height):
                new_x = x + 20 * math.sin(2 * math.pi * y / 128)
                new_y = y
                if new_x < 0:
                    new_x = 0
                if new_x > self.width - 1:
                    new_x = self.width - 1
                self.newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y))))
                
        bar.next()
        self.newimg.save('results/output/matrix/waves_2.jpg', 'JPEG')
        bar.next()
        bar.finish()

    
    def mirror(self):
        bar = ChargingBar('Mirror filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
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

                self.newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y)))) 
                
        bar.next()
        self.newimg.save('results/output/matrix/mirror.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def motion_blur(self):
        bar = ChargingBar('Motion blur filter', max = 2, fill = '▰', suffix='%(percent)d%%')        

        kernel_size = 10
        kernel = []

        for i in range(kernel_size):
            kernel.append(1 / kernel_size)

        for x in range(self.width):
            for y in range(self.height):
                r, g, b = 0, 0, 0

                for i in range(kernel_size):
                    pixel = self.image.getpixel((x, (y - i) % self.height))
                    r += pixel[0] * kernel[i]
                    g += pixel[1] * kernel[i]
                    b += pixel[2] * kernel[i]
                self.newimg.putpixel((x, y), (int(r), int(g), int(b)))

        bar.next()
        self.newimg.save('results/output/matrix/motion_blur.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def shift(self):
        bar = ChargingBar('Shift filter', max = 2, fill = '▰', suffix='%(percent)d%%')        

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
                self.newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y))))
                
        bar.next()
        self.newimg.save('results/output/matrix/shift.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def rotate(self):
        bar = ChargingBar('Rotate filter', max = 2, fill = '▰', suffix='%(percent)d%%')        
        
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

                self.newimg.putpixel((x, y), self.image.getpixel((int(new_x), int(new_y))))
                
        bar.next()
        self.newimg.save('results/output/matrix/rotate.jpg', 'JPEG')
        bar.next()
        bar.finish()