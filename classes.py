import math
import random
from progress.bar import ChargingBar
from PIL import Image, ImageChops
import numpy as np


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
            self.new_pixels.append((255 - pixel[0], 
                                    255 - pixel[1], 
                                    255 - pixel[2]))

        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('Results/Spot_filters/Inversion.jpg', 'JPEG')
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
        self.newimg.save('Results/Spot_filters/Grayscale.jpg', 'JPEG')
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
        self.newimg.save('Results/Spot_filters/Black_white.jpg', 'JPEG')
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
        self.newimg.save('Results/Spot_filters/Sepia.jpg', 'JPEG')
        bar.next()
        bar.finish()

    
    def brightness(self, value=50):
        bar = ChargingBar('Brightness filter', max = 3, fill = '▰', suffix='%(percent)d%%')

        for pixel in self.pixels:
            self.new_pixels.append((int(pixel[0] + value), 
                                    int(pixel[1] + value), 
                                    int(pixel[2] + value)))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('Results/Spot_filters/Brightness.jpg', 'JPEG')
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
        self.newimg.save('Results/Spot_filters/Contrast.jpg', 'JPEG')
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
        self.newimg.save('Results/Spot_filters/Gamma.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def blackout(self, value=5):
        bar = ChargingBar('Blackout filter', max = 3, fill = '▰', suffix='%(percent)d%%')
        
        for pixel in self.pixels:
            self.new_pixels.append((int(pixel[0] / value), 
                                    int(pixel[1] / value), 
                                    int(pixel[2] / value)))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('Results/Spot_filters/Blackout.jpg', 'JPEG')
        bar.next()
        bar.finish()    


    def green(self):
        bar = ChargingBar('Green filter', max = 3, fill = '▰', suffix='%(percent)d%%')
        
        for pixel in self.pixels:
            self.new_pixels.append((0, pixel[1], 0))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('Results/Spot_filters/Green.jpg', 'JPEG')
        bar.next()
        bar.finish()

    
    def red(self):
        bar = ChargingBar('Red filter', max = 3, fill = '▰', suffix='%(percent)d%%')  

        for pixel in self.pixels:
            self.new_pixels.append((pixel[0], 0, 0))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('Results/Spot_filters/Red.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def blue(self):
        bar = ChargingBar('Blue filter', max = 3, fill = '▰', suffix='%(percent)d%%')   
        
        for pixel in self.pixels:
            self.new_pixels.append((0, 0, pixel[2]))
            
        bar.next()
        self.newimg.putdata(self.new_pixels)
        bar.next()
        self.newimg.save('Results/Spot_filters/Blue.jpg', 'JPEG')
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
        self.newimg.save('Results/Matrix_filters/Sobel.jpg', 'JPEG')  
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
        self.newimg.save('Results/Matrix_filters/Sharpen.jpg', 'JPEG')   
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
        self.newimg.save('Results/Matrix_filters/Operator_scharra.jpg', 'JPEG')
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
        self.newimg.save('Results/Matrix_filters/Operator_pruitt.jpg', 'JPEG')
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
        self.newimg.save('Results/Matrix_filters/Waves_1.jpg', 'JPEG')
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
        self.newimg.save('Results/Matrix_filters/Waves_2.jpg', 'JPEG')
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
        self.newimg.save('Results/Matrix_filters/Motion_blur.jpg', 'JPEG')
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
        self.newimg.save('Results/Matrix_filters/Shift.jpg', 'JPEG')
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
        self.newimg.save('Results/Matrix_filters/Rotate.jpg', 'JPEG')
        bar.next()
        bar.finish()


    def guassian(self):
        bar = ChargingBar('Gaussian filter', max = 2, fill = '▰', suffix='%(percent)d%%')        

        size = 2 * 3 + 1
        sigma = 1
        kernel = []

        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            kernel.append(row)

        for i in range(size):
            for j in range(size):
                kernel[i][j] = math.exp(-((i - size // 2) ** 2 + (j - size // 2) ** 2) / (2 * sigma ** 2)) / (2 * math.pi * sigma ** 2)
        

        for x in range(self.width):
            for y in range(self.height):
                r, g, b = 0, 0, 0

                for i in range(size):
                    for j in range(size):
                        if x + i < 0 or x + i > self.width - 1 or y + j < 0 or y + j > self.height - 1:
                            continue
                        pixel = self.image.getpixel((x + i, y + j))
                        r += pixel[0] * kernel[i][j]
                        g += pixel[1] * kernel[i][j]
                        b += pixel[2] * kernel[i][j]
                self.newimg.putpixel((x, y), (int(r), int(g), int(b)))

        bar.next()
        self.newimg.save('Results/Matrix_filters/Gaussian.jpg', 'JPEG')
        bar.next()
        bar.finish()

class MathMorph(Filters):
    def dilate(self):
        bar = ChargingBar('Dilate filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                result_r = 0
                result_g = 0
                result_b = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x + i < 0 or x + i > self.width - 1 or y + j < 0 or y + j > self.height - 1:
                            continue
                        pixel = self.image.getpixel((x + i, y + j))
                        if pixel[0] > result_r:
                            result_r = pixel[0]
                        if pixel[1] > result_g:
                            result_g = pixel[1]
                        if pixel[2] > result_b:
                            result_b = pixel[2]
                self.newimg.putpixel((x, y), (result_r, result_g, result_b))
                
        bar.next()
        self.newimg.save('Results/Math_morph_filters/Dilate.jpg', 'JPEG')
        bar.next()
        bar.finish()
        
        
    def erode(self):
        bar = ChargingBar('Erode filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                result_r = 255
                result_g = 255
                result_b = 255
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x + i < 0 or x + i > self.width - 1 or y + j < 0 or y + j > self.height - 1:
                            continue
                        pixel = self.image.getpixel((x + i, y + j))
                        if pixel[0] < result_r:
                            result_r = pixel[0]
                        if pixel[1] < result_g:
                            result_g = pixel[1]
                        if pixel[2] < result_b:
                            result_b = pixel[2]
                self.newimg.putpixel((x, y), (result_r, result_g, result_b))
                
        bar.next()
        self.newimg.save('Results/Math_morph_filters/Erode.jpg', 'JPEG')
        bar.next()
        bar.finish()
        
    
    def opened(self):
        bar = ChargingBar('Opened filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        self.erode()
        bar.next()
        self.dilate()
        bar.next()
        self.newimg.save('Results/Math_morph_filters/Opened.jpg', 'JPEG')
        bar.finish()
        
    
    def closed(self):
        bar = ChargingBar('Closed filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        self.dilate()
        bar.next()
        self.erode()
        bar.next()
        self.newimg.save('Results/Math_morph_filters/Closed.jpg', 'JPEG')
        bar.finish()
        

    def top_hat(self):
        bar = ChargingBar('Top hat filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        self.erode()
        bar.next()
        for x in range(self.width):
            for y in range(self.height):
                r = self.image.getpixel((x, y))[0] - self.newimg.getpixel((x, y))[0]
                g = self.image.getpixel((x, y))[1] - self.newimg.getpixel((x, y))[1]
                b = self.image.getpixel((x, y))[2] - self.newimg.getpixel((x, y))[2]
                self.newimg.putpixel((x, y), (r, g, b))
        bar.next()
        self.newimg.save('Results/Math_morph_filters/Top_hat.jpg', 'JPEG')
        bar.finish()
        

    def black_hat(self):    
        bar = ChargingBar('Black hat filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        self.dilate()
        bar.next()
        for x in range(self.width):
            for y in range(self.height):
                r = self.newimg.getpixel((x, y))[0] - self.image.getpixel((x, y))[0]
                g = self.newimg.getpixel((x, y))[1] - self.image.getpixel((x, y))[1]
                b = self.newimg.getpixel((x, y))[2] - self.image.getpixel((x, y))[2]
                self.newimg.putpixel((x, y), (r, g, b))
        bar.next()
        self.newimg.save('Results/Math_morph_filters/Black_hat.jpg', 'JPEG')
        bar.finish()
        
    
    def grad(self):
        bar = ChargingBar('Grad filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        self.closed()
        bar.next()
        
        for x in range(self.width):
            for y in range(self.height):
                r = self.image.getpixel((x, y))[0] - self.newimg.getpixel((x, y))[0]
                g = self.image.getpixel((x, y))[1] - self.newimg.getpixel((x, y))[1]
                b = self.image.getpixel((x, y))[2] - self.newimg.getpixel((x, y))[2]
                self.newimg.putpixel((x, y), (r, g, b))
                
        bar.next()
        self.newimg.save('Results/Math_morph_filters/Grad.jpg', 'JPEG')
        bar.finish()
        
    
class Other(Filters):
    def gray_world(self):
        bar = ChargingBar('Gray world filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        avg_r = 0
        avg_g = 0
        avg_b = 0
        for x in range(self.width):
            for y in range(self.height):
                avg_r += self.image.getpixel((x, y))[0]
                avg_g += self.image.getpixel((x, y))[1]
                avg_b += self.image.getpixel((x, y))[2]
        avg_r /= self.width * self.height
        avg_g /= self.width * self.height
        avg_b /= self.width * self.height
        avg = (avg_r + avg_g + avg_b) / 3
        for x in range(self.width):
            for y in range(self.height):
                r = self.image.getpixel((x, y))[0] * avg / avg_r
                g = self.image.getpixel((x, y))[1] * avg / avg_g
                b = self.image.getpixel((x, y))[2] * avg / avg_b
                self.newimg.putpixel((x, y), (int(r), int(g), int(b)))
        bar.next()
        self.newimg.save('Results/Other_filters/Gray_world.jpg', 'JPEG')
        bar.next()
        bar.finish()
        
        
    def glass(self):
        bar = ChargingBar('Glass filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        for x in range(self.width):
            for y in range(self.height):
                res_x = (int)(x + (random.random() - 0.5) * 10)
                res_y = (int)(y + (random.random() - 0.5) * 10)
                
                res_x = np.clip(res_x, 0, self.width - 1)
                res_y = np.clip(res_y, 0, self.height - 1)
                
                self.newimg.putpixel((x, y), self.image.getpixel((res_x, res_y)))
        bar.next()
        self.newimg.save('Results/Other_filters/Glass.jpg', 'JPEG')
        bar.next()
        bar.finish()
        
    
    def histogram_linear_stretch(self):
        bar = ChargingBar('Histogram linear stretch filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        r_min = 255
        g_min = 255
        b_min = 255
        r_max = 0
        g_max = 0
        b_max = 0
        for x in range(self.width):
            for y in range(self.height):
                r_min = min(r_min, self.image.getpixel((x, y))[0])
                g_min = min(g_min, self.image.getpixel((x, y))[1])
                b_min = min(b_min, self.image.getpixel((x, y))[2])
                r_max = max(r_max, self.image.getpixel((x, y))[0])
                g_max = max(g_max, self.image.getpixel((x, y))[1])
                b_max = max(b_max, self.image.getpixel((x, y))[2])
        for x in range(self.width):
            for y in range(self.height):
                r = (self.image.getpixel((x, y))[0] - r_min)/ (r_max - r_min) * 255 
                g = (self.image.getpixel((x, y))[1] - g_min) / (g_max - g_min) * 255 
                b = (self.image.getpixel((x, y))[2] - b_min) / (b_max - b_min) * 255 
                self.newimg.putpixel((x, y), (int(r), int(g), int(b)))
        bar.next()
        self.newimg.save('Results/Other_filters/Histogram_linear_stretch.jpg', 'JPEG')
        bar.next()
        bar.finish()
        
        
    def correction_with_reference_color(self):
        bar = ChargingBar('Correction with reference color filter', max = 2, fill = '▰', suffix='%(percent)d%%')
        
        r_ref = 0
        g_ref = 0
        b_ref = 0
        for x in range(self.width):
            for y in range(self.height):
                r_ref += self.image.getpixel((x, y))[0]
                g_ref += self.image.getpixel((x, y))[1]
                b_ref += self.image.getpixel((x, y))[2]
        r_ref /= self.width * self.height
        g_ref /= self.width * self.height
        b_ref /= self.width * self.height
        for x in range(self.width):
            for y in range(self.height):
                r = self.image.getpixel((x, y))[0] * r_ref / 255
                g = self.image.getpixel((x, y))[1] * g_ref / 255
                b = self.image.getpixel((x, y))[2] * b_ref / 255
                self.newimg.putpixel((x, y), (int(r), int(g), int(b)))
        bar.next()
        self.newimg.save('Results/Other_filters/Correction_with_reference_color.jpg', 'JPEG')
        bar.next()
        bar.finish()
        
    
    def median(self):
        pass
    
    
    def glowing_edges(self):
        pass
