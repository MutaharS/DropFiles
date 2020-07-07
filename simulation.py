import csv

with open("m2.csv") as csvDataFile:
    data = list(csv.reader(csvDataFile))

    len = len(data)
    #Print out x,y,z,r,p,y for sensor1
    #for row in range(1,len):
    #   for x in range(2,8):
    #        print(data[row][x])
    #    print('\n')

    #Print out x,y,z,r,p,y for sensor2
    for row in range(1,len):
        for x in range(9,15):
            print(data[row][x])
        print('\n')