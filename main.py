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

##################################################### main #####################################################

def main():
    table = createTable()
    distances = createDistanceData()
    print(table)
    print(distances[2][1])

if __name__ == "__main__":
    main()