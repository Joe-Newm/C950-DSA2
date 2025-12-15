# Joseph Newman, Student ID: 012380140

from package import Package
from hashTable import HashTable

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

def getDistance(index1, index2):
    distances = createDistanceData()

    if index1 >= index2:
        return distances[index1][index2]
    else:
        return distances[index2][index1]

def createDictionary():
    dict = {}
    with open("addresses.csv") as file:
        lines = file.readlines()

def findNearestPackage(truck, table, distances):
    currentLocation = "4001 South 700 East"
    for packageid in truck:
        packageObj = table.lookUp(str(packageid))
        packageLocation = packageObj.address
        print(packageLocation)


        
        
        
        


##################################################### main #####################################################

def main():
    table = createTable()
    distances = createDistanceData()
    print(table)
    #print(distances[2][1]) should be 7.1

    # truck 1 
    truck1 = [1, 13, 14, 15, 16, 19, 20, 21, 27, 29, 30, 31, 34, 37, 39, 40]
    # truck 2 
    truck2 = [2, 3, 4, 6, 7, 10, 11, 12, 17, 18, 22, 25, 28, 32, 36, 38]
    # truck 3 
    truck3 = [5, 8, 9, 23, 24, 26, 33, 35]

    findNearestPackage(truck1, table, distances)




if __name__ == "__main__":
    main()