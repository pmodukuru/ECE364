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
            #encode = base64.b64encode(bytes(xmlstr,'utf8')) #either work
            encode = base64.b64encode(xmlstr.encode('utf-8'))


            #build content
            #print(binascii.b2a_base64(encode))
            #writeFile('tempFiles/binasci.txt', str(binascii.b2a_base64(encode)))

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

            #add padding
            padding = (len(encode)*3)%4
            encode = bytes(encode) + b'='*padding

            #recover xmlstring
            xmlstr = base64.b64decode(encode)

            #recover compressed img and metadata
            match = re.search(r'type="(.+)"\s*size="([\d,]+)"\s*compressed="(True|False)">([\d,\s]+)<', str(xmlstr))
            typeimg = match.group(1)
            size = match.group(2)
            compress = match.group(3)
            compimg = bytes(map(int, match.group(4).split(','))) #slowing down program

            #invert raster and rebuild image

            if compress == 'True':
                raster = np.array((list(zlib.decompress(compimg))))
            else:
                raster = np.array(list(compimg))

            #split rasterized image back into distinct channels
            total = np.split(raster, 3)
            red = total[0] #red
            blue = total[1] #green
            green = total[2] #blue

            #testing no for loop
            #print("Non looping version")
            #image = np.dstack([red, blue, green])
            #print(image)
            #
            # print(image.shape)

            image = np.zeros((int(size.split(',')[0]), int(size.split(',')[1]), 3))

            #rebuild 3D numpy array holding image values
            pcnt = 0
            for row in image:
                for pixel in row:
                    pixel[0] = red[pcnt]
                    pixel[1] = blue[pcnt]
                    pixel[2] = green[pcnt]
                    pcnt += 1

            self.img = image.astype(dtype=np.uint8)
            #print("\nLooping version")
            #print(self.img)
            #print(self.img.shape)
            #misc.imsave('outfile.png', self.img)

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

    def XMLserial(self, type, size, compressed, comparr):
        sizestr = '{0},{1}'.format(size[0],size[1])
        compstr = 'False'
        if compressed:
            compstr = 'True'
        s = '<?xml version="1.0" encoding="UTF-8"?><payload type="{0}" size="{1}" compressed="{2}">'.format(type,sizestr,compstr)
        #s += str(list(comparr))[1:-1]
        s += ','.join(map(str, list(comparr))) #might be slowing down program
        s += '</payload>'

        return s

    def XMLserial_test(self, type, size, compressed, comparr):
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


    def rasterizevec(self, image):

        red = image[:, :, 0].flatten()
        green = image[:, :, 1].flatten()
        blue = image[:, :, 2].flatten()

        return np.concatenate((red,green,blue))


