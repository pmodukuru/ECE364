from pprint import pprint as pp
import math

class PointND:
    def __init__(self, *args):

        for arg in args:
            if not type(arg) is float:
                raise ValueError("Cannot instantiate an object with non-float values.")

        self.n = len(args)
        self.t = tuple(args)

    def __str__(self):
        l = ["{0:.2f}".format(val) for val in self.t]
        return '('+ ', '.join(l) + ')'

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):

        #check cardinality of both
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")

        dist = math.sqrt(sum([(a - b) ** 2 for a,b in zip(self.t, other.t)]))

        return round(dist, 3)

    def nearestPoint(self, points):

        #check if points is empty
        if len(points) == 0:
            raise ValueError("Input cannot be empty.")

        dlist = [self.distanceFrom(point) for point in points]

        return points[dlist.index(min(dlist))]

    def clone(self):
        return PointND(*self.t)

    def __add__(self, other):
        if type(other) is float:
            return PointND(*tuple([a + other for a in self.t]))

        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        return PointND(*tuple([a + b for a,b in zip(self.t, other.t)]))

    def __radd__(self, other):
        if type(other) is float:
            return PointND(*tuple([a + other for a in self.t]))

        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        return PointND(*tuple([a + b for a,b in zip(self.t, other.t)]))

    def __sub__(self, other):
        if type(other) is float:
            return PointND(*tuple([a - other for a in self.t]))

        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        return PointND(*tuple([a - b for a, b in zip(self.t, other.t)]))

    def __rsub__(self, other):
        if type(other) is float:
            return PointND(*tuple([a - other for a in self.t]))

        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        return PointND(*tuple([a - b for a, b in zip(self.t, other.t)]))


    def __mul__(self, other):
        return PointND(*tuple([a * other for a in self.t]))

    def __rmul__(self, other):
        return PointND(*tuple([a * other for a in self.t]))

    def __truediv__(self, other):
        return PointND(*tuple([a / other for a in self.t]))

    def __neg__(self):
        return PointND(*tuple([-a for a in self.t]))

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        # check cardinality of both
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")

        for a,b in zip(self.t, other.t):
            if a != b:
                return False

        return True

    def __ne__(self, other):
        # check cardinality of both
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")

        if self == other:
            return False
        return True

    def __gt__(self, other):
        # check cardinality of both
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")

        #build origin point
        origin = PointND(*tuple([0.0 for val in self.t]))

        if self.distanceFrom(origin) > other.distanceFrom(origin):
            return True

        return False

    def __ge__(self, other):
        # check cardinality of both
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")

        #build origin point
        origin = PointND(*tuple([0.0 for val in self.t]))

        if self.distanceFrom(origin) >= other.distanceFrom(origin):
            return True

        return False

    def __lt__(self, other):
        # check cardinality of both
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")

        #build origin point
        origin = PointND(*tuple([0.0 for val in self.t]))

        if self.distanceFrom(origin) < other.distanceFrom(origin):
            return True

        return False

    def __le__(self, other):
        # check cardinality of both
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")

        #build origin point
        origin = PointND(*tuple([0.0 for val in self.t]))

        if self.distanceFrom(origin) <= other.distanceFrom(origin):
            return True

        return False

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.t = (x,y,z)
        self.n = 3

class PointGroup():
    def __init__(self, **kwargs):
        self._pointmap = {}
        if len(kwargs) == 0:
            self.n = 0
        elif not "pointList" in kwargs:
            raise KeyError("'pointList' input parameter not found.")
        else:
            pointlist = kwargs.get("pointList")
            #check if list is empty
            if len(pointlist) == 0:
                raise ValueError("'pointList' input parameter cannot be empty.")

            self.n = pointlist[0].n

            for point in pointlist:
                if point.n != self.n:
                    raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))

                self._pointmap[point.__hash__()] = point

    def addPoint(self, point):
        if point.n != self.n:
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))

        self._pointmap[point.__hash__()] = point

    def count(self):
        return len(self._pointmap)

    def __iter__(self):
        return iter(self._pointmap.values())

    def clone(self):
        return PointGroup(pointList=list(self._pointmap.values()))

    def __add__(self, point):
        if point.n != self.n:
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))

        temp = self.clone()
        temp._pointmap[point.__hash__()] = point

        return temp

    def __radd__(self, point):
        if point.n != self.n:
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))

        temp = self.clone()
        temp._pointmap[point.__hash__()] = point

        return temp


    def __contains__(self, item):
        for point in self._pointmap.keys():
            if item.__hash__() == point:
                return True

        return False

    def __sub__(self, point):
        temp = self.clone()
        temp._pointmap = dict(self._pointmap)

        if point.__hash__() in temp._pointmap.keys():
            #del temp._pointmap[point.__hash__()]
            temp._pointmap.pop(point.__hash__())

        return temp

    def __rsub__(self, point):
        temp = self.clone()
        temp._pointmap = dict(self._pointmap)

        if point.__hash__() in temp._pointmap.keys():
            #del temp._pointmap[point.__hash__()]
            temp._pointmap.pop(point.__hash__())

        return temp


    def computeBoundingHyperCube(self):
        #build list of list of points
        mlist = [point.t for point in self._pointmap.values()]
        print(mlist)

        maxlist = []
        minlist = []
        for val in zip(*mlist):
            maxlist.append(max(val))
            minlist.append(min(val))

        maxP = PointND(*maxlist)
        minP = PointND(*minlist)

        return (maxP, minP)

    def computeNearestNeighbors(self, otherPointGroup):
        tlist = []
        otherlist = list(otherPointGroup._pointmap.values())
        for point1 in self:
            tlist.append((point1, point1.nearestPoint(otherlist)))

        tlist.sort()

        return tlist

