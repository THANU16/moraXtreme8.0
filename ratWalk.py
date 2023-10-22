
# find the free area in the x line
def findFreeAreaInXLine(xCoordinates, yCoordinates, yPosition,n,r,w):
    freeXCoordinatesRange = []  
    coordinates = []
    for i in range(0,n):
        if (yCoordinates[i] == yPosition):
            coordinates.append(xCoordinates[i])
    
    if (len(coordinates)>0):
        coordinates.sort()
        # print(coordinates)
        freeDistance = []
        # find the free distance between the wall and the first coordinate
        freeDistance.append(coordinates[0]-r-0)
        if(freeDistance[0]>0):
            freeXCoordinatesRange.append([0,freeDistance[0]])

        # find the free distance between the coordinates
        for i in range(1,len(coordinates)):
            freeDistance.append(coordinates[i] - coordinates[i-1] -2*r)
            if(coordinates[i] - coordinates[i-1] -2*r>0):
                freeXCoordinatesRange.append([coordinates[i-1]+r,coordinates[i]-r])

        # find the free distance between the last coordinate and the wall
        freeDistance.append(w-coordinates[-1]-r) 
        if(freeDistance[-1]>0):
            freeXCoordinatesRange.append([coordinates[-1]+r,w])
        return freeXCoordinatesRange; 


    else: 
        return [[0,w]]   


firstLine = input()
SecondLine = input()
ThirdLine = input()
FourthLine = input()

t = list(map(int, firstLine.split()))[0]
w = list(map(int, firstLine.split()))[1]
h = list(map(int, firstLine.split()))[2]

n = list(map(int, SecondLine.split()))[0]
r = list(map(int, SecondLine.split()))[1]

xCoordinates = list(map(int, ThirdLine.split()))
yCoordinates = list(map(int, FourthLine.split()))


freeXCoordinatesRange = []
    

   
for i in range (0, h+1):
    temp = findFreeAreaInXLine(xCoordinates, yCoordinates, i,n,r,w)
    if(len(temp)>0):
        freeXCoordinatesRange.append(temp)
    else:
        print("CAN'T")