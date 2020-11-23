from PIL import Image
class textToImage:
    def text_to_image(self,message,image):
        self.message = message
        if (len(self.message)== 0):
            raise ValueError("message is empty")
            exit
        self.image_path = str(image).split(":")[-1]
        self.image_path = self.image_path[:-2]
        self.image = Image.open(self.image_path,'r')
        self.newimage = self.image.copy()

        self.npix = list(self.newimage.getdata())

        self.encodeec()
        # newimage_name = input("enter new image name with .extension  :")
        newimage_name = "encoded.png"
        self.newimage = self.newimage.save(newimage_name,str(newimage_name.split(".")[1].upper()))
        print("embedded successfully......")

    def te2bin(self):
       self.newd = []
       for i in self.message:
         self.newd.append(format(ord(i),'08b'))
       return self.newd

   #receives message and image pixel values
    def modpixel(self):
       
        imd= iter(self.npix)
        datalist= self.te2bin()

        for i in range(len(datalist)):
            pix = [value for value in imd.__next__()[:3]+
                                      imd.__next__()[:3]+
                                      imd.__next__()[:3]]
            
            for j in range(0,8):
                if (datalist[i][j]=="0" and pix[j]%2 !=0):     
                        pix[j] -=1
                  
                elif (datalist[i][j]=="1" and pix[j]%2 ==0):
                    if (pix[j] != 0):
                        pix[j] -= 1
                    else :
                        pix[j] += 1

            if (i ==len(datalist) - 1):
                if (pix[-1] % 2 )== 0:
                    if pix[-1] != 0:
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1

            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
      
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    

    def encodeec(self):
        width = self.newimage.size[0]
        (x,y) = (0,0)
    
   
        for pixels in self.modpixel():
            self.newimage.putpixel((x,y),pixels)
            if (x == width-1):
                  x = 0
                  y +=1
            else:
                  x +=1

if __name__ == "__main__":
	message = input("enter message to be encoded :")
	picture = input("input picture name with extension to embed text :")
	texttoimage = textToImage()
	texttoimage.text_to_image(message,picture)


    