if __name__ == "__main__":

    #testing PointND
    p1 = PointND(1.2,2.1,3.23,4.1)

    print(p1)
    p2 = PointND(1.3, -1.3, -5.0, 2.1)
    p3 = PointND(-1.3, -5.0, 2.1, 12.3)
    print(p1.distanceFrom(p2))
    #print(point.distanceFrom(p3))

    p4 = PointND(1.3,2.1,3.23,4.1)
    p5 = PointND(-1.2,-2.1,-3.23,-4.1)
    points = [p2,p3,p4,p5]
    print(p1.nearestPoint(points))

    #test clone
    print(p1)
    p1c = p1.clone()
    print(p1c)

    #test add
    a1 = PointND(1.0,2.0,-1.0,5.0)
    a2 = PointND(0.0,1.0,3.0,-6.0)
    a3 = a1 + a2
    print(a3)
    print(a1 + 2.0)

    #test sub
    s1 = PointND(1.0, 2.0, -1.0, 5.0)
    s2 = PointND(0.0, 1.0, 3.0, -6.0)
    s3 = s1 - s2
    print(s3)
    print(s1 - 2.0)

    #test mult and div
    print(s1 * 2.0)
    print(s1 / 2.0)

    #test neg
    print(-s2)

    #test get item
    print(s1[3])

    #test eq and ne
    s1 = PointND(1.0, 2.0, -1.0, 5.0)
    s2 = PointND(0.0, 1.0, 3.0, -6.0)
    s1c = s1.clone()

    print(s1 == s2)
    print(s1 != s2)
    print(s1 == s1c)
    print(s1 != s1c)

    #test gt
    s1 = PointND(1000.0, 2.0, -1.0, 5.0)
    s2 = PointND(0.0, 1.0, 3.0, -6.0)
    print(s1 > s2)
    print(s2 > s1)
    print(s1 > s1)

    #test ge
    s1 = PointND(1000.0, 2.0, -1.0, 5.0)
    s2 = PointND(0.0, 1.0, 3.0, -6.0)
    print(s1 >= s2)
    print(s2 >= s1)
    print(s1 >= s1)

    # test lt
    s1 = PointND(1000.0, 2.0, -1.0, 5.0)
    s2 = PointND(0.0, 1.0, 3.0, -6.0)
    print(s1 < s2)
    print(s2 < s1)
    print(s1 < s1)

    # test le
    s1 = PointND(1000.0, 2.0, -1.0, 5.0)
    s2 = PointND(0.0, 1.0, 3.0, -6.0)
    print(s1 <= s2)
    print(s2 <= s1)
    print(s1 <= s1)

    #test Point3D
    p1 = Point3D()
    print(p1)
    p2 = Point3D(3.4, 2, 9.1)
    print(p2)
    p3 = Point3D(1.2, 3.44, -1.2)

    #test pointmap init
    pm1 = PointGroup()
    print(pm1.n)
    pm2 = PointGroup(pointList=[p1, p2, p3])
    print(pm2._pointmap)
    #pm3 = PointGroup(pointList=[p1, s1, p3])

    #test Pointgroup add
    p4 = Point3D(-1.9, 8.1, 0.0)
    pm2 = PointGroup(pointList=[p1, p2, p3])
    print(pm2._pointmap)
    pm2.addPoint(p4)
    print(pm2._pointmap)

    #test len Pointgroup
    pm2 = PointGroup(pointList=[p1, p2, p3])
    pm3 = PointGroup(pointList=[p1, p2, p3])
    pm3.addPoint(p4)

    print(pm2.count())
    print(pm3.count())

    #test clone
    print("testing clone")
    print(pm2._pointmap)
    print(pm2.clone()._pointmap)

    #test add and sub
    p4 = Point3D()
    print(p4.n)
    p5 = Point3D(1.4, 9, 3.1)
    p6 = Point3D(0.2, 0.44, -0.2)

    pm2 = PointGroup(pointList=[p1, p2, p3])
    print(pm2._pointmap)
    pm3 = pm2 + p5
    print(pm3._pointmap)

    #pm2 doesnt have p1
    pm2 = PointGroup(pointList=[p1, p2, p3])
    print(pm2._pointmap)
    pm4 = pm2 - p1
    print(pm4._pointmap)

    print("pm2: " + str(pm2._pointmap))
    pm5 = pm2 - p1
    print("pm5: " + str(pm5._pointmap))
    print("pm2: " + str(pm5._pointmap))

    #test in
    pm2 = PointGroup(pointList=[p1, p2, p3])
    print(p1 in pm2)
    print(p5 in pm2)

    #test hypercube
    pm2 = PointGroup(pointList=[p1, p2, p3])
    hyper = pm2.computeBoundingHyperCube()
    print(hyper[0].t)
    print(hyper[1].t)

    #test neighbors
    p1 = Point3D(-1.3,-.04,1.34)
    p2 = Point3D(3.4, 2, 9.1)
    p3 = Point3D(1.2, 3.44, -1.2)
    p4 = Point3D()
    p5 = Point3D(1.2, 10.2, -3.4)
    p6 = Point3D(-3.2, 3.2, 4.5)
    pm2 = PointGroup(pointList=[p1, p2, p3])
    pm3 = PointGroup(pointList=[p4, p5, p6])

    print(pm2.computeNearestNeighbors(pm3))




