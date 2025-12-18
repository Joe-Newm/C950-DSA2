# Joseph Newman, Student ID: 012380140

from package import Package
from hashTable import HashTable
from datetime import datetime, date, time, timedelta


# function for creating table populated with packages.csv file
def createTable():
    table = HashTable(10)
    # open and read packages file, instantiate package object, add package object to hash table
    with open("packages.csv") as file:
        lines = file.readlines()

        # read each line of file, seperate values by comma
        for line in lines:
            values = line.strip().split(",")

            #check if package has notes, if not add empty string as note
            while len(values) < 8:
                values.append("")
            
            #instantiate package object
            p = Package(*values)
            # add package to hash table
            table.insertItem(p)
    return table


# create list of lists with the distances floats from distances.csv
def createDistanceData():
    distances = []
    with open("distances.csv") as file:
        lines = file.readlines()

        #loop through each line and make list of values on each row
        for line in lines:
            values = line.strip().split(",")

            #append the list to the list of lists
            distances.append(values)

    return distances


# This function will always make the greater index first for finding distances so that it always works correctly
def getDistance(index1, index2):
    distances = createDistanceData()

    if index1 >= index2:
        return float(distances[index1][index2])
    else:
        return float(distances[index2][index1])


# opens addresses.csv and appends each line to an array with the correct index to be used to find distances
def createLocationIndex():
    list = []
    with open("addresses.csv") as file:
        lines = file.readlines()

        for line in lines:
            value = line.strip()
            list.append(value)

    return list


# maps the location value to index that can be used for finding distance between locations
def getLocationIndex(value):
    locationList = createLocationIndex()
    return locationList.index(value)    
    

# algorithm for finding the shortest distance from the truck in order to pick next package delivery
def findNearestPackage(truck, table):
    currentLocation = "4001 South 700 East"
    # set shortest Distance variable to 9000 just because none are that far and the loop will set it to the shortest distance it can find
    shortestDistance = 9000
    totalTime = datetime(2025,1,1,8,0,0)
    #speed of truck
    speed = 18

    for packageid in truck:
        packageObj = table.lookUp(str(packageid))
        packageLocation = packageObj.address
        currDistance = getDistance(getLocationIndex(packageLocation), getLocationIndex(currentLocation))
        #print(packageLocation)
        #print(currDistance, "\n")

        if shortestDistance > currDistance:
            shortestDistance = currDistance


    time = timedelta(hours=shortestDistance / speed)
    totalTime += time

    print(shortestDistance, totalTime)

##################################################### main #####################################################

def main():
    table = createTable()
    #print(table)
    #print(distances[2][1]) should be 7.1

    # truck 1 
    truck1 = [1, 13, 14, 15, 16, 19, 20, 21, 27, 29, 30, 31, 34, 37, 39, 40]
    # truck 2 
    truck2 = [2, 3, 4, 6, 7, 10, 11, 12, 17, 18, 22, 25, 28, 32, 36, 38]
    # truck 3 
    truck3 = [5, 8, 9, 23, 24, 26, 33, 35]

    findNearestPackage(truck1, table)




if __name__ == "__main__":
    main()