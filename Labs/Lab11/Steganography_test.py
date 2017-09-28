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

        #rasterize
        raster = self.rasterizevec(self.img)

        # compression stage
        compress = False
        comparray = raster
        if compressionLevel != -1:
            compress = True
            comparray = zlib.compress(raster, compressionLevel)

        test = list(comparray)
        test = np.char.mod('%d', test)
        #print(list(test))

        xmlstr = self.XMLserial('Color', self.img.shape, compress, comparray)
        writeFile('tempFiles/payload.xml', xmlstr)

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
        #s += ','.join(map(str, list(comparr))) #might be slowing down program
        s += ','.join(np.char.mod('%d', list(comparr)))
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
    #p2 = Payload(content=p1.content)
