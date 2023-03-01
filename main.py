import os
import colorsys
import math
from PIL import Image


class Filters:
    class SpotFilters:
        def __init__(self, image):
            self.image = image
            self.pixels = image.load()
            self.width, self.height = image.size
            self.pixels = list(image.getdata())

        
        def inversion(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            pixels = [(255 - pixel[0], 255 - pixel[1], 255 - pixel[2]) for pixel in self.pixels] 
            newimg.putdata(pixels)                                                             
            newimg.save('results/spot_filters/inversion.jpg', 'JPEG')
            print("Inversion filter applied")


        def grayscale(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            pixels = [(int((pixel[0] + pixel[1] + pixel[2]) / 3), 
                       int((pixel[0] + pixel[1] + pixel[2]) / 3), 
                       int((pixel[0] + pixel[1] + pixel[2]) / 3)) for pixel in self.pixels] 
            newimg.putdata(pixels)                                                             
            newimg.save('results/spot_filters/grayscale.jpg', 'JPEG')
            print("Grayscale filter applied")


        def blackwhite(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            def blackwhite(pixel):  
                if (pixel[0] + pixel[1] + pixel[2]) / 3 > 128:
                    return 255
                else:
                    return 0
                

            pixels = [(blackwhite(pixel), blackwhite(pixel), blackwhite(pixel)) for pixel in self.pixels]
            newimg.putdata(pixels)                                                             
            newimg.save('results/spot_filters/blackwhite.jpg', 'JPEG')
            print("Black and white filter applied")


        def sepia(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            pixels = [(int(pixel[0] * 0.393 + pixel[1] * 0.769 + pixel[2] * 0.189), 
                       int(pixel[0] * 0.349 + pixel[1] * 0.686 + pixel[2] * 0.168), 
                       int(pixel[0] * 0.272 + pixel[1] * 0.534 + pixel[2] * 0.131)) for pixel in self.pixels]
            newimg.putdata(pixels)                                                             
            newimg.save('results/spot_filters/sepia.jpg', 'JPEG')
            print("Sepia filter applied")


        def brightness(self, value):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            pixels = [(pixel[0] + value, pixel[1] + value, pixel[2] + value) for pixel in self.pixels] 
            newimg.putdata(pixels)                                                             
            newimg.save('results/spot_filters/brightness.jpg', 'JPEG')
            print("Brightness filter applied")


    class MatrixFilters:
        def __init__(self, image):
            self.image = image
            self.pixels = image.load()
            self.width, self.height = image.size
            self.pixels = list(image.getdata())

        
        def sobel(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            sobelx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]                                  
            sobely = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]                             

            for x in range(1, self.width - 1):                                           
                for y in range(1, self.height - 1):                                      
                    sumx = 0                                                           
                    sumy = 0                                                  
                    for i in range(3):                                                
                        for j in range(3):                                 
                            sumx += img.getpixel((x + i - 1, y + j - 1))[0] * sobelx[i][j] 
                            sumy += img.getpixel((x + i - 1, y + j - 1))[0] * sobely[i][j] 
                    sumx = math.sqrt(sumx ** 2)                                      
                    sumy = math.sqrt(sumy ** 2)                                         

                    length = sumx + sumy                                                  
                    length = length / 2164 * 255                                                     
                    length = int(length)                                                   

                    newimg.putpixel((x,y),(length, length, length))                                                                            
            newimg.save('results/matrix_filters/sobel.jpg', 'JPEG')
            print("Sobel filter applied")


        def sharpen(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            sharp = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]

            for x in range(1, self.width - 1):                        
                for y in range(1, self.height - 1):                
                    new_r, new_g, new_b = 0, 0, 0 
                    for a in range(3):                         
                        for b in range(3):
                            p = img.getpixel((x + a - 1, y + b - 1)) 
                            r_channel, g_channel, b_channel = p[0], p[1], p[2]       
                            new_r += r_channel * sharp[a][b]                 
                            new_g += g_channel * sharp[a][b]                
                            new_b += b_channel * sharp[a][b]

                    newimg.putpixel((x, y),(new_r, new_g, new_b))                                                                          
            newimg.save('results/matrix_filters/sharpen.jpg', 'JPEG')
            print("Sharpen filter applied")

        
        def blur(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            blur = [[-1, -1, 1], [-1, 9, -1], [-1, -1, -1]]

            for x in range(1, self.width - 1):                        
                for y in range(1, self.height - 1):                
                    new_r, new_g, new_b = 0, 0, 0 
                    for a in range(3):                         
                        for b in range(3):
                            p = img.getpixel((x + a - 1, y + b - 1)) 
                            r_channel, g_channel, b_channel = p[0], p[1], p[2]       
                            new_r += r_channel * blur[a][b]                 
                            new_g += g_channel * blur[a][b]                
                            new_b += b_channel * blur[a][b]

                    newimg.putpixel((x, y),(new_r, new_g, new_b))                                                                          
            newimg.save('results/matrix_filters/blur.jpg', 'JPEG')
            print("Blur filter applied")

        
        def emboss(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            emboss = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]

            for x in range(1, self.width - 1):                        
                for y in range(1, self.height - 1):                
                    new_r, new_g, new_b = 0, 0, 0 
                    for a in range(3):                         
                        for b in range(3):
                            p = img.getpixel((x + a - 1, y + b - 1)) 
                            r_channel, g_channel, b_channel = p[0], p[1], p[2]       
                            new_r += r_channel * emboss[a][b]                 
                            new_g += g_channel * emboss[a][b]                
                            new_b += b_channel * emboss[a][b]

                    newimg.putpixel((x, y),(new_r, new_g, new_b))                                                                          
            newimg.save('results/matrix_filters/emboss.jpg', 'JPEG')
            print("Emboss filter applied")


        def reflection(self):
            newimg = Image.new("RGB", (self.width, self.height), "white")   
            pixels = [(pixel[0], pixel[1], pixel[2]) for pixel in self.pixels] 
            for x in range(self.width):
                for y in range(self.height):
                    newimg.putpixel((x, y), pixels[(y * self.width + (self.width - x - 1))])
            newimg.save('results/matrix_filters/reflection.jpg', 'JPEG')
            print("Reflection filter applied")



if __name__ == '__main__':
    img = Image.open('cat.jpg')
    spot = Filters.SpotFilters(img)
    spot.inversion()
    spot.grayscale()
    spot.blackwhite()
    spot.sepia()
    spot.brightness(100)
    print()
    matrix = Filters.MatrixFilters(img)
    matrix.sobel()
    matrix.sharpen()
    matrix.blur()
    matrix.emboss()
    matrix.reflection()
