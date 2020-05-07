import csv
def read_csv(path):
    """return a list of the rows from the CSV file at the specified path with
    their column headers as keys, and all numeric data formatted as floats.
    If the file does not exist, return None."""
    try:
        with open(path) as csvfile:
            #uses DictReader module built into python
            reader = csv.DictReader(csvfile)
            new_list = []
            for row in reader:
                row_dict = {}
                #sets column header as each row's key
                for item in row.items():
                    try:
                        #Changes item to float in dictionary
                        row_dict[item[0]] = float(item[1])
                    except ValueError:
                        #does not change anything
                        row_dict[item[0]] = item[1]
                #appends dictionary to list
                new_list.append(row_dict)
            return new_list
    #returns none if file does not exist
    except IOError:
            return None

def print_averages(rows):
    """print each column header from the CSV and the average value in
     that column (if numeric) or a message (if non-numeric)."""
    #keys of the first row become the keys in the dictionary
    for key in rows[0].keys():
        #checks if dictionary value for key is a float
        if isinstance(rows[0][key], (float)):
            col = []
            for row in rows:
                #breaks down dictionaries into pairs of key values
                #learned from tutoring
                for item in row.items():
                    if item[0] == key:
                        col.append(item[1])
            #concatonates everything into message
            print key + ' average = ' + str(sum(col)/len(col))
        else:
            print key + " is non-numeric"
