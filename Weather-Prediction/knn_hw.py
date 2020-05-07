#from scipy.spatial import distance #From SciPy.org https://docs.scipy.org/doc/scipy/reference/spatial.html
import math

def euclidean_distance(data_point1, data_point2):
    """return the Euclidean distance between two dictionary data points from the data set"""
    #squares each key value of the data point to fit the formula distance = sqrt((x1-x2)^2+(y1-y2)^2+(z1-z2)^2)
    TMAX = math.pow((data_point1['TMAX'] - data_point2['TMAX']), 2)
    PRCP = math.pow((data_point1['PRCP'] - data_point2['PRCP']), 2)
    TMIN = math.pow((data_point1['TMIN'] - data_point2['TMIN']), 2)
    #takes the square root of the sum of values to match the distance formula
    return math.sqrt(TMAX + PRCP + TMIN)

def read_dataset(filename):
    """return a list of data point dictionaries read from the specified file"""
    #opens file
    f = open(filename, 'r')
    list = []
    #loops through f
    for line in f:
        dictionary = dict()
        #splits spaces out of line
        line = line.split()
        DATE = line[0]
        #sets each key to a float
        PRCP = float(line[1])
        TMAX = float(line[2])
        TMIN = float(line[3])
        RAIN = line[4]
        #accesses key of dictionary and sets value
        dictionary['DATE'] = DATE
        dictionary['TMAX'] = TMAX
        dictionary['PRCP'] = PRCP
        dictionary['TMIN'] = TMIN
        dictionary['RAIN'] = RAIN
        #adds value to the empty list
        list.append(dictionary)
    return list


def majority_vote(nearest_neighbors):
    """return a prediction of whether it is raining or not based on a majority vote of the list of neighbors"""
    counter = 0
    #loops through nearest_neighbors
    for neighbors in nearest_neighbors:
        #if it is raining at the neighbor's location then the counter increments 1
        if neighbors['RAIN'] == 'TRUE':
            counter += 1
        #if it is not raining at the neighor's location then the counter decrements 1
        elif neighbors['RAIN'] == 'FALSE':
            counter -= 1
    #ties are broken because equal numbers of False and True = 0 which returns True
    if counter >= 0:
        return 'TRUE'
    return 'FALSE'


def k_nearest_neighbors(filename, test_point, k):
    """using the above functions, return the majority vote prediction for whether it's raining or not on the provided test point"""
    points = read_dataset(filename)
    counter = 0
    #arbitrarily high number to include all numbers in data set
    record_low = 999999999999999999999999999999
    record_point = 0
    #sets nearest neighbors to an empty list to add on to later
    nearest_neighbors = []
    #k is the number of neighbors that will be included when determining if it is raining at the location of the neighbors
    while counter < k:
        for point in points:
            #determines closest neighbors and adds them to the empty nearest_neighbors list
            distance = euclidean_distance(point, test_point)
            if distance < record_low:
                record_low = distance
                record_point = point
        nearest_neighbors.append(record_point)
        #removes point from data set so that it is not counted as a neighbor multiple times
        points.remove(point)
        #increments counter
        counter += 1
    return majority_vote(nearest_neighbors)
