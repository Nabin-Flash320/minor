from PIL import Image

class ImageCryptography:
    def __init__(self,image):
        self.image = Image.open(image)
        self.COLUMN_KEY = '2143'#key for changing column
        self.ROW_KEY = '4312'#key for changing row
        self.IMAGE_KEY = ('193','239')#key for XOR of the pixels
        self.templ = [i for i in range(16)]
        self.temp_im = []
        self.new_im = Image.new("RGB",(4*int(self.image.size[0]/4),4*int(self.image.size[1]/4)),(255,255,255))

    def sliceImage(self):
        im_width = int(self.image.size[0]/4)        #croped image width
        im_height = int(self.image.size[1]/4)       #croped image height
        left, top, right, bottom = 0, 0, im_width, im_height  #slicing area
        #image is sliced into 16 equal pieces using Image.crop() function
        for i in range(16):
            self.temp_im.append(self.image.crop((left, top, right, bottom)))
            if i%4 == 3:
                left, top, right, bottom = 0, top+im_height, im_width, bottom+im_height
            else:
                left, right = left+im_width, right+im_width

    def pasteImage(self):
        im_width = int(self.image.size[0]/4)         #croped image width
        im_height = int(self.image.size[1]/4)        #croped image height
        left, top, right, bottom = 0, 0, im_width, im_height    #slicing area
        #paste sliced image into new image
        for i in range(16):
            Image.Image.paste(self.new_im,self.temp_im[i],(left, top, right, bottom))
            if i%4 == 3:
                left, top, right, bottom = 0, top+im_height, im_width, bottom+im_height
            else:
                left, right = left+im_width, right+im_width
    #Rotate pixel bitwise to left by 4 bits
    def rotate(self,rgb):
        r, b, g = rgb
        list_r, list_g, list_b = list('{0:08b}'.format(r)), list('{0:08b}'.format(g)), list('{0:08b}'.format(b))
        for i in range(4):#loop for rotation
            temp_r, temp_g, temp_b = list_r[i], list_g[i], list_b[i]
            list_r[i], list_g[i], list_b[i] = list_r[i+4], list_g[i+4], list_b[i+4]
            list_r[i+4], list_g[i+4], list_b[i+4] = temp_r, temp_g, temp_b
        return(int("".join(list_r),2), int("".join(list_g),2), int("".join(list_b),2))
    #Encrypt the image           
    def encryptImage(self):
        self.sliceImage()
        #change position of columns
        for i in range(len(self.temp_im)):
            if (int(self.COLUMN_KEY[i%4])-1) < (i%4):
                key = i - ((i%4)-(int(self.COLUMN_KEY[i%4])-1))
            elif (int(self.COLUMN_KEY[i%4])-1) > (i%4):
                key = i + ((int(self.COLUMN_KEY[i%4])-1)-(i%4))
            self.templ[i] = self.temp_im[key]
        #change position of rows
        for i in range(len(self.templ)):
            key = ((int(self.ROW_KEY[int(i/4)])-1)*4) + (i%4)
            self.temp_im[i] = self.templ[key]
        self.pasteImage()
        pixels = self.new_im.load()
        # Rotate and XOR RGB value of image
        for i in range(self.new_im.size[0]):
            for j in range(self.new_im.size[1]):
                r, g, b = self.rotate(self.new_im.getpixel((i,j)))
                if (i + j) % 2 == 0:
                    pixels[i,j] = (r ^ int(self.IMAGE_KEY[0]), g ^ int(self.IMAGE_KEY[0]), b ^ int(self.IMAGE_KEY[0]))
                else:
                    pixels[i,j] = (r ^ int(self.IMAGE_KEY[1]), g ^ int(self.IMAGE_KEY[1]), b ^ int(self.IMAGE_KEY[1]))

        self.temp_im = []
        self.new_im.show()
        self.new_im.save('ehand.png', "PNG")
   #Decrypt the image
    def decryptImage(self):
        pixels = self.image.load()
        #XOR and roate RGB value of the image
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                r, g, b = self.image.getpixel((i,j))
                if (i + j) % 2 == 0:
                    pixels[i,j] = (r ^ int(self.IMAGE_KEY[0]), g ^ int(self.IMAGE_KEY[0]), b ^ int(self.IMAGE_KEY[0]))
                else:
                    pixels[i,j] = (r ^ int(self.IMAGE_KEY[1]), g ^ int(self.IMAGE_KEY[1]), b ^ int(self.IMAGE_KEY[1]))
                pixels[i,j] = tuple(self.rotate(self.image.getpixel((i,j))))
        self.sliceImage()
        #change position of columns to original position
        for i in range(len(self.temp_im)):
            key = (int(self.COLUMN_KEY[i%4])-1)+(4*int(i/4))
            self.templ[key] = self.temp_im[i]
        #change position of rows to original position
        for i in range(len(self.templ)):
            key = ((int(self.ROW_KEY[int(i/4)])-1)*4)+int(i%4)
            self.temp_im[key] = self.templ[i]
        self.pasteImage()
        self.new_im.show()
