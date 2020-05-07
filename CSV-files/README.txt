CSV Skills

Reading comma-separated value (CSV) files with the csv module
Error handling with try/except

read_csv(path) – return a list of the rows from the CSV file at the specified path with their column headers as keys, and all numeric data formatted as floats. If the file does not exist, return None.
print_averages(rows) – print each column header from the CSV and the average value in that column (if numeric) or a message (if non-numeric).

Read CSV
This function should read a CSV and return the data in list-of-dictionaries form with the numbers converted to floats, like you did on the previous assignment (though last week you read from a .txt file). The twist this week, is that it should read any CSV (unless the file does not exist, in which case you should return None). Last week you knew where the numbers were. This week you'll need to use try and except to make sure your type conversions don't cause errors.

Python's csv module (Links to an external site.) will be helpful, particularly its DictReader, but it won't get you the whole way.

File: fisher.csv

>>> rows = read_csv('fisher.csv')
>>> print rows[0]
{'WID_PETAL': 3.5, 'LEN_SEPAL': 1.4, 'LEN_PETAL': 5.1, 'WID_SEPAL': 0.2}

File: seattleWeatherData.csv

>>> rows = read_csv('seattleWeatherData.csv')
>>> print rows[0]
{'DATE': '1/1/1948', 'TMAX': 51.0, 'PRCP': 0.47, 'TMIN': 42.0, 'RAIN': 'TRUE'}
File: something that does not exist

>>> rows = read_csv('doesnotexist.csv')
>>> print rows
None

Print averages
To make sure you're converting those numeric values to floats, write a function to use your list from read_csv() and print out each column average or a message if the column is non-numeric. Recall dictionary order is (effectively) random, so the order on these lines does not matter.

File: fisher.csvPreview the document

>>> rows = read_csv('fisher.csv')
>>> print_averages(rows)
WID_PETAL average = 3.05733333333
LEN_SEPAL average = 3.758
LEN_PETAL average = 5.84333333333
WID_SEPAL average = 1.19933333333
File: seattleWeatherData.csvPreview the document

>>> rows = read_csv('seattleWeatherData.csv')
>>> print_averages(rows)
DATE is non-numeric
TMAX average = 59.5430562079
PRCP average = 0.106221622045
TMIN average = 44.5133865665
RAIN is non-numeric
