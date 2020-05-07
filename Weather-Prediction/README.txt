Program Skills
Advanced dictionaries
File input

In this program you'll be using the k-Nearest Neighbors algorithm (Links to an external site.) to predict whether we expect it to be raining in Seattle based on various weather conditions. Additionally, this week you'll be writing your own functions to read in the data to use from a CSV file.

Program Requirements
For this assignment, you will write at least four (4) functions with the following names and behaviors (Please ensure that the names match EXACTLY as is):

euclidean_distance(data_point1, data_point2) – return the Euclidean distance between two dictionary data points from the data set.
read_dataset(filename) – return a list of data point dictionaries read from the specified file.
majority_vote(nearest_neighbors) – return a prediction of whether it is raining or not based on a majority vote of the list of neighbors.
k_nearest_neighbors(filename, test_point, k) – using the above functions, return the majority vote prediction for whether it's raining or not on the provided test point.
Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.

1. Euclidean distance
This is what you probably think of as a "normal" distance function:

LaTeX: d\:=\:\sqrt{\left(x_1-\:x_2\right)^2+\left(y_1-y_2\right)^2}d = ( x 1 − x 2 ) 2 + ( y 1 − y 2 ) 2

except in this case we're taking the distance between points in three dimensional space, where those dimensions are the precipitation amount, maximum temperature, and minimum temperature for the day. (You can ignore the date when doing this calculation.)

>>> euclidean_distance({'DATE': '1951-05-19', 'TMAX': 66.0, 'PRCP': 0.0, 'TMIN': 43.0, 'RAIN': 'FALSE'},{'DATE': '1951-01-27', 'TMAX': 33.0, 'PRCP': 0.0, 'TMIN': 19.0, 'RAIN': 'FALSE'}) 
=> 40.80441152620633
>>> euclidean_distance({'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'}, {'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'})
=> 17.694349380522585
2. Read dataset
You've been using our provided file reading functions so far, but this week since we're starting to talk about file I/O you'll be writing your own! Feel free to reference our provided solutions for assistance, but in this case you'll specifically want to read this filePreview the document into a list of dictionaries.

Each line of the filePreview the document looks something like this:

1948-01-01 0.47 51 42 TRUE
where the first entry is the DATE, the second entry is the PRCP (precipitation), the third entry is the TMAX (maximum temperature), the fourth entry is the TMIN (minimum temperature) and the last entry is a boolean representing RAIN (what we'll be predicting for new data points).

In this function, you must read the file in line by line, split each line out with its spaces, and create a dictionary with the keys listed above and the values on the line, where the numeric values have been converted to floats. The function should return a list with one dictionary for each line in the file.

The sample line provided above, for example, should produce the following dictionary:

{'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.47, 'TMIN': 42.0, 'RAIN': 'TRUE'}
We won't show you the whole result of testing this function, but here are some things you can try:

>>> dataset = read_dataset('rain.txt')
>>> len(dataset)
=> 25548
>>> dataset[0]
=> {'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.47, 'TMIN': 42.0, 'RAIN': 'TRUE'}
Again, here's the file for you to read in: rain.txtPreview the document

3. Majority vote
This is how a k-Nearest Neighbor (or kNN) algorithm works: in order to classify a point, you look at the classification of the k points closest to it and say that it has the same label they do (in this case, whether it was raining or not). This function takes in a list of those neighbors, and should return the string representing whether it's raining or not. (Note: this function does not return a boolean!)

If a tie occurs, default to 'TRUE' as your answer. This is Seattle, after all.

>>> majority_vote([{'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'},
{'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'},
{'DATE': '2014-12-05', 'TMAX': 55.0, 'PRCP': 0.12, 'TMIN': 44.0, 'RAIN': 'TRUE'},
{'DATE': '1954-09-08', 'TMAX': 71.0, 'PRCP': 0.02, 'TMIN': 55.0, 'RAIN': 'TRUE'},
{'DATE': '2014-08-27', 'TMAX': 84.0, 'PRCP': 0.0, 'TMIN': 61.0, 'RAIN': 'FALSE'}])
=> 'TRUE'
4. k-Nearest Neighbors
In this function, you'll be given a file with points (to read using your function), a test point dictionary that has all of the same keys except 'RAIN', and the value of k indicating how many neighbors to select.

Find the closest k neighbors using your Euclidean distance, and return their majority vote on whether it's raining or not in the test point.

>>> k_nearest_neighbors('rain.txt', {'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.47, 'TMIN': 42.0}, 2)
=> 'TRUE'
>>> k_nearest_neighbors('rain.txt', {'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.00, 'TMIN': 42.0}, 2)
=> 'FALSE'
>>> k_nearest_neighbors('rain.txt', {'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.00, 'TMIN': 42.0}, 10)
=> 'FALSE'
>>> k_nearest_neighbors('rain.txt', {'DATE': '1948-01-01', 'TMAX': 51.0, 'PRCP': 0.05, 'TMIN': 42.0}, 10)
=> 'TRUE'
