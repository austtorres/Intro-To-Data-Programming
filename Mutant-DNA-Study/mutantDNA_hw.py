def is_valid_sequence(seq):
    """Takes in string of DNA sequence and returns True iff its characters are acceptable DNA bases"""

    #Sets which characters are Valid
    valid = "A C G T -"

    #raises a ValueError if there are invalid characters (Characters that are not A,T,C,G or -)
    for element in seq:
        if element not in valid:
            raise ValueError(element + " is not a valid DNA character!")
    return True

def add_indel(seq, pos):
    """Takes in sequence as string and an index in the string to add a '-' to the end of the sequence"""

    #Checks to see if index is in the range of the sequence. If not it raises an IndexError
    #ValueError is raised if sequence contains invalid characters because is_valid_sequence is called
    if is_valid_sequence(seq):
        if pos>len(seq):
            raise IndexError('Index ' + str(pos) + ' is out of range!')

        #adds an indel to the end of the sequence and returns correct message
        else:
            seq_list = list(seq)
            seq_list.insert(pos, '-')
            return "".join(seq_list)

def delete_indel(seq, pos):
    """Takes in sequence as a string and an index and removes an indel from specified position"""

    #Checks to see if sequence is valid
    if is_valid_sequence(seq):
        seq_list = list(seq)

        #Checks if index is out of bounds. If it is an IndexError is raised
        if pos >= len(seq):
            raise IndexError('Index ' + str(pos) + ' is out of range!')

        #Checks to see if indel is at specified index. If not a ValueError is raised
        elif seq_list[pos] != "-":
            raise ValueError('No indel at index ' + str(pos) + '!')

        #otherwise indel is removed from sequence
        else:
            seq_list.pop(pos)
        return "".join(seq_list)

def align_sequences(seq1, seq2):
    """Takes in 2 sequences as strings and adds indels to the shorer one until the two strings are the same length"""

    #Checks to see if both sequences are valid
    if is_valid_sequence(seq1) and is_valid_sequence(seq2):
        match = 0
        mismatch = 0

        #If seq1 is shorter than seq2, indels are added until they are the same length
        if len(seq1) < len(seq2):
            for i in range(len(seq2)-len(seq1)):
                seq1 = add_indel(seq1, len(seq1))

        #If seq2 is shorter than seq1, indels are added until they are the same length
        elif len(seq2) < len(seq1):
            for i in range(len(seq1)-len(seq2)):
                seq2 = add_indel(seq2, len(seq2))
        seq1 = list(seq1)
        seq2 = list(seq2)

        #If the sequences have the same character at the same index, the character is made lowercase
        for index in range(len(seq1)):
            if seq1[index] == seq2[index] and seq1[index] != '-' and seq2[index] != '-':
                seq1[index] = seq1[index].lower()
                seq2[index] = seq2[index].lower()

                #Counts how many characters match each other
                match += 1

            #counts how many characters do not match
            else:
                mismatch += 1
        print "Matches: " + str(match)
        print "Mismatches: " + str(mismatch)
        print "Str1: " + "".join(seq1)
        print "Str2: " + "".join(seq2)
