def get_stopwords(filename):
    """To read the stop words file"""
    #provided function
    with open(filename, 'r') as f:
        return [word[:-1].replace("'","") for word in f]


def get_text(filename):
    """To read the text document and return a list of words to remove the stopwords from and then be placed into a dictionary using later functions"""
    #provided function
    with open(filename, 'r') as f:
        return get_alphanum(f.read()).split() # USES YOUR FUNCTION


def get_alphanum(text):
    """transforms the argument text string to lowercase, removes all non-alphanumeric characters, and returns the resulting string"""
    text = text.lower()
    new_list = ''
    #loops through all characters in the text and appends alphanumeric characters to a new list
    for character in text:
        if character.isalnum() or character.isspace():
            new_list += character
    return new_list

def remove_stopwords(word_list, stopwords):
    """removes all words that are in the stopwords list from the word list without returning any values"""
    appended = list()
    #loops through word list and adds words that are not also in the stopwords to a new list
    for word in (word_list):
        if word not in stopwords:
            appended.append(word)
    #allows words to be retrievable in test code
    global words
    words = appended




def get_word_freq(word_list):
    """creates and returns a dictionary of frequencies of words in the word list, with the words as keys and the frequencies as values"""
    dictionary = dict()
    #loops through word list and counts how many times a word appears and adds 1 to the frequency each time the word appears
    for word in word_list:
        #counts how many times a word is in the word list
        frequency = word_list.count(word)
        dictionary[word] = frequency
    return dictionary


def get_keywords_threshold(word_freq, threshold):
    """creates and returns a dictionary of words and their frequencies from the provided word_freq dictionary if frequency is over the threshold"""
    new_dictionary = dict()
    for key in word_freq.keys():
        #checks to see if the key of the word is over the threshold
        if word_freq[key] > threshold:
            new_dictionary[key] = word_freq[key]
    #if the key of the word is over the threshold then it is added to the new dictionary and returned
    return new_dictionary


def get_top_keywords(word_freq, n):
    """ creates and returns a dictionary of the highest n keywords in the provided word_freq dictionary"""
    newest_dictionary = dict()
    #sorts the words by the value of their frequency
    values = sorted(word_freq.values())
    #reverses how the words are sorted so that it displays the highest n keywords instead of the lowest n keywords
    values.reverse()
    #creates a dictionary of the highest n keywords
    values = values[:n]
    for keys in word_freq.keys():
        #loops through word_freq that has been previously sorted
        for value in values:
            if word_freq[keys] == value:
                newest_dictionary[keys] = value
    return newest_dictionary
