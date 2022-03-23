# This is a sample Python script.
import copy
import random
import matplotlib.pyplot as plt
import math
import itertools


class City:

    def __init__(self, num):
        self.x = random.randint(1, 100)
        self.y = random.randint(1, 100)
        self.number = num
        self.visited = 0


def generateCity(ran):
    cities = []
    for i in range(int(ran)):
        cities.append(City(i))
    return cities


def mydistance(city1: City, city2: City):
    return math.sqrt(pow(city1.x - city2.x, 2) + pow(city1.y - city2.y, 2))

def nearest(city: City, cities: list):
    nearest = 200
    citynum = -1
    dist = 0

    for i in range(len(cities)):

        if cities[i].number != city.number and cities[i].visited == 0:
            dist = mydistance(city,cities[i])
            if dist < nearest:
                nearest = dist
                citynum = cities[i].number


    return citynum



def nearest_neabor(cities:list):
    fastest = []
    wholeDistance = 0

    for i in range(len(cities)):
        temp = copy.deepcopy(cities)
        temp[i].visited = 1
        aCity = i
        aCityCopy = aCity
        dist = 0
        fast = []
        while(aCity != -1):

            fast.append(cities[aCity])
            aCityCopy = aCity
            aCity = nearest(temp[aCity],temp)
            if(aCity != -1):
                temp[aCity].visited = 1
                dist = dist + mydistance(temp[aCityCopy],temp[aCity])
        dist = dist + mydistance(temp[aCityCopy], temp[i])
        if (dist < wholeDistance and dist != 0 ) or i == 0 :
            wholeDistance = dist
            fastest = copy.deepcopy(fast)


    print("\nNEAREST N :")
    print("Minimal distance: ", wholeDistance)
    for i in range(len(fastest)):
        print(str(fastest[i].number), "(", str(fastest[i].x), ",", str(fastest[i].y), ")", end='')
        if (i < len(fastest) - 1):
            print(" --> ", end='')
            plt.plot([fastest[i].x, fastest[i + 1].x], [fastest[i].y, fastest[i + 1].y], "g")



def brutforce(cities: list):
    fastest = []
    minDist = 0
    wholeDistance = 0

    temp = itertools.permutations(cities)
    for i in temp:
        for j in range(len(i) - 1):
            wholeDistance += mydistance(i[j], i[j + 1])
        wholeDistance += (mydistance(i[len(i)-1],i[0]))
        if (wholeDistance < minDist and wholeDistance != 0) or minDist == 0:
            minDist = wholeDistance
            fastest = i
        wholeDistance = 0



    print("BRUTFORCE :")
    print("Minimal distance: ",minDist)
    for i in range(len(fastest)):
        print(str(fastest[i].number),"(",str(fastest[i].x),",",str(fastest[i].y),")",end='')
        if(i < len(fastest)-1):
            print(" --> ",end='')
            plt.plot([fastest[i].x, fastest[i + 1].x], [fastest[i].y, fastest[i + 1].y], "r")
    print()


def dikstra(cities):
    print("j")


if __name__ == '__main__':

    xCord = []
    yCord = []


    cities = generateCity(5)
    # cities[0].x = 5
    # cities[0].y = 80
    # cities[1].x = 24
    # cities[1].y = 75
    # cities[2].x = 0
    # cities[2].y = 56
    # cities[3].x = 3
    # cities[3].y = 70
    # cities[4].x = 39
    # cities[4].y = 47
    for val in cities:
        print("Numer: ", val.number, " X:", val.x, " Y:", val.y)
        xCord.append(val.x)
        yCord.append(val.y)
        plt.text(val.x + 1, val.y + 1, val.number)



    plt.scatter(xCord, yCord)
    xCordCopy = xCord.copy()
    yCordCopy = yCord.copy()
    for i in range(len(xCord) - 1):
        for j in range(i + 1, len(xCord)):
            plt.plot([xCord[i], xCord[j]], [yCord[i], yCord[j]], "b")

    brutforce(cities)
    nearest_neabor(cities)

    plt.show()

