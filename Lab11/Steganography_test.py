import numpy as np
from scipy import misc
from pprint import pprint as pp
import zlib
import base64
import re
import binascii

def writeFile(filename, string):
    with open(filename, 'w') as myFile:
        myFile.writelines(string)

class Payload:
    def __init__(self, img=None, compressionLevel=-1, content=None):
        #input validation
        if img is None and content is None:
            raise ValueError("Both img and content not provided")
        elif compressionLevel > 9 or compressionLevel < -1:
            raise ValueError("compressionLevel must be between -1 and 9 inclusive")

        #member variable initialization
        self.img = np.zeros(shape=(0,0))
        self.content = np.zeros(shape=(0,0))


        #Img and compressionLevel provided
        if not img is None:
            if not type(img) is np.ndarray:
                raise TypeError("Error. img input not a ndarray")


            #initialize img
            print("image provided")
            self.img = img.astype(np.uint8)

            #rasterize img
            raster = self.rasterizevec(self.img)

            #compression stage
            compress = False
            comparray = raster
            if compressionLevel != -1:
                compress = True
                comparray = zlib.compress(raster, compressionLevel)

            #XML serialization
            xmlstr = self.XMLserial('Color', self.img.shape, compress, comparray)

            #base64 encoding
            encode = base64.b64encode(xmlstr.encode('utf-8'))

            #build content
            vbase64eval = np.vectorize(self.base64eval)
            self.content = vbase64eval(list(encode))

            #handle padding
            index = np.argwhere(self.content==-1)
            self.content = np.delete(self.content, index)

            self.content = self.content.astype(dtype=np.uint8)


        #content provided
        elif not content is None:
            if not type(content) is np.ndarray:
                raise TypeError("Error. Content not ndarray")

            print("Content Provided")
            self.content = content

            #base64 decoding
            vbase64dec = np.vectorize(self.base64dec)
            encode = vbase64dec(self.content)

            print(encode)

    def base64dec(self, val):

        #A-Z
        if val >= 0 and val <= 25:
            return chr(val+65)
        #a-z
        elif val >= 26 and val <= 51:
            return chr(val+71)
        #0-9
        elif val >= 52 and val <= 61:
            return chr(val-4)
        #+
        elif val == 62:
            return chr(43)
        #/
        elif val == 63:
            return chr(47)
        else:
            return False

    def base64eval(self, asci):

        #0-9
        if asci <= 57 and asci >= 48:
            return asci+4
        #A-Z
        elif asci >= 65 and asci <= 90:
            return asci-65
        #a-z
        elif asci >= 97 and asci <= 122:
            return asci-71
        #+
        elif asci == 43:
            return 62
        #/
        elif asci == 47:
            return 63
        #handle padding
        else:
            return -1

    def rasterizevec(self, image):

        red = image[:, :, 0].flatten()
        green = image[:, :, 1].flatten()
        blue = image[:, :, 2].flatten()

        return np.concatenate((red,green,blue))

    def XMLserial(self, type, size, compressed, comparr):
        sizestr = '{0},{1}'.format(size[0],size[1])
        compstr = 'False'
        if compressed:
            compstr = 'True'
        s = '<?xml version="1.0" encoding="UTF-8"?><payload type="{0}" size="{1}" compressed="{2}">'.format(type,sizestr,compstr)
        #s += str(list(comparr))[1:-1]
        s += ','.join(map(str, list(comparr))) #might be slowing down program
        #s += ','.join(np.char.mod('%d', list(comparr)))
        #test = np.char.mod('%d', comparr)

        s += '</payload>'

        return s



if __name__ == "__main__":
    carrier = misc.imread("data/carrier1.png")
    payload = misc.imread("data/payload1.png")

    test = [
            [[3,3,3], [4,5,6], [7,8,9]],
            [[35,98,123], [99,39,38], [12,12,203]],
            [[18,24,123], [230,19,3], [43,92,160]]
           ]
    test2 = [
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    ]
    test = np.array(test, dtype=np.uint8)
    p1 = Payload(img=payload, compressionLevel=9)
    p2 = Payload(content=p1.content)
