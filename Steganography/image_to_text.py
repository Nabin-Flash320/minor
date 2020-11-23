from PIL import Image
class ImageToText:

    def __init__(self,img):
        self.image = Image.open(img,'r')

    def decode(self):
        self.imd = iter(list(self.image.getdata()))
        self.data = ""
        while (True):
            pix = [value for value in self.imd.__next__()[:3]+
                                   self.imd.__next__()[:3]+
                                   self.imd.__next__()[:3]]

            self.bin_str ="" 
            for i in pix[:8]:
                if (i % 2 == 0):
                    self.bin_str +="0"
                else: 
                    self.bin_str +="1"
            self.data += chr(int(self.bin_str,2))
            if (pix[-1]% 2 != 0):
                return self.data

if __name__ == "__main__":
	img = input("input image to be embedded with ext : ")
	s = ImageToText(img)
	y = s.decode()
	print("decoded message is : " +y)
