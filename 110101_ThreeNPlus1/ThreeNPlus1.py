import sys
import datetime

def three_n_plus_one(x):
    currentVal = x

    final = []
    final.append(x)

    while (currentVal != 1) :
        if (currentVal % 2 == 0):
            currentVal = currentVal // 2
        else:
            currentVal = 3 * currentVal + 1
        final.append(currentVal)

    return final


def threeNPlus1CountOnly(x):
    count = 1
    currentVal = x

    while (currentVal != 1) :
        if (currentVal % 2 == 0):
            currentVal = currentVal // 2
        else:
            currentVal = 3 * currentVal + 1
        count += 1

    return count

def threeNPlus1CountOnlyWithCache(x):
    if (x in threeNPlus1CountOnlyWithCache.cacheHash):
        #print("hit", str(x))
        return threeNPlus1CountOnlyWithCache.cacheHash[x]

    result = threeNPlus1CountOnly(x)

    threeNPlus1CountOnlyWithCache.cacheHash[x] = result

    return result

threeNPlus1CountOnlyWithCache.cacheHash = {}


def maxThreeNPlus1(start, end):
    if (start > end):
        t = start
        start = end
        end = t

#    print ("start" + str(start) + " end" + str(end))
    maxInstanceLength = 0

    for c in range(start, end + 1):
        instanceLength = threeNPlus1CountOnlyWithCache(c)
        if (instanceLength > maxInstanceLength):
  #          print(instanceLength)
            maxInstanceLength = instanceLength
 #   print("return" + str(maxInstanceLength))
    return maxInstanceLength


def threeNPLus1FromStdIn():
#    print (datetime.datetime.now())
    for line in sys.stdin:
        if (not line.strip() == ""):
            splitResult = line.split()
            maxResult = maxThreeNPlus1(int(splitResult[0]), int(splitResult[1]))
            print(splitResult[0] + " " + splitResult[1] + " " + str(maxResult))
#    print (datetime.datetime.now())

def main():
    threeNPLus1FromStdIn()

if __name__ == '__main__':
    main()

