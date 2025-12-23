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
def findNearestPackage(truck, table, totalTime):
    # variable to keep up with trucks current location. Starts at the hub.
    currentLocation = "4001 South 700 East"
    #speed of truck
    speed = 18
    correctionTime = datetime(2025,1,1,10,20,0)
    truckMileage = 0

    # update each package on each truck with loadingTime 
    for packageid in truck:
        packageObj = table.lookUp(str(packageid))
        packageObj.loadingTime = totalTime

    while truck:
        # set shortest Distance variable to 9000 just because none are that far and the loop will set it to the shortest distance it can find
        shortestDistance = 9000
        nearestPackage = None


        for packageid in truck:
            packageObj = table.lookUp(str(packageid))


            # check wrong address constraints for packages
            if "Wrong address" in packageObj.notes and totalTime < correctionTime:
                    continue
            

            packageLocation = packageObj.address
            if "Wrong address" in packageObj.notes:
                packageLocation = "410 S State St"

            currDistance = getDistance(getLocationIndex(packageLocation), getLocationIndex(currentLocation))
            #print(packageLocation)
            #print(currDistance, "\n")




            if shortestDistance > currDistance:
                shortestDistance = currDistance
                nearestPackage = packageid

        # add time it took to deliver pakcage to totaltime
        time = timedelta(hours=shortestDistance / speed)
        totalTime += time

        # add mileage
        truckMileage += shortestDistance

        # remove delivered package and change the trucks current location
        truck.remove(nearestPackage)
        packageObj = table.lookUp(str(nearestPackage))
        packageObj.deliveryTime = totalTime
        currentLocation = packageObj.address

        # print package info for testing
        #print(f'package id: {packageObj.id}\npackage constraints: {packageObj.notes}\ntime delivered: {packageObj.deliveryTime}\nloading time: {packageObj.loadingTime}\n')

        # print statement for testing
        #print(shortestDistance, totalTime, currentLocation)

    return totalTime, truckMileage


##################################################### main #####################################################

def main():
    table = createTable()
    #print(table)
    #print(distances[2][1]) should be 7.1

    # these are for keeping the initial loading sequence later for console interface
    truck1Load = [1, 13, 14, 15, 16, 19, 20, 21, 27, 29, 30, 31, 34, 37, 39, 40]
    truck2Load = [2, 3, 4, 5, 7, 10, 11, 12, 17, 18, 22, 8, 23, 24, 36, 38]
    truck3Load = [6, 25, 9, 28, 32, 26, 33, 35]

    # these lists are the actual trucks and their lists will be manipulated in the delivery algorithm
    truck1 = [1, 13, 14, 15, 16, 19, 20, 21, 27, 29, 30, 31, 34, 37, 39, 40]
    truck2 = [2, 3, 4, 5, 7, 10, 11, 12, 17, 18, 22, 8, 23, 24, 36, 38]
    truck3 = [6, 25, 9, 28, 32, 26, 33, 35]

    # this is departure time for truck 1 and 2, truck3 departs when truck 1 returns to hub
    departureTime = datetime(2025,1,1,8,0,0)

    truck1Time, truck1Mileage = findNearestPackage(truck1, table, departureTime)
    truck2Time, truck2Mileage = findNearestPackage(truck2, table, departureTime)
    # truck 3 leaves when truck1 gets back so i take truck1 time when finishing its deliverys and add 3.7 miles at 18mph to get back to hub and that is when truck 3 departs
    truck3Time, truck3Mileage = findNearestPackage(truck3, table, truck1Time + timedelta(hours=3.7 / 18))

    # code for console interface
    selectedTime = input("hello, please pick a time to check statuses of all packages. (HH:MM)\n")

    # map user input time to datetime obj that can be used as comparison with packages loading and delivery time
    hour, minute = map(int, selectedTime.split(":"))
    checkTime = datetime(2025, 1, 1, hour, minute)

    # if statements for checking package statuses based on the user input time
    delayedPackages = [6,25,28,32]
    for bucket in table.table:
        for item in bucket:
            package = item[1]


            # constraint for package #9 wrong address
            if int(package.id) == 9 and checkTime > datetime(2025,1,1,10,20,0):
                package.address = "410 S State St"

            # constraints for packages 6, 25, 28, 32
            elif int(package.id) in delayedPackages and checkTime < datetime(2025,1,1,9,5,0):
                status = "DELAYED"

            elif checkTime < package.loadingTime:
                status = "At hub"

            elif checkTime < package.deliveryTime:
                status = "En route"

            else:
                status = f"Delivered at {package.deliveryTime.time()}"

            # output which truck package was on
            if int(package.id) in truck1Load:
                print(f"Package {package.id}: {status} on truck 1")
                print(f"Package deadline: {package.deadline}")
                print(f"delivery address: {package.address}\n")
            if int(package.id) in truck2Load:
                print(f"Package {package.id}: {status} on truck 2")
                print(f"Package deadline: {package.deadline}")
                print(f"delivery address: {package.address}\n")
            if int(package.id) in truck3Load:
                print(f"Package {package.id}: {status} on truck 3")
                print(f"Package deadline: {package.deadline}")
                print(f"delivery address: {package.address}\n")

    print(f"truck 1 total mileage: {truck1Mileage}")
    print(f"truck 2 total mileage: {truck2Mileage}")
    print(f"truck 3 total mileage: {truck3Mileage}")
    print(f"total mileage of all trucks: {truck1Mileage + truck2Mileage + truck3Mileage}")


if __name__ == "__main__":
    main()