class Carrier:
    def __init__(self, img):
        if not type(img) is np.ndarray:
            raise TypeError("Error. Content type not ndarray")
        self.img = img

    def clean(self):
        print("cleaning")
        img_copy = np.copy(self.img)
        rand = (np.random.randint(0, 2, dtype=np.uint8))
        '''if rand == 0:
            img_copy = img_copy & ~rand
        elif rand == 1:
            img_copy = img_copy & ~rand
        else:
            img_copy = img_copy & ~rand'''

        ri = 0
        pi = 0
        for ri, row in enumerate(self.img):
            for pi, pixel in enumerate(row):
                rand = (np.random.randint(0, 2, dtype=np.uint8))
                img_copy[ri][pi][0] = pixel[0] & ~rand
                rand = (np.random.randint(0, 2, dtype=np.uint8))
                img_copy[ri][pi][1] = pixel[1] & ~rand
                rand = (np.random.randint(0, 2, dtype=np.uint8))
                img_copy[ri][pi][2] = pixel[2] & ~rand

        '''for ri, row in enumerate(self.img):
            for pi, pixel in enumerate(row):
                rand = (np.random.randint(0, 2, dtype=np.uint8))
                red = np.unpackbits(pixel[0])
                red[6:7] = np.unpackbits(rand)[6:7]
                img_copy[ri][pi][0] = np.packbits(red)


                rand = (np.random.randint(0, 2, dtype=np.uint8))
                green = np.unpackbits(pixel[1])
                green[6:7] = np.unpackbits(rand)[6:7]
                img_copy[ri][pi][1] = np.packbits(green)


                rand = (np.random.randint(0, 2, dtype=np.uint8))
                blue = np.unpackbits(pixel[2])
                blue[6:7] = np.unpackbits(rand)[6:7]
                img_copy[ri][pi] = np.packbits(blue)'''


        return img_copy


    def embedPayload(self, payload, override=False):
        if not type(payload) is Payload:
            raise TypeError("Error. Payload not ndarray")
        if len(payload.content) > 3 * len(self.img.flatten()):
            raise ValueError("Error. Payload too large for carrier")
        if override == False:
            if self.payloadExists():
                raise Exception("Carrier already contains payload")

        print("Embedding")
        print(len(payload.content))
        flatimg = np.copy(self.img)
        flatimg.shape = (self.img.shape[0]*self.img.shape[1], 3)
        #print(flatimg)
        #print(flatimg.reshape(self.img.shape) == self.img)

        for index,bcontent in enumerate(payload.content):

            unpkcontent = np.unpackbits(bcontent)
            redunpk = np.unpackbits(flatimg[index][0])
            greenunpk = np.unpackbits(flatimg[index][1])
            blueunpk = np.unpackbits(flatimg[index][2])

            redunpk[6:8] = unpkcontent[6:8]
            greenunpk[6:8] = unpkcontent[4:6]
            blueunpk[6:8] = unpkcontent[2:4]

            flatimg[index][0] = np.packbits(redunpk)
            flatimg[index][1] = np.packbits(greenunpk)
            flatimg[index][2] = np.packbits(blueunpk)

        return flatimg.reshape(self.img.shape)



    def extractPayload(self):
        print("Extracting")
        extract = []
        flatimg = np.copy(self.img)
        flatimg.shape = (self.img.shape[0] * self.img.shape[1], 3)
        ncontent = np.zeros(8).astype(dtype=np.uint8)

        for pixel in flatimg:
            red = np.unpackbits(pixel[0])[6:8]
            green = np.unpackbits(pixel[1])[6:8]
            blue = np.unpackbits(pixel[2])[6:8]

            ncontent[6:8] = red
            ncontent[4:6] = green
            ncontent[2:4] = blue

            #extract.append(np.packbits(ncontent))
            extract.extend(np.packbits(ncontent))

        extract = np.array(extract, dtype=np.uint8)

        return Payload(content=extract)

    def payloadExists(self):
        string = r'<?xml version="1.0" encoding="UTF-8"?>'
        encode = base64.b64encode(string.encode('utf-8'))

        vbase64eval = np.vectorize(self.base64eval)
        tempcontent = vbase64eval(list(encode))

        print(len(tempcontent))
        print(tempcontent)

        extract=[]
        ncontent =[0,0]

        flatimg = np.copy(self.img)
        flatimg.shape = (self.img.shape[0] * self.img.shape[1], 3)

        for pixel in flatimg[0:52]:

            red = np.unpackbits(pixel[0])[6:8]
            green = np.unpackbits(pixel[1])[6:8]
            blue = np.unpackbits(pixel[2])[6:8]

            ncontent[6:8] = red
            ncontent[4:6] = green
            ncontent[2:4] = blue

            # extract.append(np.packbits(ncontent))
            extract.extend(np.packbits(ncontent))

        extract = np.array(extract, dtype=np.uint8)
        if np.array_equal(extract[1:len(extract)-1],tempcontent[1:len(tempcontent)-1]):
            return True
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



if __name__ == "__main__":
    carrier = [
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]],
            [[8,8,8], [8,8,8], [8,8,8]]
        ]

    carrier = misc.imread("data/carrier1.png")
    payload = misc.imread("data/payload1.png")

    test = [
        [[3, 3, 3], [4, 5, 6], [7, 8, 9]],
        [[35, 98, 123], [99, 39, 38], [12, 12, 203]],
        [[18, 24, 123], [230, 19, 3], [43, 92, 160]]
    ]
    test2 = [
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    ]
    test = np.array(test, dtype=np.uint8)
    p1 = Payload(img=payload, compressionLevel=9)
    p2 = Payload(content=p1.content)
