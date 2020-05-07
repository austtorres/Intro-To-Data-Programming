def hamming_distance(name_A, name_B):
    """Determines the Hamming Distance between name_A and name_B"""

    mismatch = 0

  #checks to see if the letters in both names are the same in each corresponding index
    for index in range(len(name_A)):
      if name_A[index] != name_B[index]:

        #indicates how many letters are different between the names
        mismatch += 1

    return mismatch


def name_distance(name_A, name_B):
    """Indicates the distance between name_A and name_B even if the names are a different
    length. If they are the same length the distance is simply their Hamming distance"""

    #Calls previous function if names are the same length
    if len(name_A) == len(name_B):
        return hamming_distance(name_A, name_B)

        #function for when name_A is shorter than name_B
        #adds the difference in the length of the names to the Hamming distance by appending it
    elif len(name_A) < len(name_B):
        distance = list()
        for i in range(len(name_B) - len(name_A) + 1):
            substring = (name_B[i:len(name_A)+i])

            #adds difference in length to Hamming distance
            distance.append(hamming_distance(substring, name_A))
        return min(distance) + len(name_B)-len(name_A)

        #The same function but for if name_B is shorter than name_A
    else:
        distance = list()
        for i in range(len(name_A) - len(name_B) + 1):
            substring = (name_A[i:len(name_B)+i])
            distance.append(hamming_distance(substring, name_B))
        return min(distance) + len(name_A)-len(name_B)


def get_name_lists(file_name):
    """opens a file name, reads its contents, and returns the contents in a list"""

    with open(file_name, 'r') as fr:
        return [name[:-1] for name in fr]


def name_matching(filename, target, k):
    """takes in a list of names from the file, compares the target name to each name in the
    list, and returns a list of names that are within the distance k from the target name"""

    names = get_name_lists(filename)
    students = list()

    #if any names in the file are within the distance k of the target, the names are returned
    for person in names:
        if name_distance(target, person) < k:
            students.append(person)
    return students
