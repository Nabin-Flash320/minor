
class TextCryptography:
    def __init__(self):
        #encryption and decryption key for capital alphabet
        self.keyCapital = 'LEMQGJFZUPOIHSYWCNRTXDABKV'
        #encryption and decryption key for small alphabet
        self.keySmall   = 'selyujdcqnhvfmiwbpztgkroxa'
        self.list = []
    #class fuction to encrypt the text message
    def encryptText(self, text):
        #convert srting into list
        self.list = list(text)
        for i in range(len(self.list)):
            if self.list[i].isalpha:
                #subtitute small alphabet from key
                if ord(self.list[i]) >= 97 and ord(self.list[i]) <= 122:
                    self.list[i] =  self.keySmall[ord(self.list[i])%97]
                #subtitute capital alphabet form key
                elif ord(self.list[i]) >= 65 and ord(self.list[i]) <= 90:
                    self.list[i] = self.keyCapital[ord(self.list[i])%65]     
            else:
                continue
        #convert list into string
        text = "".join(self.list)
        return text
    #class function to decrypt the text message
    def decryptText(self,text):
        #convert text string into list
        self.list = list(text)
        #obtain original text using key
        for i in range(len(self.list)):
            if self.list[i].isalpha:
                if ord(self.list[i]) >= 97 and ord(self.list[i]) <= 122:
                    self.list[i] = chr(self.keySmall.find(self.list[i])+97)
                elif ord(self.list[i]) >= 65 and ord(self.list[i]) <= 90:
                    self.list[i] = chr(self.keyCapital.find(self.list[i])+65)
        text = "".join(self.list)
        return text
