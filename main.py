from package import Package
from hashTable import HashTable

def main():
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

    print(table)

if __name__ == "__main__":
    main()