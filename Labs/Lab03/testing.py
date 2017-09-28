#! /bin/python3.5

def getPairwiseDifference(vec):
    if not type(vec) is list:
        print("not a list")
        return None
    if len(vec) < 1:
        return None
    result = []

    for i in range(len(vec) - 1):
        result.append(vec[i+1] - vec[i])

    return result

def flatten(l):
    if not type(l) is list:
        print("Not a list")
        return None
    result = []
    for sub in l:
        if not type(sub) is list:
            print("Sublist is not a list: {}".format(sub))
            return None
        for subvals in sub:
            result.append(subvals)

    return result

def partition(l,n):
    pass

def rectifySignal(signal):
    i = 0
    while i < len(signal):
        if signal[i] < 0:
            signal[i] = 0
        i += 1
    return signal



if __name__ == '__main__':
    l = [4 , 3, -2, 3, 4]
    print(l)
    print(getPairwiseDifference(l))

    l = [[4, 3, 4], [9, 'hello', 4], [3, True, "Hi"]]
    print(flatten(l))

    signal = [1, -3, 4, 5, -11, 3, 4]
    print(signal)
    print(rectifySignal(signal))
