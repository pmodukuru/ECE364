from points import *
from prelab08addon import performProcessing


def createPoint(dataString):
    try:
        p = PointND(*map(float, dataString.split(',')))
    except ValueError as e:
        return e.args
    return p

def distanceBetween(point1, point2):
    try:
        dist = point1.distanceFrom(point2)
    except ValueError as e:
        return e.args

    return dist

def checkVicinity(point, pointList, radius):
    lesser = 0
    greater = 0
    invalid = 0
    for p in pointList:
        try:
            if distanceBetween(point, p) <= radius:
                lesser += 1
            else:
                greater += 1
        except:
            invalid += 1

    return (lesser, greater, invalid)

def checkOperation(*args):
    try:
        performProcessing()
    except ConnectionRefusedError as e:
        raise ConnectionRefusedError(*e.args)
    except OSError as e:
        return "The following Error occurred: {}".format(e.__class__.__name__)
    except Exception as e:
        return False

    return True

if __name__ == "__main__":

    #test 1
    d1 = "3.14,2.701,19.77"
    d2 = "4.98,3FA2,None"
    print(createPoint(d1))
    print(createPoint(d2))

    #test 2
    d1 = "3.14,2.701,19.77"
    p1 = createPoint(d1)
    d2 = "0.00,0.01,2.371"
    p2 = createPoint(d2)
    d3 = "0.00,0.01,2.371,27.23"
    p3 = createPoint(d3)
    print(distanceBetween(p1, p3))

    #test 3
    d1 = "3.14,2.701,19.77"
    p1 = createPoint(d1)
    d2 = "0.00,0.01,2.371"
    p2 = createPoint(d2)
    d3 = "0.00,0.01,2.371,27.23"
    p3 = createPoint(d3)
    d4 = "23.4,45.08,11.2"
    p4 = createPoint(d4)
    d5 = "0.00,0.00,0.00"
    p5 = createPoint(d5)
    print(checkVicinity(p5, [p1,p2,p3,p4,p5], 0.00))

    #test 4
    print(checkOperation("hello"))

